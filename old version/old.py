# pip install yt-dlp
from yt_dlp import YoutubeDL

# Enter the YouTube video URL
url = input("Please enter the YouTube video URL: ")

# Download options
options = {
    "format": "bestvideo[height<=1080]+bestaudio/best",  # video quality
    "outtmpl": "C:/Users/charith/Desktop/%(title)s.%(ext)s",  # file save path
    "cookiefile": "C:/ffmpeg/cookies.txt",  # cookies file path
    "progress_hooks": [
        lambda d: print(f"Download Status: {d['status']} - {d.get('filename', '')}")
    ],
}

# Create a YoutubeDL instance with options
with YoutubeDL(options) as ydl:
    try:
        info = ydl.extract_info(url, download=True)  # Download video
        print(f"Download Complete: {info['title']}")
    except Exception as e:
        print(f"An error occurred: {e}")
