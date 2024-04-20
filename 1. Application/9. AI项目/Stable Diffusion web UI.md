---
title: "Stable Diffusion web UI"
date: 2024-01-22

---

# 介绍
Stable Diffusion 也是 Ai 画图的一种，已在 GitHub 上开源，所以可以本地部署。
本地部署有没有生成图片数量限制，不用花钱，不用排队，自由度高等一堆优点。
由于在查阅资料过程中，发现一个叫：Stable Diffusion web UI 的项目，是在 Stable Diffusion 的项目上封装，且带有 UI 界面，部署难度大大降低，所以使用这个。

> Github: [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

# 部署

## 准备工作
电脑/服务器一台，需要有以下配置：

- GPU显卡，最低配置4GB显存，没显卡的可以使用CPU跑（网上说可以，但我没实际测试）

- 物理内存最好16GB起步，总之显存内存越大越好。

我的服务器配置为：NVIDIA GeForce RTX2080 Ti，物理内存：128GB，这个配置估计没问题。

## 环境安装

我的服务器系统为：Ubuntu 18.04，为不影响我的本地环境，所以打算安装在 Docker 环境中。

### Docker 安装 CentOS
```shell
# 拉取 CentOS7 镜像
docker pull centos:centos7.9.2009

# 部署 CentOS7
## 使用 --gpus all 参数，让容器也能使用GPU显卡
docker run -it --name stable-diffusion-webui --gpus all -d centos:centos7.9.2009

# 进入 CentOS
docker exec -it stable-diffusion-webui bash
```

**！！！！！有个非常重要的点！！！！！**

**stable-diffusion-webui 是不允许使用 Root 用户运行的！为避免后期各种问题！**

**建议新建用户部署！**

**建议新建用户部署！**

**建议新建用户部署！**

```shell
# 我创建了一个叫 qq 的用户部署
useradd qq
```

### 安装 Python
stable-diffusion-webui 是使用 Python3.10.6 的开发环境，

这里因个人习惯，所以使用 miniconda，下载地址：Miniconda - conda documentation

直接安装 Python 3.10.6 也一样，可以直接跳过这部分。
```shell
sh Miniconda3-latest-Linux-x86_64.sh
安装完毕后，执行以下命令，出现版本信息即可。
[qq@cc757762d81f /]$ conda -V
conda 23.1.0
```
还要配置 conda 库包的源地址，清除缓存。
```shell
conda config --set show_channel_urls yes

# 执行完后，修改 /home/qq/.condarc 文件为以下内容
channels:
 - defaults
show_channel_urls: true
default_channels:
 - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
 - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
 - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
 conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
 msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
 bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
 menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
 pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
 pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
 simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

# 清除缓存
conda clean -i
```

创建 conda 环境并激活进入。

```shell
conda create --name stable-diffusion-webui python=3.10.6

conda activate stable-diffusion-webui
```

升级 pip，修改镜像源地址。

```shell
python -m pip install --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 安装 Cuda
只需要知道它是显卡跑算法的程序，必须安装即可。

> [cuda-toolkit-archive](http://developer.nvidia.com/cuda-toolkit-archive)

根据 cuda 版本安装，cuda版本可以使用 nvidia-smi 查看，就在右上角的位置。

## 下载项目文件

### 源码
`stable-diffusion-webui` 的源码
```shell
yum install -y git

# 请记得 git clone 下本地的路径，后续需要存放模型等文件
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

### 官方模型

> 下载地址：

> 1.4版本：[v1.4](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/tree/main)

> 1.5版本：[v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5)

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/stablediffusionwebui-1.png)

下载完成后，存放在 `stable-diffusion-webui/models` 下。

### GFPGAN

腾讯的开源项目，用于修复和绘制人脸，下载 V1.4 model 即可。
存放在 `stable-diffusion-webui/` 下。
> Github: [GFPGAN](https://github.com/TencentARC/GFPGAN)

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/stablediffusionwebui-2.png)

环境已全部准备完毕，可以启动程序。

## 测试
运行程序肯定会出现报错信息的，多半是网络环境的问题

```shell
# 首先进入到 stable-diffusion-webui 目录，先执行这个脚本测试一下
./webui.sh
```

报错信息

```shell
Cannot locate TCMalloc (improves CPU memory usage)
Python 3.10.6 (main, Oct 24 2022, 16:07:47) [GCC 11.2.0]
Version: v1.2.1
Commit hash: 89f9faa63388756314e8a1d96cf86bf5e0663045
Installing gfpgan
Traceback (most recent call last):
  File "/home/painer/stable-diffusion-webui/launch.py", line 369, in <module>
    prepare_environment()

```

是由于网络环境的问题，有两种办法解决：

1. 编辑 `launch.py` 文件
   1. 找到 `gfpgan_package = os.environ.get` 这行
   2. 将后面的 URL 修改为：`git+https://ghproxy.com/https://github.com/********`
2. 手动下载 `gfpgan` 文件，然后手动安装部署：[GFPGAN](https://github.com/TencentARC/GFPGAN)
   1. 将安装包放置：`stable-diffusion-webui/venv/scripts`(手动创建)
   2. 安装：`python -m pip install basicsr facexlib`
   3. `python -m pip install -r requirements.txt`
   4. `python setup.py develop`
3. 继续执行 `python launch.py`，如遇其它问题按同理解决


# 启动程序

```shell
# 使用自定义端口启动
python launch.py --port 7861

# 局域网内共享
python launch.py --share --listen

# 开启 API 模式
## API地址：127.0.0.1:7861/docs
python launch.py --nowebui
```

启动时能选择增加更多参数，参数见文章底部 [参考文档]

# 安装扩展

在 Stable Diffusion web UI 中，扩展在以下图中添加：

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/stablediffusionwebui-3.png)

但因国内网络环境问题，经常无法加载，那就可以使用其它操作。

如可以先打开复制图中的 URL 地址中的内容，然后放在一个正常的网络环境，如搭建一台 Web 服务器等操作之类的，然后就可以将该 URL 替换了。

## 安装中文
> [中文插件](https://github.com/dtlnor/stable-diffusion-webui-localization-zh_CN)

可以先下载该项目，然后放进服务器中的：`/home/painer/stable-diffusion-webui/extensions` 目录中，然后再按说明加载扩展即可。

# 使用说明
## 常用参数
`Clip Skip`
- early stopping parameter for CLIP model，1是保持不变，最后一层才停止。
如何设置：[Setting]-->[stable diffusion]-->[clip skip]

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/stablediffusionwebui-4.png)

`ENSD`
- 全称是：`Eta noise seed delta`，
![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/stablediffusionwebui-5.png)

## 命令行生成图像
```shell
python scripts/txt2img.py --prompt "a close-up portrait of a cat by pablo picasso, vivid, abstract art, colorful, vibrant" --plms --n_iter 5 --n_samples 1

生成成功后，图像存放在 `outputs/
```

# 导入 Lora
> [civitai](https://civitai.com/)

下载完成后，导入到：`stable-diffusion-webui/models/Lora` 目录


---
参考文档

> [安装gfpgan](https://blog.csdn.net/weixin_40735291/article/details/129153398)

> [Prompts](https://www.bilibili.com/video/BV12X4y1r7QB)

> [启动参数](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings)

> [启动参数](https://profaneservitor.github.io/sdwui-docs/cn/cli/)

> [启动参数](https://blog.csdn.net/watson2017/article/details/129285656)
