from openai import OpenAI

def save_transcript_to_srt(transcript, output_srt_path):
    with open(output_srt_path, 'w') as srt_file:
        srt_file.write(transcript)

if __name__ == "__main__":
    client = OpenAI()

    audio_file_path = "./test_com.mp4"
    output_srt_path = "./output_transcript.srt"

    with open(audio_file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file, 
            response_format="srt"
        )

    save_transcript_to_srt(transcript, output_srt_path)
    print(f"Transcription saved to {output_srt_path}")