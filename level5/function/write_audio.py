#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr


def write_audio(adjust=False, output=''):
    output = "" if output == '' else output + "/"
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if adjust:
            r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    # write audio to a RAW file
    with open(output + "microphone-results.raw", "wb") as f:
        f.write(audio.get_raw_data())

    # write audio to a WAV file
    with open(output + "microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    # write audio to an AIFF file
    with open(output + "microphone-results.aiff", "wb") as f:
        f.write(audio.get_aiff_data())

    # write audio to a FLAC file
    with open(output + "microphone-results.flac", "wb") as f:
        f.write(audio.get_flac_data())
