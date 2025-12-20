from pytube import Playlist
import sys
def get_videos_from_playlist(playlist_url):
    """
    Given a YouTube playlist URL, returns a list of (title, video_url) tuples.
    """
    try:
        playlist = Playlist(playlist_url)
        videos = [(video.title, video.watch_url) for video in playlist.videos]
        return videos
    except Exception as e:
        print(f"Error fetching playlist: {e}")
        return []

# Example usage
if __name__ == "__main__":
    sample_id = 'PLRhWUdOnZHklr5GcNBO7dDsTspk85M8eH'
    lsid = len(sample_id)
    print(lsid)
    sample_url = 'https://www.youtube.com/watch?v=EWdNhA5prXQ&list=PLRhWUdOnZHklr5GcNBO7dDsTspk85M8eH'
    p1 = "tVj0ZTS4WF4"
    p2 = "PL51ECD03F3389E312"
    l1 = len(p1)
    l2 = len(p2)
    print(len(p1),len(p2))
    my_url     = "https://www.youtube.com/watch?v=tVj0ZTS4WF4&list=PL51ECD03F3389E312"
    url = sample_url
    url = 'https://www.youtube.com/watch?v=EWdNhA5prXQ&list=PLRhWUdOnZHklr5GcNBO7dDsTspk85M8eH'
    url = 'https://www.youtube.com/watch?v=tVj0ZTS4WF4&list=PL51ECD03F3389E312'
    #playlist = Playlist('https://www.youtube.com/watch?v=EWdNhA5prXQ&list=PLRhWUdOnZHklr5GcNBO7dDsTspk85M8eH')
    playlist = Playlist(url)
    print('Number Of Videos In playlist: %s' % len(playlist.video_urls))
    sys.exit(0)
    for video in playlist.videos:
        video.streams.first().download()
    sys.exit(0)
    YOUR_PLAYLIST_ID = "PL51ECD03F3389E312"
    url = f"https://www.youtube.com/playlist?list={YOUR_PLAYLIST_ID}"
    url="https://www.youtube.com/watch?v=tVj0ZTS4WF4&list=PL51ECD03F3389E312"
    videos = get_videos_from_playlist(url)
    for i, (title, link) in enumerate(videos, start=1):
        print(f"{i}. {title} — {link}")
