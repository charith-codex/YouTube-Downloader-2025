# pip install yt-dlp
from yt_dlp import YoutubeDL

# Enter the YouTube video URL
url = input("Please enter the YouTube video URL: ")

# Ask the user for their choice: 1 for video, 2 for MP3
print("Enter your choice:")
print("1 - Download Video")
print("2 - Download MP3")

choice = input("Your choice: ").strip()

# Define options for video and MP3
video_options = {
    "format": "bestvideo[height<=1080]+bestaudio/best",  # Video quality
    "outtmpl": "C:/Users/charith/Desktop/%(title)s.%(ext)s",  # File save path
    "cookiefile": "C:/ffmpeg/cookies.txt",  # Cookies file path (if required)
    "progress_hooks": [
        lambda d: print(f"Download Status: {d['status']} - {d.get('filename', '')}")
    ],
}

audio_options = {
    "format": "bestaudio/best",  # Best audio quality
    "outtmpl": "C:/Users/charith/Desktop/%(title)s.%(ext)s",  # File save path
    "postprocessors": [
        {  # Convert audio to MP3
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",  # Bitrate (192kbps)
        }
    ],
    "cookiefile": "C:/ffmpeg/cookies.txt",  # Cookies file path (if required)
    "progress_hooks": [
        lambda d: print(f"Download Status: {d['status']} - {d.get('filename', '')}")
    ],
}

# Choose the appropriate options based on user input
if choice == "1":
    options = video_options
    download_type = "Video"
elif choice == "2":
    options = audio_options
    download_type = "MP3"
else:
    print("Invalid choice. Please enter '1' or '2'.")
    exit()

# Create a YoutubeDL instance with the selected options
with YoutubeDL(options) as ydl:
    try:
        info = ydl.extract_info(url, download=True)  # Download video or audio
        print(f"{download_type} Download Complete: {info['title']}")
    except Exception as e:
        print(f"An error occurred: {e}")
