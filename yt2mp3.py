import os
import re
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

YOUTUBE_URL_PATTERN = re.compile(
    r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/[\w\-\?=&#/]+$"
)
SOUNDCLOUD_URL_PATTERN = re.compile(
    r"^(https?://)?(www\.)?(soundcloud\.com)/[\w\-\?=&#/]+$"
)

def is_youtube_url(url):
    return bool(YOUTUBE_URL_PATTERN.match(url))

def is_soundcloud_url(url):
    return bool(SOUNDCLOUD_URL_PATTERN.match(url))

def download_mp3(url, output_dir=OUTPUT_DIR):
    try:
        print(f"\nDownloading from: {url}")
        print(f"Saving to: {output_dir}")

        os.makedirs(output_dir, exist_ok=True)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'ffmpeg_location': os.path.join(BASE_DIR, 'ffmpeg', 'tools', 'ffmpeg', 'bin'),
            'geo_bypass': True, # prevent api failures
            'noplaylist': True, # download only current song
            'retries': 2,
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '0',
                }
            ],
            'quiet': False
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download complete!\n")

    except DownloadError as e:
        error_msg = str(e).lower()
        if "timed out" in error_msg:
            print("Connection timed out. Check your internet connection or try again later.")
        elif "could not connect" in error_msg or "failed to resolve" in error_msg:
            print("Cannot connect to YouTube servers, try again later.\n")
        elif "slow" in error_msg or "connection reset" in error_msg:
            print("Connection is too slow. Try again later.\n")
        else:
            print(f"yt-dlp error: {e}\n")

    except socket.timeout:
        print("Socket timeout. Your internet might be unstable.\n")

    except Exception as e:
        print(f"Unknown error: {e}\n")

def main():
    while True:
        print("Select platform to download:")
        print("1. Youtube")
        print("2. Soundcloud")
        print("Type 'exit' to quit.")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "exit":
            print("Exiting...")
            break

        if choice not in ("1", "2"):
            print("Invalid choice\n")
            continue

        while True:
            url = input("Paste the URL (or type 'back' to reselect platform, 'exit' to quit): ").strip()
            if url.lower() == "exit":
                print("Exiting...")
                return
            if url.lower() == "back":
                print("Returning to platform selection...\n")
                break
            if not url:
                print("Enter a URL.\n")
                continue

            if choice == "1":
                if not is_youtube_url(url):
                    print("Invalid Youtube URL.")
                    continue
            elif choice == "2":
                if not is_soundcloud_url(url):
                    print("Invalid Soundcloud URL.")
                    continue

            download_mp3(url)

if __name__ == "__main__":
    main()
