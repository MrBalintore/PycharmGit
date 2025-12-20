import os

from YouTube.youtube_playlist_to_mp3_files.get_application_argv import get_application_argv


def main():
     argv = get_application_argv()
     command_line = " ".join(argv)
     print("command_line=",command_line)
     os.system(command_line)


if __name__ == "__main__":
    main()