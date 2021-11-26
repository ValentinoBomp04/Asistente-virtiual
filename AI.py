from typing import Text
import speech_recognition as SR
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime

name = 'Jarvis'

key = 'AIzaSyCd63lau8iNV1N8PcVWqu50bcSuc11EtMM'

flag = 1

listener = SR.Recognizer()


engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)

engine. setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def talk(text):
     engine.say(text)
     engine.runAndWait()

def listen():
    '''
        The program recover our voice and it sends to another function
    '''
    flag = 1
    try:
        with SR.Microphone() as source:
            print('Escuchando..')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                flag= funciones(rec)
            else:
                talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return flag

def funciones():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce','')
        talk('reproduciendo'+ music)
        pywhatkit.playonyt(music)
    elif 'cuantos suscriptores tiene' in rec:
        sub_num = rec.replace('cuantos suscriptores tiene', '')
        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=%27'+ sub_num.strip() + '&key=' + key).read()
        subs = json.loads(data)["items"][0]["stadistics"]["subscriberCount"]
        talk(sub_num + "tiene {:,d}".format(int(subs))+"suscriptores")

    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
     
    elif 'exit' in rec:
        flag = 0
        talk("Saliendo...")
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return flag

while flag:
    flag = listen()
