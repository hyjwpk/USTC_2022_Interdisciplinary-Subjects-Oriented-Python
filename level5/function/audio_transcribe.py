#!/usr/bin/env python3

import speech_recognition as sr
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")


def audio_transcribe(language='en', file=AUDIO_FILE, adjust=False, grammar=None):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        if adjust:
            r.adjust_for_ambient_noise(source)
        audio = r.record(source)  # read the entire audio file

    if language == 'en':
        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_sphinx(audio, grammar=grammar))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    else:
        # recognize speech using Vosk
        try:
            print("Vosk thinks you said " + r.recognize_vosk(audio))
        except sr.UnknownValueError:
            print("Vosk could not understand audio")
        except sr.RequestError as e:
            print("Vosk error; {0}".format(e))
