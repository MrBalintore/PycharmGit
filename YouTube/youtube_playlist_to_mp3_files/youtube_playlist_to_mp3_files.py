import os
import sys
from parse_arguments import app_parse_args
#from YouTube.youtube_playlist_to_mp3_files.read_playlist_wrapper import read_playlist_wrapper


def main():
    print(f"youtube_playlist_to_mp3_files:main sys.argv={sys.argv}")
    """
    youtube_playlist_to_mp3_files playlist_url
                                  output_path=.
                                  download_audio=True
                                  download_video=False
                                  action=True
                                  api_key = "AIzaSyDBtBPHzW0TGMbH3pra0eSWtaW4rmTBTEM"

    write a python program to parse command line arguments
    1st argument is playlist_url
    optional keyword arguments are output_path, download_audio, download_video, action, api_key
    default values are .  , True, False, True, AIzaSyDBtBPHzW0TGMbH3pra0eSWtaW4rmTBTEM respectvely

working command line

sys.argv=['C:\\Users\\david\\PycharmProjects\\PycharmGit\\YouTube\\youtube_playlist_to_mp3_files\\youtube_playlist_to_mp3_files.py', '--action', 'False', '--output_path', 'D:\\My Documents\\My Audio', 'https://www.youtube.com/playlist?list=PLgLsAOMxeaBBjyO3FtEuGV0VVOHXzAMfq']
Parsed arguments:

failing command line

sys.argv=['C:\\ProgramData\\anaconda3\\python.exe', 'C:\\Users\\david\\PycharmProjects\\PycharmGit\\YouTube\\youtube_playlist_to_mp3_files\\youtube_playlist_to_mp3_files.py', '--action', 'False', '--output_path', '"D:\\My Documents\\My Audio"', 'https://www.youtube.com/playlist?list=PLgLsAOMxeaBBjyO3FtEuGV0VVOHXzAMfq']
sys.argv=['C:\\Users\\david\\PycharmProjects\\PycharmGit\\YouTube\\youtube_playlist_to_mp3_files\\youtube_playlist_to_mp3_files.py', '--action', 'False', '--output_path', '"D:\\My Documents\\My Audio"', 'https://www.youtube.com/playlist?list=PLgLsAOMxeaBBjyO3FtEuGV0VVOHXzAMfq']


    """
    from YouTube.youtube_playlist_to_mp3_files.read_playlist_wrapper import read_playlist_wrapper
    api_key = os.environ.get('YT_API_KEY')
    my_dance_music_video_url = "https://www.youtube.com/playlist?list=PL51ECD03F3389E312"
    my_dance_music_2_url = "https://www.youtube.com/playlist?list=PLgLsAOMxeaBDhVozIxZnTmLJKFyebQ11P"
    my_music_videos_url = "https://www.youtube.com/playlist?list=PLgLsAOMxeaBD_baXCuU75ABawiZ0TCwQc"
    python_tutorials_url = "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"
    bronowski_url = "https://www.youtube.com/watch?v=YHUvpbxlccE&list=PLgLsAOMxeaBBjyO3FtEuGV0VVOHXzAMfq"
    url = bronowski_url
    url = my_music_videos_url
    url = my_dance_music_2_url

    my_output_path = """D:\\My Documents\\My Audio"""

    args = app_parse_args()
    read_playlist_wrapper(
                          args.playlist_url,
                          output_path = args.output_path,
                          action = args.action,
                          api_key = args.api_key,
                          download_audio=args.download_audio,
                          download_video=args.download_video
                          )

if __name__ == "__main__":
    main()
