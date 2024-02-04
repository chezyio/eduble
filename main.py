import subprocess

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

if __name__ == "__main__":
    # Get input file path from user
    input_video_path = input("Enter the input video file path: ").strip()

    # Verify if the input file exists
    try:
        with open(input_video_path):
            pass
    except FileNotFoundError:
        print("Error: Input file not found.")
        exit()

    # Get output file path from user with a valid extension (e.g., .mp4)
    output_video_path = input("Enter the output video file path with a valid extension (e.g., .mp4): ").strip()

    # You can adjust the compression level as needed (0 for lossless, higher for more compression)
    compression_level = 50

    compress_video(input_video_path, output_video_path, compression_level)