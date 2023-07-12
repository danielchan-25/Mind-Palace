# Whisper

> https://github.com/openai/whisper

## 介绍

**Whisper** 是一个由 OpenAI 训练并开源的神经网络，在英语语音识别方面的稳健性和准确性接近人类水平，支持其它98种语言的自动语音辨识。

Whisper系统所提供的自动语音辨识（Automatic Speech Recognition，ASR）模型是被训练来运行语音辨识与翻译任务的，它们能将各种语言的语音变成文本，也能将这些文本翻译成英文。

### 运行模型以及所需配置

目前 Whisper 有 9 种模型（分为纯英文和多语言），其中四种只有英文版本

以下是现有模型的大小，及其内存要求和相对速度

| 大小   | 参数   | 纯英文模型 | 多语言模型 | 所需显存 | 速度 |
| ------ | ------ | ---------- | ---------- | -------- | ---- |
| tiny   | 39 M   | tiny.en    | tiny       | ~1 GB    | ~32x |
| base   | 74 M   | base.en    | base       | ~1 GB    | ~16x |
| small  | 244 M  | small.en   | small      | ~2 GB    | ~6x  |
| medium | 769 M  | medium.en  | medium     | ~5 GB    | ~2x  |
| large  | 1550 M | N/A        | large      | ~10 GB   | 1x   |

## 部署

> OS：Ubuntu 22.04.1 LTS

先创建一个 Python 环境：

```sh
conda create --name whisper python==3.9.7
conda activate whisper
```

直接安装

```sh
pip install -U openai-whisper
pip install git+https://github.com/openai/whisper.git
```

## 使用

1. 先找一段带文字的音频，如：`audio.mp3`
2. 执行命令：`whisper audio.mp3 --model tiny --language Chinese `
3. 等待模型下载
4. 生成字幕了！（为什么生成的中文都是繁体字？）



经测试，模型越大，出错率越低

以下是我在网上采摘一段文字，转成mp3文件后，再使用 `Whisper` 转回中文的真实测试：

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/whisper-1.png)



---

2023/06/28 更新

> 新增测试：短文本 & 长文本 的生成时间，以及错别字
>
> 显卡型号：RTX 2060

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/whisper-shorttext.png)

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/whisper-longtext.png)