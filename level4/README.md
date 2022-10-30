# Level 4

## 环境配置

conda 4.13.0

执行`conda create -n speech_recognition python=3.6`创建python3.6环境

执行`conda activate speech_recognition`激活环境

从github clone [speech_recognition](https://github.com/Uberi/speech_recognition)项目

在clone的项目下执行`python setup.py install`安装speech-recognition

执行`pip install PyAudio PocketSphinx Vosk`安装所需库

参考版本如下

PyAudio             0.2.11

pocketsphinx        0.1.15

vosk                0.3.42

下载vosk的[model](https://alphacephei.com/vosk/models)并解压于根目录model文件夹下，改变语言需要替换相应模型

根目录结构如下

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
da---l         2022/6/30     23:51                examples
da---l         2022/6/30     23:52                model
-a----          2022/7/3     16:06          19181 level4.md

model文件夹下的目录结构如下

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
da---l         2022/6/30     23:52                am
da---l         2022/6/30     23:52                conf
da---l         2022/6/30     23:52                graph
da---l         2022/6/30     23:52                ivector
da---l         2022/6/30     23:52                rescore
da---l         2022/6/30     23:52                rnnlm
-a---l          2022/6/2      3:46             94 README

功能复现中所用模型为

[vosk-model-en-us-0.22](https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip)

[vosk-model-cn-0.22](https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip)

## 功能复现

### 识别麦克风语音

#### 使用vosk-model-en-us-0.22

输入如下

`python .\examples\microphone_recognition.py`

在程序输出`Say something!`后对麦克风说出“one two three”后输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:11:12:13:14:15
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "one two three"
}
```

#### 使用vosk-model-cn-0.22

输入如下

`python .\examples\microphone_recognition.py`

在程序输出`Say something!`后对麦克风说出“一 二 三”后输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:6:7:8:9:10
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "一 二 三"
}
```

### 转录音频文件

#### 使用Sphinx与vosk-model-en-us-0.22识别英文

输入如下

`python .\examples\audio_transcribe_en.py`

输出如下

```
Sphinx thinks you said one two three
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:11:12:13:14:15
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "one two three"
}
```

#### 使用vosk-model-cn-0.22

输入如下

`python .\examples\audio_transcribe_cn.py`

输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:6:7:8:9:10
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "砸 自己 的 脚"
}
```

### 将音频数据保存到音频文件

输入如下

`python .\examples\write_audio.py`

在程序输出`Say something!`后对麦克风说出一段话后输出四个音频文件，格式分别为raw、wav、aiff、flac

### 通过环境噪声水平校准识别器能量阈值

在识别语音前先侦测环境声音以调整语音响应阈值，避免对环境噪声的错误响应

#### 使用vosk-model-en-us-0.22

输入如下

`python .\examples\calibrate_energy_threshold.py`

在程序输出`Say something!`后对麦克风说出“one two three”后输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:11:12:13:14:15
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "one two three"
}
```

#### 使用vosk-model-cn-0.22

输入如下

`python .\examples\calibrate_energy_threshold.py`

在程序输出`Say something!`后对麦克风说出“一 二 三”后输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:6:7:8:9:10
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "一 二 三"
}
```

### 后台识别麦克风语音

利用多线程技术在进行语音识别的同时进行其他任务

#### 使用vosk-model-en-us-0.22

输入如下

`python .\examples\background_listening.py`

在程序输出`Say something!`后对麦克风说出“one two three”后输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:11:12:13:14:15
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "one two three"
}
```

#### 使用vosk-model-cn-0.22

输入如下

`python .\examples\background_listening.py`

在程序输出`Say something!`后对麦克风说出“一 二 三”后输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:6:7:8:9:10
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "一 二 三"
}
```

### 其他有用的识别特性

使用不同的关键词集识别语音，使用的三组关键词集分别为
[("one", 1.0), ("two", 1.0), ("three", 1.0)]

[("wan", 0.95), ("too", 1.0), ("tree", 1.0)]

[("un", 0.95), ("to", 1.0), ("tee", 1.0)]

使用语法识别语音，语法规则如下

```
grammar counting;

public <counting> = ( <digit> ) +;

<digit> = one | two | three | four | five | six | seven ;
```

即重复出现多次数字

输入如下

`python .\examples\special_recognizer_features.py`

输入如下

```
Sphinx recognition for "one two three" with different sets of keywords:
three  two  two  one  one 
tree  too  wan  too  wan 
tee  to  un  to  un  un  un  un 
Sphinx recognition for "one two three" for counting grammar:
INFO: fsg_model.c(700): FSG: 3 states, 7 unique words, 14 transitions (1 null)
INFO: fsg_model.c(208): Computing transitive closure for null transitions
INFO: fsg_model.c(270): 0 null transitions added
one one two three
```

### 队列工作

将接收到的语音信息依次放入队列中，直到按下ctrl+c中断后停止接收，在处理完队列中的全部语音后终止程序

#### 使用vosk-model-en-us-0.22

输入如下

`python .\examples\threaded_workers.py`

在程序输出`Say something!`后对麦克风说出“one two three”、“hello”后输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:11:12:13:14:15
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "one two three"
}
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:11:12:13:14:15
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "hello"
}
```

#### 使用vosk-model-cn-0.22

输入如下

`python .\examples\threaded_workers.py`

在程序输出`Say something!`后对麦克风说出“一 二 三”、“你好”后输出如下

```
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:6:7:8:9:10
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "一 二 三"
}
LOG (VoskAPI:ReadDataFiles():model.cc:213) Decoding params beam=13 max-active=7000 lattice-beam=6
LOG (VoskAPI:ReadDataFiles():model.cc:216) Silence phones 1:2:3:4:5:6:7:8:9:10
LOG (VoskAPI:RemoveOrphanNodes():nnet-nnet.cc:948) Removed 0 orphan nodes.
LOG (VoskAPI:RemoveOrphanComponents():nnet-nnet.cc:847) Removing 0 orphan components.
LOG (VoskAPI:ReadDataFiles():model.cc:248) Loading i-vector extractor from model/ivector/final.ie
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:183) Computing derived variables for iVector extractor
LOG (VoskAPI:ComputeDerivedVars():ivector-extractor.cc:204) Done.
LOG (VoskAPI:ReadDataFiles():model.cc:279) Loading HCLG from model/graph/HCLG.fst
LOG (VoskAPI:ReadDataFiles():model.cc:294) Loading words from model/graph/words.txt
LOG (VoskAPI:ReadDataFiles():model.cc:303) Loading winfo model/graph/phones/word_boundary.int
LOG (VoskAPI:ReadDataFiles():model.cc:310) Loading subtract G.fst model from model/rescore/G.fst
LOG (VoskAPI:ReadDataFiles():model.cc:312) Loading CARPA model from model/rescore/G.carpa
LOG (VoskAPI:ReadDataFiles():model.cc:318) Loading RNNLM model from model/rnnlm/final.raw
Vosk thinks you said {
  "text" : "你好"
}
```
