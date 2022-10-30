import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Demo of speech_recognition")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--input', help='audio file path to be transcribed')
    group.add_argument('-m', '--micro', action='store_true', help='speech recognition from microphone')
    group.add_argument('-w', '--write', action='store_true', help='write audio from the microphone to files')
    group.add_argument('-t', '--thread', action='store_true', help='speech recognition from microphone with thread')
    parser.add_argument('-e', '--extract', action='store_true', help='extract mono audio from video')
    parser.add_argument('-en', '--english', action='store_true')
    parser.add_argument('-cn', '--chinese', action='store_true')
    parser.add_argument('-a', '--adjust', action='store_true', help='adjust for ambient noise levels')
    parser.add_argument('-g', '--grammar', help='use grammar file')
    args = parser.parse_args()

    # transcribe audio file
    if args.input is not None:
        print('input:{}'.format(args.input))
        try:
            if args.extract:
                from function.extract_audio import extract_audio
                file = extract_audio(args.input)
            else:
                file = args.input
            from function.audio_transcribe import audio_transcribe
            if args.english:
                audio_transcribe('en', file, args.adjust, args.grammar)
            if args.chinese:
                audio_transcribe('cn', file, args.adjust)
        except FileNotFoundError:
            print('FileNotFound!')
            sys.exit(1)

    # microphone_recognition
    if args.micro:
        from function.microphone_recognition import microphone_recognition
        if args.english:
            microphone_recognition('en', args.adjust, args.grammar)
        if args.chinese:
            microphone_recognition('cn', args.adjust)

    if args.write:
        from function.write_audio import write_audio
        write_audio(args.adjust)

    if args.thread:
        from function.threaded_workers import threaded_workers
        if args.english:
            threaded_workers('en', args.adjust, args.grammar)
        if args.chinese:
            threaded_workers('cn', args.adjust)


if __name__ == '__main__':
    main()
