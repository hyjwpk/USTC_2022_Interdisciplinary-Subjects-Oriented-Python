# level3.15

## 题目

**（加** **1** **分）【计算机】**基于 Python 的 faceswap 等工具，对自己的视频文件进行人脸替换，例如改为动画人物

提示：类似魔术/川剧中的变脸

## 运行环境

[faceswap](https://faceswap.dev/)

## 换脸步骤

1.从视频中提取存在人脸的对应帧并生成信息文件（fsa），用extract函数实现

2.对提取出的帧按照人脸进行排序，用sort函数实现

3.将不需要的人脸删除后，更新信息文件（fsa），用alignments_clean函数实现

4.从信息文件中重新提取人脸对应帧，用alignments_extract函数实现

5.输入需要替换的人脸视频的帧和被替换的人脸视频的帧，进行学习生成模型，用train函数实现

6.使用学习的模型将视频的人脸进行替换，输出替换后的帧文件，用convert函数实现

7.将替换后的帧文件合并输出视频，使用generate函数实现

## 输入输出示例

输入的视频文件为A_1.mp4、A_2.mp4、C.flv，source.flv，输出的人脸帧文件在A、B、C文件夹中，信息文件为A_1_alignments.fsa、A_2_alignments.fsa、C_alignments.fsa，训练的模型在model、model_2文件夹中，视频文件为output1.mp4(动漫人物)、output2.mp4(真人)、output3.mp4(真人)。

源码在main.py中，运行前需删除对应函数前的注释并修改参数路径
