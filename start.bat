@echo off
cd /d "%~dp0"

cd scripts

:menu
cls
echo ============================
echo       CONVERTER MENU
echo ============================
echo 1. Run YT2MP3 (yt2mp3.py)
echo 2. Run MP4 Convert (convert.py)
echo 3. Exit
echo.

set /p choice=Select option (1/2/3): 

if "%choice%"=="1" goto yt2mp3
if "%choice%"=="2" goto convert
if "%choice%"=="3" goto exit

echo.
echo Invalid choice. Try again.
timeout /t 2 >nul
goto menu

:yt2mp3
echo.
echo Starting yt2mp3 converter...
python yt2mp3.py
echo.
pause
goto menu

:convert
echo.
echo Starting mp4 to mp3 converter...
python convert.py
echo.
pause
goto menu

:exit
echo Exiting...
exit