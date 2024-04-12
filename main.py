import whisper, time
from whisper.utils import get_writer

try:
    start = time.perf_counter()
    model = whisper.load_model("tiny")
    result = model.transcribe("audio/test.mp3", fp16=False, language="es", initial_prompt="prompt", word_timestamps=True)
    writer = get_writer(output_format="all", output_dir="target")
    writer(result, "audio/test.mp3")
    end = time.perf_counter() - start
    print("Tiempo de ejecucion: ", end)
except Exception as e:
    print(e.with_traceback())
