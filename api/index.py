


from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import subprocess
from openai import OpenAI
import re
from nltk.tokenize import sent_tokenize
from summarizer import Summarizer
import cv2
import datetime

app = Flask(__name__)
CORS(app)

# Set the upload folder
UPLOAD_FOLDER = '../uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def compress_video(input_file, output_file, compression_level=23):
    # FFmpeg command to compress video
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_file,          
        '-c:v', 'libx264',         
        '-crf', str(compression_level),  
        '-c:a', 'aac',             
        '-strict', 'experimental',  
        output_file                 
    ]

    try:
        # Run FFmpeg command
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Compression completed. Output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during compression: {e}")

def save_transcript_to_srt(transcript, output_srt_path):
    with open(output_srt_path, 'w') as srt_file:
        srt_file.write(transcript)

def extract_and_display_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        subtitle_content = file.read()

    # Use regular expressions to remove timestamps and numbers
    subtitle_content = re.sub(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+\n', '', subtitle_content)
    subtitle_content = re.sub(r'\d+\n', '', subtitle_content)

    # Split the content into subtitles based on the empty lines
    subtitles = subtitle_content.split('\n\n')

    # Extract sentences from each subtitle
    sentences = []
    for subtitle in subtitles:
        # Use NLTK's sentence tokenizer to extract sentences
        subtitle_sentences = sent_tokenize(subtitle)
        sentences.extend(subtitle_sentences)

    # Return the extracted sentences
    return sentences

def summarize_text(text):
    model = Summarizer()
    optimal_k = model.calculate_optimal_k(text, k_max=20)
    result = model(text, num_sentences=optimal_k)
    summarized_text = ''.join(result)
    return summarized_text

def generate_frames_with_timestamps(video_path, timestamps, output_folder):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for timestamp in timestamps:
        # Convert timestamp to seconds
        timestamp_parts = re.match(r'(\d+):(\d+):(\d+),(\d+)', timestamp)
        if timestamp_parts:
            hours, minutes, seconds, milliseconds = map(int, timestamp_parts.groups())
            timestamp_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
        else:
            print(f"Invalid timestamp format: {timestamp}")
            continue

        # Set the video capture position to the corresponding timestamp
        cap.set(cv2.CAP_PROP_POS_MSEC, timestamp_seconds * 1000)

        # Read the frame
        ret, frame = cap.read()

        if ret:
            # Save the frame with timestamp as the filename
            frame_filename = f"{timestamp.replace(':', '_')}.jpg"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame)

    cap.release()

@app.route('/api/video', methods=['POST'])
def process_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # If the user does not select a file, the browser also
    # submits an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Check if the file has an allowed extension
    if file and allowed_file(file.filename):
        # Generate a secure filename
        filename = secure_filename(file.filename)

        # Save the file to the upload folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Compress the video
        compressed_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'compressed_' + filename)
        compress_video(file_path, compressed_file_path)

        # Transcribe with Whisper
        client = OpenAI()
        
        with open(compressed_file_path, "rb") as compressed_video_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=compressed_video_file,
                response_format="srt"
            )

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                    "role": "system",
                    "content": "translate input into Chinese."
                    },
                    {
                    "role": "user",
                    "content": transcript
                    }
                ],
                temperature=0.7,
                max_tokens=5000,
                top_p=1
             )

        translated_chinese = response.choices[0].message.content

        # Save the transcript to SRT file
        output_srt_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output_transcript.srt')
        save_transcript_to_srt(transcript, output_srt_path)

        # Extract sentences from the SRT file
        sentences = extract_and_display_sentences(output_srt_path)

        # Summarize the extracted sentences
        summarized_text = summarize_text(' '.join(sentences))

        # Extract timestamps and generate frames with OpenCV
        subtitles_content = open(output_srt_path).read()
        timestamps = re.findall(r'(\d+:\d+:\d+,\d+) --> \d+:\d+:\d+,\d+', subtitles_content)
        output_frames_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'frames')
        generate_frames_with_timestamps(compressed_file_path, timestamps, output_frames_folder)

        return jsonify({'filename': filename, 'message': 'File processed successfully', 'transcript': transcript, 'summarized_text': summarized_text, 'frames_folder': output_frames_folder, 'translated_chinese': translated_chinese})

    return jsonify({'error': 'Invalid file format'})

if __name__ == '__main__':
    app.run(port=5328)