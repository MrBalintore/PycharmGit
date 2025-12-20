def get_application_argv():
     exe = r"C:\ProgramData\anaconda3\python.exe"
     py_script = r"C:\Users\david\PycharmProjects\PycharmGit\YouTube\youtube_playlist_to_mp3_files\youtube_playlist_to_mp3_files.py"
     bronowski_url = "https://www.youtube.com/watch?v=YHUvpbxlccE&list=PLgLsAOMxeaBBjyO3FtEuGV0VVOHXzAMfq"
     bronowski_url = "https://www.youtube.com/playlist?list=PLgLsAOMxeaBBjyO3FtEuGV0VVOHXzAMfq"
     url = bronowski_url

     my_output_path = "\"D:\\My Documents\\My Audio\""
     action = "False"
     parts = [exe, py_script, "--action", action, "--output_path", my_output_path, url]
     return parts
