import os


def extract(__video_path, __output_path):
    args = " -D s3fd -A fan -nm none -rf 0 -min 0 -l 0.4 -sz 512 -een 1 -si 0 -L INFO "
    cmd = python_path + faceswap_path + " extract -i " + __video_path + " -o " + __output_path + args
    print(cmd)
    os.system(cmd)


def sort(__image_path):
    args = " -s face -t -1.0 -fp rename -g hist -b 5 -lf sort_log.json -L INFO "
    cmd = python_path + tool_path + " sort -i " + __image_path + args
    print(cmd)
    os.system(cmd)


def alignments_clean(__alignments_path, __image_path):
    args = " -een 1 -sz 512 -L INFO "
    cmd = python_path + tool_path + " alignments -j remove-faces -o console -a " + __alignments_path + \
        " -fc " + __image_path + args
    print(cmd)
    os.system(cmd)


def alignments_extract(__alignments_path, __image_path, __video_path):
    args = " -een 1 -sz 512 -L INFO "
    cmd = python_path + tool_path + " alignments -j extract -o console -a " + __alignments_path + \
        " -fc " + __image_path + " -fr " + __video_path + args
    print(cmd)
    os.system(cmd)


def train(__image_A_path, __image_B_path, __model_path):
    args = " -t original -bs 16 -it 1000000 -s 250 -ss 25000 -ps 100 -L INFO "
    cmd = python_path + faceswap_path + " train -A " + __image_A_path + " -B " + __image_B_path + \
        " -m " + __model_path + args
    print(cmd)
    os.system(cmd)


def convert(__video_path, __output_path, __model_path):
    args = " -c avg-color -M extended -w opencv -osc 100 -l 0.4 -j 0 -L INFO "
    cmd = python_path + faceswap_path + " convert -i " + __video_path + " -o " + __output_path + \
        " -m " + __model_path + args
    print(cmd)
    os.system(cmd)


def generate(__image_path, __output_path, __video_path):
    args = " -fps -1.0 -ef .png -s 00:00:00 -e 00:00:00 -d 00:00:00 -sc 1920x1080 -L INFO "
    cmd = python_path + tool_path + " effmpeg -a gen-vid -i " + __image_path + " -o " + __output_path +\
        " -r " + __video_path + args
    print(cmd)
    os.system(cmd)


python_path = " C:/ProgramData/Anaconda3/envs/faceswap/python.exe "
faceswap_path = " C:/Users/wangc/faceswap/faceswap.py "
tool_path = " C:/Users/wangc/faceswap/tools.py "
video_path = " C:/Users/wangc/Downloads/A_1.mp4 "
output_path = " C:/Users/wangc/Downloads/Temp "
alignments_path = "C:/Users/wangc/Downloads/A_1_alignments.fsa"
image_A_path = "C:/Users/wangc/Downloads/A"
image_B_path = "C:/Users/wangc/Downloads/B"
model_path = "C:/Users/wangc/Downloads/model"
out_video_path = "C:/Users/wangc/Downloads/output1.mp4"


# extract(video_path, output_path)
# sort(output_path)
# alignments_clean(alignments_path, output_path)
# alignments_extract(alignments_path, output_path, video_path)
# train(image_A_path, image_B_path, model_path)
# convert(video_path, output_path, model_path)
# generate(output_path, out_video_path, video_path)
