import os
import sys
from YouTube.youtube_playlist_to_mp3_files.get_application_argv import get_application_argv

from YouTube.youtube_playlist_to_mp3_files.youtube_playlist_to_mp3_files import main as application_main
def main():
     argv = get_application_argv()
     sys.argv = [ s.replace("\"","") for s in argv[1:] ] # omit the python
     print(f"sys.argv={sys.argv}")
     application_main()

     #command_line = " ".join(argv)
     #print("command_line=",command_line)
     #os.system(command_line)


if __name__ == "__main__":
    main()