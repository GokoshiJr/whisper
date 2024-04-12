import whisper

model = whisper.load_model("tiny")
result = model.transcribe("audio/test.mp3", fp16=False, language="es")
print(result["text"])
