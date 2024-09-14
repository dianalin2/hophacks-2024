from RealtimeSTT import AudioToTextRecorder

def process_text(text):
    return text

with AudioToTextRecorder() as recorder:
    recorder.text(process_text)

