import glob
import importlib
import inspect
import json
import os
import random
import time
from time import ctime

import playsound
import requests
import speech_recognition as sr
from gtts import gTTS

from scraper import open_chrome_and_visit_bing

for filename in glob.glob("audio*"):
    os.remove(filename)

# files in package directory
files = os.listdir('package')
# imported modules
imp_modules = []
# all methods from imported modules
all_methods_from_imported_modules = {}

# import all modules
for file in files:
    if not file.startswith('__'):
        name = file.split('.')
        plugin = f"package.{name[0]}"
        imp_modules.append(importlib.import_module(plugin, "."))

# fill the dictionary with functions name as key and the actual function as value
for index, module in enumerate(imp_modules, start=0):
    module_methods = dir(module)
    for item in module_methods:
        if not item.startswith('_'):
            all_methods_from_imported_modules[item] = imp_modules[index].__getattribute__(item)
methods_array = all_methods_from_imported_modules.keys()
print(methods_array)
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
    ran = random.randint(1, 10000000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    while True:
        try:
            tts.save(audio_file)
            break
        except RuntimeError as e:
            print(e)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def login():
    global token, user_id
    url = 'https://bitsapiforbytes.herokuapp.com/extension_login'
    body = {"user": {
        "email": "dravener@gmail.com",
        "password": "papaki1"
    }}
    headers = {'content-type': 'application/json'}
    req = requests.post(url, data=json.dumps(body), headers=headers)
    infos = json.loads(req.text)
    print(infos)
    token = infos["token"]
    user_id = infos["userId"]


def write(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    f = open(file_name, "w+")
    f.write(text_to_append)
    f.close()


def respond(voice_data):
    global resultTextFromSearch, imp_modules, all_methods_from_imported_modules
    all_method = all_methods_from_imported_modules
    if 'good morning' in voice_data:
        gueno_speak('Good morning Captain!')
    if 'what time is it' in voice_data:
        gueno_speak(ctime())
    if 'login' in voice_data:
        login()
    if 'functions' in voice_data:
        print(all_methods_from_imported_modules)
    if 'do you have this function' in voice_data:
        func = input("Enter your function: ")
        all_method['does_gueno_have_function'](func, all_methods_from_imported_modules, gueno_speak, inspect)
    if 'info' in voice_data:
        print(token, user_id)
    # in progress of creating navigator that will help user navigate browser
    if 'open browser' in voice_data:
        all_method['open_browser']()
        all_method['go_to_website']('google')
        all_method['find_element']('button')
    # in progress of creating navigator that will help user navigate browser
    if 'search' in voice_data:
        try:
            for filenam in glob.glob("pages-files-*"):
                os.remove(filenam)
        except FileNotFoundError:
            print('No Such file exists to remove.')
        search_input = input("Enter your search: ")
        resultTextFromSearch = open_chrome_and_visit_bing(search_input, token, user_id)
        # print(resultTextFromSearch)
        i = random.randint(1, 10000000)
        for (key, value) in resultTextFromSearch.items():
            print(key)
            try:
                write('pages-files-' + str(i) + key + '.txt', value)
            except FileNotFoundError:
                print('No Such file exists to remove.')
    if 'exit' in voice_data:
        exit()


time.sleep(1)
gueno_speak("Hello Captain")
while 1:
    # voice_data = record_audio()
    search = input("Enter your command: ")
    respond(search)
