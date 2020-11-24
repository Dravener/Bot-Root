import speech_recognition as sr

r = sr.Recognizer()


def record_audio(gueno_speak, ask=False):
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
