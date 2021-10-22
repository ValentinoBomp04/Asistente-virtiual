from typing import Text
import speech_recognition as SR
import pyttsx3
import pywhatkit
import urllib.request
import json

name = 'Jarvis'

key = 'AIzaSyCd63lau8iNV1N8PcVWqu50bcSuc11EtMM'

listener = SR.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)


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
        music = rec.replace('reproduce','')
        talk('reproduciendo'+ music)
        pywhatkit.playonyt(music)
    if 'cuantos suscriptores tiene' in rec:
        sub_num = rec.replace('cuantos suscriptores tiene', '')
        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=%27'+ sub_num.strip() + '&key=' + key).read()
        subs = json.loads(data)["items"][0]["stadistics"]["subscriberCount"]
        talk(sub_num + "tiene {:,d}".format(int(subs))+"suscriptores")

funciones()