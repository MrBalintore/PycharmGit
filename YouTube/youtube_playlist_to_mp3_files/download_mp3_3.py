import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "url"
url = str("https://www.youtube.com/watch?v=QsZ0g61Ymhc")


def download_video_as_mp3(url, media_file, download_audio=True, download_video=False):
    #yt = YouTube(url, "WEB", on_progress_callback=on_progress)
    yt = YouTube(url, "WEB", on_progress_callback=on_progress, use_po_token=True)
    if (download_audio):
        #all_streams = yt.streams.filter(only_audio=True).all()
        #print(f"all_streams={all_streams}")
        #audio_stream_first = yt.streams.filter(only_audio=True).first()
        print("aaa")
        audio_stream_last = yt.streams.filter(only_audio=True).last()
        print("bbb")
        #audio_stream_best = yt.streams.get_audio_only()
        audio_stream = audio_stream_last
        #downloaded_audio_file = audio_stream.download(
        #    filename =mp3_filename,
        #     output_path=output_path
        #)
        downloaded_audio_file = audio_stream.download(
            filename = os.path.basename(media_file),
            output_path=os.path.dirname(media_file)
        )
        print(f"downloaded_audio_file={downloaded_audio_file}")


    if ( download_video ):
        ys = yt.streams.get_highest_resolution()
        output_path = os.path.dirname(media_file)
        downloaded_video_file = ys.download(output_path=output_path)
        print(f"downloaded_video_file={downloaded_video_file}")

def main():
    url = "url"
    url = str("https://www.youtube.com/watch?v=QsZ0g61Ymhc")

    my_output_path = r"""D:\My Documents\My Audio"""
    print("output_path={output_path}")
    media = "media"
    media = my_output_path
    download_video_as_mp3(url,output_path=media)

if __name__ == "__main__":
    main()