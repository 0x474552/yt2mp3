# yt2mp3 & Audio Converter

> **Disclaimer:** This tool is intended for downloading and converting content that you own or have permission to use. 

This project was created for educational purposes. Users are solely responsible for complying with applicable laws and the terms of service of any platform used.

---

## FFmpeg Licensing
This project includes FFmpeg, licensed under the GNU LGPL v2.1+ or GNU GPL v2+. 
© The FFmpeg developers — https://ffmpeg.org/

---

## Overview
This repository contains Python scripts to easily convert media to MP3 format:
- **`yt2mp3.py`** - Downloads and converts YouTube or SoundCloud links directly to MP3 files.
- **`convert.py`** - Converts local MP4 video files to MP3 audio files.
- Might rework it or add more in the future...

---

## Setup & Usage

### 1. Prerequisites
- **Python:** Ensure you have Python installed on your system.
- **FFmpeg:** This project requires FFmpeg to handle audio conversion. 
  - Run the script `download-ffmpeg.bat` to download ffmpeg into the folders meant for the scripts.
  - It will download it as a zip package and extracts into `resources/ffmpeg/`.
  - If you re-arrange the folder structure, you would have to modify the python scripts to handle the new folder structure also.

### 2. Install Dependencies
Before running the scripts, install the required Python packages by running:
```bash
pip install -r requirements.txt
```

### 3. Run the Tool
Execute the `start.bat` file by double-clicking it or running it in your command prompt:
```bat
start.bat
```
- `start.bat` will give you an option to run either `yt2mp3.py` or `convert.py`.
- Other necessary details are self-explanatory when you run the batch file.

---

## Tips & Maintenance
- **Keep `yt-dlp` updated:** YouTube and SoundCloud frequently update their sites. Keeping the `yt-dlp` package up to date will prevent common errors while executing the script. You can update it anytime by running:
  ```bash
  pip install -U yt-dlp
  ```

- **Update FFMPEG (if you have to):** Simply delete the resources folder and run `download-ffmpeg.bat` again, as it fetches the latest stable essential build for it, downloads the zip package and extracts it accordingly.