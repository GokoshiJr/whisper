mkdir target
mkdir audio

python -m venv venv
venv\scripts\activate.bat
pip install

whisper .\test.mp3 --model tiny --language Spanish --fp16 False --output_dir .\target

tiny
small
base
medium
large
