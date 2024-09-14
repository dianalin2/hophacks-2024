from gtts import gTTS
from RealtimeSTT import AudioToTextRecorder
from pydub import AudioSegment
from pydub.playback import play
import os

def tts(text, lang='en', filename='temp.mp3'):
    gTTS(text, lang=lang, slow=False).save(filename)
    audio = AudioSegment.from_mp3(filename)
    play(audio)
    os.remove(filename)

def process_text(text):
    return text

with AudioToTextRecorder() as recorder:
    recorder.text(process_text)
