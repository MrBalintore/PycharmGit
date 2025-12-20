
def seconds_to_time_string(total_seconds):
    total_seconds = int(total_seconds)
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{hours}:{minutes}:{seconds}'

def video_id_to_video_url(video_id):
        video_prefix = "https://www.youtube.com/watch?v="
        return video_prefix + str(video_id)


def get_video_information(playist_id, youtube):
    # start loop round playlist segments
    i = 0
    nextPageToken = None
    all_requested_items = []
    all_returned_items  = []
    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails,snippet',
            playlistId=playist_id,
            maxResults=50,
            pageToken=nextPageToken
        )

        pl_segment = pl_request.execute()
        all_requested_items += pl_segment['items']

        segment_vid_ids_requested = [item['contentDetails']['videoId'] for item in pl_segment['items']]

        vid_request = youtube.videos().list(
            part="contentDetails,snippet",
            id=','.join(segment_vid_ids_requested)
        )
        n_request_items = len(pl_segment['items'])
        vid_response = vid_request.execute()
        all_returned_items += vid_response['items']####

        n_response_items = len(vid_response['items'])

        debug = False
        if debug:
            if n_request_items != n_response_items:
                print(f"differing request({n_request_items}) and response({n_response_items})")


        for item in vid_response['items']:
            title = item['snippet']['title']
            print(f"playlist video[{i}]={title}")
            i += 1

        nextPageToken = pl_segment.get('nextPageToken')

        if not nextPageToken:
            break
    # stop loop round playlist segments
    all_requested_ids = [item['contentDetails']['videoId'] for item in all_requested_items]
    all_returned_ids = [item['id'] for item in all_returned_items ]
    all_missing_ids = list(set(all_requested_ids) - set(all_returned_ids))
    all_missing_urls = list(map(video_id_to_video_url, all_missing_ids))
    #### return all_items, all_missing_urls # work with all_items below here
    return all_returned_items, all_requested_items


def generate_missing_urls(all_requested_items, all_returned_items):
    all_requested_ids = [item['contentDetails']['videoId'] for item in all_requested_items]
    all_returned_ids = [item['id'] for item in all_returned_items]
    all_missing_ids = list(set(all_requested_ids) - set(all_returned_ids))
    all_missing_urls = list(map(video_id_to_video_url, all_missing_ids))
    return all_missing_urls


def get_playlist_info(playist_id, youtube):
    req = youtube.playlists().list(part='snippet', id=playist_id)
    res = req.execute()
    return res

# get API key
#https://www.youtube.com/watch?v=th5_9woFJmk


# how to get the duration of a youtube playlist
#https://www.youtube.com/watch?v=coZbOM6E47I


#https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to
#https://console.cloud.google.com/



