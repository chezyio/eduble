import subprocess
from openai import OpenAI

def compress_video(input_file, output_file, compression_level=23):
    """
    Compress video using FFmpeg.

    Parameters:
    - input_file: Input video file path.
    - output_file: Output video file path.
    - compression_level: Compression level for the output video (default is 23).

    Note: Compression level ranges from 0 (lossless) to 51 (worst quality).
    """
    # FFmpeg command to compress video
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_file,          # Input file
        '-c:v', 'libx264',         # Video codec (H.264)
        '-crf', str(compression_level),  # Compression level (0-51, lower values mean higher quality)
        '-c:a', 'aac',             # Audio codec (AAC)
        '-strict', 'experimental',  # Allow experimental codecs (for AAC)
        output_file                 # Output file
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

if __name__ == "__main__":
    # Compress video
    input_video_path = "./test.mp4"
    compressed_video_path = "./test_com.mp4"
    compression_level = 40
    compress_video(input_video_path, compressed_video_path, compression_level)

    # Transcribe with Whisper
    client = OpenAI()
    
    with open(compressed_video_path, "rb") as compressed_video_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=compressed_video_file,  # Pass the compressed video file
            response_format="srt"
        )

    output_srt_path = "./output_transcript.srt"
    save_transcript_to_srt(transcript, output_srt_path)
    print(f"Transcription saved to {output_srt_path}")