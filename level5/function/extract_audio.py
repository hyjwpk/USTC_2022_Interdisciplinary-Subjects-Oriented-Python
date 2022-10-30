from moviepy.editor import AudioFileClip


def extract_audio(path, output=''):
    # extract mono audio from video
    my_audio_clip = AudioFileClip(path)
    output = "output.wav" if output == '' else output + "/output.wav"
    my_audio_clip.write_audiofile(output, ffmpeg_params=['-ac', '1'])
    return output
