@echo off
set "DOWNLOAD_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
set "ZIP_FILE=ffmpeg-download.zip"
set "EXTRACT_FOLDER=ffmpeg-extracted"
set "TARGET_FOLDER=resources\ffmpeg"

@REM Download latest stable build from gyan.dev (.zip format)
echo Downloading the latest stable ffmpeg essentials build...
powershell -Command "Invoke-WebRequest -Uri '%DOWNLOAD_URL%' -OutFile '%ZIP_FILE%'"

@REM Extracts the downloaded .zip file into a temporary folder
echo Extracting downloaded zip file...
powershell -Command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '%EXTRACT_FOLDER%' -Force"

echo Creating target directory structure...
echo Structure: "resources/ffmpeg/.."
if not exist "%TARGET_FOLDER%" mkdir "%TARGET_FOLDER%"

echo Moving extracted files over...
:: Loop through the extracted directory to find the inner folder (e.g., ffmpeg-x.x-essentials_build)
for /d %%D in ("%EXTRACT_FOLDER%\*") do (
    xcopy "%%D\*" "%TARGET_FOLDER%\" /E /I /H /Y /Q
)

@REM Clean up downloaded .zip and the temporary folder for extraction
echo Cleaning up temporary files...
del "%ZIP_FILE%"
rmdir /s /q "%EXTRACT_FOLDER%"

echo Done! FFmpeg is now located at %TARGET_FOLDER%
pause