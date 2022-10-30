#!/usr/bin/env python3

import speech_recognition as sr

from os import path
AUDIO_FILE_EN = path.join(path.dirname(path.realpath(__file__)), "english.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE_EN) as source:
    audio_en = r.record(source)  # read the entire audio file

# recognize keywords using Sphinx
try:
    print("Sphinx recognition for \"one two three\" with different sets of keywords:")
    print(r.recognize_sphinx(audio_en, keyword_entries=[("one", 1.0), ("two", 1.0), ("three", 1.0)]))
    print(r.recognize_sphinx(audio_en, keyword_entries=[("wan", 0.95), ("too", 1.0), ("tree", 1.0)]))
    print(r.recognize_sphinx(audio_en, keyword_entries=[("un", 0.95), ("to", 1.0), ("tee", 1.0)]))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# grammar example using Sphinx
try:
    print("Sphinx recognition for \"one two three\" for counting grammar:")
    print(r.recognize_sphinx(audio_en, grammar='counting.gram'))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
