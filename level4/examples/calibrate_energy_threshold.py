#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Vosk
try:
    print("Vosk thinks you said " + r.recognize_vosk(audio))
except sr.UnknownValueError:
    print("Vosk could not understand audio")
except sr.RequestError as e:
    print("Vosk error; {0}".format(e))
