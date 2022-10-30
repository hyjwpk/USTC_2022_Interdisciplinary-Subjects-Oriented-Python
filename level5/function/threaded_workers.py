#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

from threading import Thread

try:
    from queue import Queue  # Python 3 import
except ImportError:
    from Queue import Queue  # Python 2 import

import speech_recognition as sr


def threaded_workers(language='en', adjust=False, grammar=None):
    r = sr.Recognizer()
    audio_queue = Queue()

    def recognize_worker():
        # this runs in a background thread
        while True:
            audio = audio_queue.get()  # retrieve the next audio processing job from the main thread
            if audio is None:
                break  # stop processing if the main thread is done

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

            audio_queue.task_done()  # mark the audio processing job as completed in the queue

    # start a new thread to recognize audio, while this thread focuses on listening
    recognize_thread = Thread(target=recognize_worker)
    recognize_thread.daemon = True
    recognize_thread.start()
    with sr.Microphone() as source:
        if adjust:
            r.adjust_for_ambient_noise(source)
        try:
            while True:  # repeatedly listen for phrases and put the resulting audio on the audio processing job queue
                print("Say something!")
                audio_queue.put(r.listen(source))
        except KeyboardInterrupt:  # allow Ctrl + C to shut down the program
            print('exit')

    audio_queue.join()  # block until all current audio processing jobs are done
    audio_queue.put(None)  # tell the recognize_thread to stop
    recognize_thread.join()  # wait for the recognize_thread to actually stop
