import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
from time import ctime
import time
import json
import requests
from scraper import openChromeAndVisitBing

r = sr.Recognizer()
token = ''
user_id = ''
resultTextFromSearch = 'init'
image_text = ''


def record_audio(ask=False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if ask:
            gueno_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            gueno_speak('Did not get that.')
        except sr.RequestError:
            gueno_speak('Server Down')
        print(voice_data)
        return voice_data


def gueno_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    while True:
        try:
            tts.save(audio_file)
            break
        except:
            print('got the issue ')
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def login():
    global token, user_id
    url = 'https://bitsapiforbytes.herokuapp.com/extension_login'
    body = {"user": {
        "email": "your_account_email",
        "password": "password"
    }}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(body), headers=headers)
    infos = json.loads(r.text)
    token = infos["token"]
    user_id = infos["userId"]


def respond(voice_data):
    global resultTextFromSearch
    if 'good morning' in voice_data:
        gueno_speak('Good morning Captain!')
    if 'what time is it' in voice_data:
        gueno_speak(ctime())
    if 'login' in voice_data:
        login()
    if 'info' in voice_data:
        print(token, user_id)
    if 'search' in voice_data:
        search = input("Enter your search: ")
        resultTextFromSearch = openChromeAndVisitBing(search)
        for (key, value) in resultTextFromSearch.items():
            print(key, value)
            print('===================================================================================================')
    if 'exit' in voice_data:
        exit()


time.sleep(1)
gueno_speak("Hello Captain")
while 1:
    # voice_data = record_audio()
    search = input("Enter your command: ")
    respond(search)
