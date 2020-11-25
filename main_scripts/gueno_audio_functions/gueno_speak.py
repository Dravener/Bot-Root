import os
import random

import playsound
from gtts import gTTS


def tell_me(previous_function: str, all_methods, user_input):
    tts = gTTS(text=previous_function, lang='en')
    ran = random.randint(1, 10000000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    while True:
        try:
            tts.save(audio_file)
            break
        except ValueError as e:
            print(e)
    playsound.playsound(audio_file)
    print(previous_function)
    os.remove(audio_file)
