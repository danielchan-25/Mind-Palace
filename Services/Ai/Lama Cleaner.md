# Lama Cleaner

一个由 SOTA AI 模型驱动的免费开源修图工具。这个工具可以本地运行，帮助你擦除图片中你不想要的内容，移除背景、面部修复等工作。

> https://github.com/Sanster/lama-cleaner

## 安装

1. 创建 Python 环境（个人喜欢将各个项目的环境隔离而已，不创建也行）

   ```sh
   conda create -n lama_cleaner python==3.10.6
   ```

2. 程序部署

   ```sh
   # 有GPU的使用以下这行，无的话可以忽略
   pip install torch==1.13.1+cu117 torchvision==0.14.1 --extra-index-url https://download.pytorch.org/whl/cu117
   
   pip install lama-cleaner
   ```

## 使用

直接使用命令行启动，访问 `http://IP:8080` 进入网页端

```sh
lama-cleaner --model=lama --device=cuda --host=0.0.0.0 --port=8080

# 有GPU的使用--device=cuda，无GPU的使用--device=cpu
# 加上--host=0.0.0.0参数，局域网内任何主机允许访问
# 更多使用参数请使用 -h 查看
```

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/lama_cleaner-1.png)

## 测试

简单测试了一下 `lama` 模型，使用了来自百度图片中的广州地铁，尝试将其中的部分抹去，以下是前后对比图：

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/lama_cleaner-2.png)

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/lama_cleaner-3.png)

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/lama_cleaner-4.png)
