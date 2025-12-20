from urllib.parse import urlparse, parse_qs


def get_playlist_id(url: str) -> str | None:
    """Extracts the YouTube playlist ID from a playlist URL."""
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get("list", [None])[0]
