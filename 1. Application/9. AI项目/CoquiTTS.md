---
title: "Coqui TTS"
date: 2024-04-11

---

官网: [CoquiTTS](https://coqui.ai/)
Github: [CoquiTTS](https://github.com/coqui-ai/TTS)

# 简介
`Coqui TTS` **是一个用于高级文本到语音生成的库**。它建立在最新研究的基础上，旨在实现易于训练、速度和质量之间的最佳平衡。

`Coqui TTS` 带有预训练模型、用于测量数据集质量的工具，并且已经在 20 多种语言中用于产品和研究项目。

特征：

- 用于 Text2Speech 任务的高性能深度学习模型
- 快速高效的模型训练
- 终端和 Tensorboard 上的详细训练日志
- 支持多扬声器 TTS
- 高效、灵活、轻量级但具有完整的 Trainer API
- 能够将 PyTorch 模型转换为 Tensorflow 2.0 和 TFLite 以进行推理
- 已发布和可供阅读的模型
- 在 dataset_analysis 下管理 Text2Speech 数据集的工具
- 用于使用和测试模型的实用程序
- 模块化的代码库可以轻松实现新想法

# 使用

可以使用命令行执行：
```shell
tts --text "Hello, World" --out_path output/hello.mp3

# 同样也支持中文
tts --text '你好，世界！' --out_path output/hello.mp3 --model_name "tts_models/zh-CN/baker/tacotron2-DDC-GST"
```
