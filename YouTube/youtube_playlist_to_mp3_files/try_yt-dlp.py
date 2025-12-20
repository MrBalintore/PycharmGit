#https://www.reddit.com/r/youtubedl/comments/1efqwrt/python_api/

import tkinter


import customtkinter
import yt_dlp


# download function

def startDownload():
    try:
        yt_link = link.get()
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]

        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(yt_link)
        print("Download Complete")


    except:
        print("Error")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI elemets

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(pady=10)

# RubApp
app.mainloop()
"""
https://www.reddit.com/r/youtubedl/comments/qzqzaz/can_someone_please_post_a_simple_guide_on_making/
yt-dlp -x --audio-format mp3 -i PLlaN88a7y2_rosKX2WQt2VjFbjyDQXOkR


yt-dlp -x --audio-format mp3 -i --ffmpeg-location "C:\Users\david\ffmpeg-8.0-full_build\ffmpeg-8.0-full_build\bin"  https://www.youtube.com/watch?v=tVj0ZTS4WF4&list=PLgLsAOMxeaBDhVozIxZnTmLJKFyebQ11P 

download dance music playlist
=============================
yt-dlp -x --audio-format mp3 -i https://www.youtube.com/playlist?list=PLgLsAOMxeaBDhVozIxZnTmLJKFyebQ11P

download music videos
=====================
yt-dlp -x -t sleep --audio-format mp3 -i https://www.youtube.com/playlist?list=PLgLsAOMxeaBD_baXCuU75ABawiZ0TCwQc

broknowski lectured
====================
yt-dlp -x --audio-format mp3 -i https://www.youtube.com/playlist?list=PLgLsAOMxeaBBjyO3FtEuGV0VVOHXzAMfq

"""

