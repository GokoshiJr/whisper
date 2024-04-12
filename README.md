# Create folders
mkdir target
mkdir audio

# Setup

## Create virtual env
python -m venv venv
venv\scripts\activate.bat

## Install dependencies
pip install -r requirements.txt

## on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

whisper .\test.mp3 --model tiny --language Spanish --fp16 False --output_dir .\target

tiny
small
base
medium
large
