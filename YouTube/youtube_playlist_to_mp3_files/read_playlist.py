import os
import pprint
from pprint import pformat

from googleapiclient.discovery import build

from YouTube.youtube_playlist_to_mp3_files.download_mp3_3 import download_video_as_mp3
from YouTube.youtube_playlist_to_mp3_files.duration_to_seconds import duration_to_seconds
from YouTube.youtube_playlist_to_mp3_files.read_playlist_utilities import get_playlist_info, get_video_information, \
    generate_missing_urls, seconds_to_time_string, video_id_to_video_url


def read_playlist(playist_id, output_path=".",
                  action=True,
                  api_key="AIzaSyDBtBPHzW0TGMbH3pra0eSWtaW4rmTBTEM",
                  download_audio = True,
                  download_video = False):
    debug = False
    youtube = build('youtube', 'v3', developerKey=api_key)


    res = get_playlist_info(playist_id, youtube)

    play_list_title = res["items"][0]['snippet']['title']

    returned_items, requested_items = get_video_information(playist_id, youtube)

    missing_urls = generate_missing_urls(requested_items, returned_items)

    n_videos = len(returned_items)

    print(f"missing_urls=\n{pformat(missing_urls)}")

    playlist_output_path = os.path.join(output_path, play_list_title)
    if not os.path.exists(playlist_output_path):
        os.makedirs(playlist_output_path)
    # start loop round videos

    total_time = seconds_to_time_string(sum( map( duration_to_seconds, [ item['contentDetails']['duration'] for item in returned_items] )))
    print(f"{n_videos} videos with total duration {total_time} in playlist |{play_list_title}| ")

    failed_downloads = {}

    for i, item in enumerate(returned_items):  # only get video details of videos that are present !
        video_id = item['id']
        video_title = item["snippet"]["title"]
        video_filename = video_title.replace("/","")
        video_url = video_id_to_video_url(video_id)


        raw = True
        if action:
            if raw:
                check_and_download(download_audio, download_video, i, playlist_output_path, returned_items,
                                   video_filename,
                                   video_url)
            else:
                try:
                    check_and_download(download_audio, download_video, i, playlist_output_path, returned_items,
                                       video_filename,
                                       video_url)

                except Exception as e:
                    title = item['snippet']['title']
                    failed_downloads[i] = { "video_url":video_url,"Exception":e, "title":title }
    failed_downloads_s = pprint.pformat(failed_downloads)
    print(f"failed_downloads={failed_downloads_s}")


    # stop loop round videos


def check_and_download(download_audio, download_video, i, playlist_output_path, returned_items, video_title, video_url):
    print(f"processing video {i + 1} of {len(returned_items)} |{video_title}|", flush=True)
    if download_audio:
        extension = ".mp3"
    else:
        extension = ".mp4"
    media_file = os.path.join(playlist_output_path, video_title + extension)
    if not os.path.exists(media_file):
        download_video_as_mp3(video_url,
                              media_file,
                              download_audio=download_audio,
                              download_video=download_video)
    else:
        print(f"{media_file} already present")
