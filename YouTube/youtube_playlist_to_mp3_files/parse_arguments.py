import argparse

def app_parse_args():
    parser = argparse.ArgumentParser(
        description="Parse playlist download arguments."
    )

    # Positional argument
    parser.add_argument(
        "playlist_url",
        help="The URL of the playlist to process."
    )

    # Optional keyword arguments
    parser.add_argument(
        "--output_path",
        default=".",
        help="The output directory path (default: current directory)."
    )

    parser.add_argument(
        "--download_audio",
        type=bool,
        default=True,
        help="Whether to download audio (default: True)."
    )

    parser.add_argument(
        "--download_video",
        type=bool,
        default=False,
        help="Whether to download video (default: False)."
    )

    parser.add_argument(
        "--action",
        type=bool,
        default=True,
        help="Whether to perform the main action (default: True)."
    )

    parser.add_argument(
        "--api_key",
        default="AIzaSyDBtBPHzW0TGMbH3pra0eSWtaW4rmTBTEM",
        help="API key to use (default: pre-set key)."
    )

    args = parser.parse_args()

    # Display parsed arguments
    print("Parsed arguments:")
    print(f"Playlist URL   : {args.playlist_url}")
    print(f"Output Path    : {args.output_path}")
    print(f"Download Audio : {args.download_audio}")
    print(f"Download Video : {args.download_video}")
    print(f"Action         : {args.action}")
    print(f"API Key        : {args.api_key}")
    return args


if __name__ == "__main__":
    app_parse_args()
