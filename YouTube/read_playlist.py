import os
from pytube import Playlist, YouTube
from moviepy.editor import AudioFileClip

# -------- SETTINGS --------
PLAYLIST_URL = "YOUR_PLAYLIST_URL_HERE"
OUTPUT_DIR = "downloads"  # folder to save MP3s
PLAYLIST_URL = """https://www.youtube.com/watch?v=QZvlY_7-nJA&list=PLgLsAOMxeaBDY5gCNyUhDS_1pLrcuTdBX"""
OUTPUT_DIR = r"C:\Users\david\Downloads\MP3S"

# --------------------------

def download_playlist_as_mp3(url, output_dir="downloads"):
    # Create output folder if not exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    playlist = Playlist(url)
    print(f"Downloading playlist: {playlist.title}")

    for video_url in playlist.video_urls:
        try:
            yt = YouTube(video_url)
            print(f"\nDownloading: {yt.title}")

            # Download best audio stream
            audio_stream = yt.streams.filter(only_audio=True).first()
            temp_file = audio_stream.download(output_path=output_dir)

            # Convert to MP3
            base, ext = os.path.splitext(temp_file)
            mp3_file = base + ".mp3"

            audio_clip = AudioFileClip(temp_file)
            audio_clip.write_audiofile(mp3_file, codec="mp3")
            audio_clip.close()

            # Remove original file (mp4/webm)
            os.remove(temp_file)

            print(f"Saved as: {mp3_file}")
        except Exception as e:
            print(f"Failed to process {video_url}: {e}")


if __name__ == "__main__":
    download_playlist_as_mp3(PLAYLIST_URL, OUTPUT_DIR)
