import speech_recognition as sr


r = sr.Recognizer()

def start_transcribe():
    transcript = None
    with sr.Microphone() as source:
        print("Start Speaking")                # use the default microphone as the audio source
        audio = r.listen(source)
    try:
        transcript = r.recognize_google(audio, language='en-US') # recognize speech using Google Speech Recognition
    except:                            # speech is unintelligible
        print("Could not understand audio")
    return transcript
