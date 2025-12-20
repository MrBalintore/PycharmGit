from YouTube.youtube_playlist_to_mp3_files.get_playlist_id import get_playlist_id
from YouTube.youtube_playlist_to_mp3_files.read_playlist import read_playlist


def read_playlist_wrapper(playlist_url,
                          output_path = ".",
                          action=True,
                          api_key="AIzaSyDBtBPHzW0TGMbH3pra0eSWtaW4rmTBTEM",
                          download_audio = True,
                          download_video=False)    :

    playlist_id = get_playlist_id(playlist_url)
    read_playlist(playlist_id, output_path=output_path, action=action, api_key=api_key)
