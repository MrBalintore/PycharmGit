from YouTube.youtube_playlist_to_mp3_files.get_playlist_id import get_playlist_id


# Example usage:
def main():
    playlist_url = "https://www.youtube.com/playlist?list=PLynG1vM8FLxQAvb4SmBS2YVdc0PygXnh5"
    playlist_id = get_playlist_id(playlist_url)
    print(playlist_id)


if __name__ == "__main__":
    main()
