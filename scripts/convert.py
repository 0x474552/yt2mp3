import os
import subprocess
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_DIR = os.path.join(BASE_DIR, "mp4_input")
OUTPUT_DIR = os.path.join(BASE_DIR, "mp3_output")

BITRATE = "192k"
Q_SCALE = "2"  # for -q:a

COUNTER_FILE = os.path.join(BASE_DIR, "scripts", "count.txt")

# FFMPEG_BIN = os.path.join(BASE_DIR, "resources", "ffmpeg", "tools", "ffmpeg", "bin", "ffmpeg.exe")
# new ffmpeg location in resources/
FFMPEG_BIN = os.path.join(BASE_DIR, 'resources','ffmpeg', 'bin'),

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(INPUT_DIR, exist_ok=True)

# load counter
if os.path.exists(COUNTER_FILE):
    try:
        with open(COUNTER_FILE, "r") as f:
            counter = int(f.read().strip() or 1)
    except ValueError:
        counter = 1
else:
    counter = 1

today = datetime.now().strftime("%Y%m%d")

files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".mp4")]
failed_files = []
success_count = 0

for filename in files:
    input_path = os.path.join(INPUT_DIR, filename)

    print(f"\nFile: {filename}")
    print("1 = -q:a (better quality")
    print("2 = -b:a (fixed bitrate)")
    
    choice = input("Choose mode (default = 2): ").strip()

    serial = f"{counter:03d}" # format number with leading 0s and 3 digits
    output_filename = f"{today}_{serial}.mp3"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    if choice == "1":
        print("Using -q:a mode")
        command = [
            FFMPEG_BIN,
            "-y",
            "-i", input_path,
            "-vn",
            "-q:a", Q_SCALE,
            output_path
        ]
    else:
        print("Using -b:a mode")
        command = [
            FFMPEG_BIN,
            "-y",
            "-i", input_path,
            "-vn",
            "-b:a", BITRATE,
            output_path
        ]

    print(f"Converting -> {output_filename}")

    try:
        subprocess.run(command, check=True)
        counter += 1
        success_count += 1
    except subprocess.CalledProcessError:
        print(f"Conversion failed: {filename}")
        failed_files.append(filename)

# save counter
with open(COUNTER_FILE, "w") as f:
    f.write(str(counter))

print("\nCompleted.")
print(f"\nSuccessfully converted: {success_count}")

if failed_files:
    print("\nFailed files:")
    for f in failed_files:
        print(f"- {f}")
else:
    print("\nConverted all files.")