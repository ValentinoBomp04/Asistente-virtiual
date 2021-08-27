from typing import Text
import speech_recognition as SR
import pyttsx3

name = 'jarvis'

listener = SR.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

for voice in voices:
    print(voice)

def talk(text):
     engine.say(text)
     engine.runAndWait()


def listen():
    try:
        with SR.Microphone() as source:
            print('Escuchando..')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)

    except:
        pass
    return rec


def funciones():
    rec = listen()
    if 'reproduce' in rec:
         talk(rec)

funciones()