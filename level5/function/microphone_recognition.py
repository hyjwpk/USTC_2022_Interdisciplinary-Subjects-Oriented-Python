#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr


def microphone_recognition(language='en', adjust=False, grammar=None):
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if adjust:
            r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

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
