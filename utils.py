import re


def is_youtube_url(url: str) -> bool:
    pattern = r"^(https?://)?(www\.|m\.)?(youtube\.com|youtu\.be)/(watch\?v=|embed/|v/|shorts/)?([^&\n?#]+)"
    return bool(re.match(pattern, url, re.IGNORECASE))
