# Vicuna-7B 本地部署

> 模型地址：https://huggingface.co/lmsys/vicuna-7b-v1.3
> 
> 框架地址：https://github.com/vllm-project/vllm
> 
> 项目地址：https://github.com/lm-sys/FastChat#vicuna-weights

## vllm

### pip 安装

```shell
# (Optional) Create a new conda environment.
conda create -n myenv python=3.8 -y
conda activate myenv

# Install vLLM.
pip install vllm  # This may take 5-10 minutes.
```

### 源码安装

```shell
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .  # This may take 5-10 minutes.
```

## 模型下载

可以用 浏览器/迅雷 下载模型文件（最大的那几个），其它的直接用 `Git` 下载

```shell
# apt install git-lfs

git lfs install
git clone https://huggingface.co/lmsys/vicuna-7b-v1.3
```

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/vicuna-1.png)


注意 `tokenizer.json` 文件的大小，经常下载不全导致出现奇奇怪怪的问题

## Vicuna 环境安装
### 源码
```shell
git clone https://github.com/lm-sys/FastChat.git
cd FastChat
pip install -e .
```

## 模型启动
### 命令行方式
```shell
python -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.3
```
### webUI 方式

打开三个终端窗口，也可以选择后台运行

1. 启动控制器
```shell
python -m fastchat.serve.controller
```

2. 启动模型工作器
```shell
CUDA_VISIBLE_DEVICES=3,4 python -m fastchat.serve.model_worker --model-path ./vicuna-7b-v1.3 --num-gpu 2
```

3. 为确保您的模型工作器与控制器正确连接，请使用以下命令发送测试消息，您将看到一个简短的输出
```shell
python -m fastchat.serve.test_message --model-name vicuna-7b-v1.3
```

4. 启动 `Gradio Web` 交互界面
```shell
python -m fastchat.serve.gradio_web_server --host 0.0.0.0 --port 8700 --share
```

5. 网页访问：`localhost:7860`，在输入栏中提问即可。

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/vicuna-2.png)
