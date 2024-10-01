import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Start Speaking")                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    print(r.recognize_google(audio, language='en-US'))    # recognize speech using Google Speech Recognition
except:                            # speech is unintelligible
    print("Could not understand audio")

print("hi")