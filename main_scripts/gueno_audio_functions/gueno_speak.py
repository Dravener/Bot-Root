import os
import random

import playsound
from gtts import gTTS


def gueno_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    ran = random.randint(1, 10000000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    while True:
        try:
            tts.save(audio_file)
            break
        except ValueError as e:
            print(e)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)