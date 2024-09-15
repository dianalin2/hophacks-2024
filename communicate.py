from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
import speech_recognition as sr
import os

def start_transcribe():
    r = sr.Recognizer()
    transcription = None
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("Say something!")
        audio = r.listen(source)

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            transcription = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return transcription

def tts(text, lang='en', filename='temp.mp3'):
    gTTS(text, lang=lang, slow=False).save(filename)
    # audio = AudioSegment.from_mp3(filename)
    # play(audio)
    playsound(filename)
    os.remove(filename)

