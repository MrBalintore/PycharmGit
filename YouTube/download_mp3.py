from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_as_mp3(url, output_path='.'):
    """
    Downloads the audio from a YouTube URL, converts it to MP3, and saves it.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str): The directory to save the MP3 file.
    """
    try:
        print("# 1. Create a YouTube object")
        yt = YouTube(url)

        print("# 2. Get the best audio stream (usually WebM or MP4)")
        # You can also filter by abr (average bitrate) for specific quality
        audio_stream = yt.streams.filter(only_audio=True).first()
        if not audio_stream:
            print("No audio stream found.")
            return

        print("# 3. Download the audio stream to a temporary file")
        downloaded_file = audio_stream.download(output_path=output_path)
        base, ext = os.path.splitext(downloaded_file)

        # 4. Convert the downloaded file to MP3 using pydub and FFmpeg
        # If the downloaded file is already an mp3, we can just rename it.
        if ext != '.mp3':
            # Load the audio file
            audio = AudioSegment.from_file(downloaded_file)

            # Define the new filename with the .mp3 extension
            new_file_path = f"{base}.mp3"

            # Export as MP3
            audio.export(new_file_path, format="mp3")

            # Remove the original downloaded file
            os.remove(downloaded_file)
            print(f"'{yt.title}' downloaded and converted to MP3: {new_file_path}")
        else:
            # If already MP3, just rename it (though pytube often doesn't give it .mp3 directly)
            new_file_path = f"{base}.mp3"
            os.rename(downloaded_file, new_file_path)
            print(f"'{yt.title}' downloaded as MP3: {new_file_path}")


    except Exception as e:
        print(f"An error occurred: {e}")
        raise e # throw again so we can trap and record

# Example usage:
#video_url = input("Enter YouTube video URL: ")
print("Enter YouTube video URL: ")
video_url = str("https://www.youtube.com/watch?v=QsZ0g61Ymhc",output_path="media")
download_youtube_as_mp3(video_url)
