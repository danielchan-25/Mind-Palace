# DragGAN

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/DragGAN-1.png)

> https://github.com/XingangPan/DragGAN

DragGAN 是由Max Planck研究所开发的一种新的人工智能工具，它允许用户通过几个点击和拖动来真实地修改照片。根据一篇研究文章，它提供了两个主要组成部分：基于特征的运动监督和一种革命性的点追踪技术。

DragGAN 允许用户交互地将图片中的点拖动到他们选择的目标位置。这种基于特征的运动监督使用户能够精确地移动处理点，完全控制图片修改过程。此外，点追踪技术确保在整个编辑过程中精确监测处理点。

## 部署

先创建一个 Python 环境

```sh
conda create --name=DragGAN python==3.10.6
conda activate DragGAN
```

下载项目

```sh
git clone https://github.com/XingangPan/DragGAN.git
cd DragGAN/
```

安装环境

```sh
pip install -r requirements.txt
```

下载预训练 StyleGAN2 的权重

```sh
python scripts/download_model.py
```

启动 GUI

```sh
python visualizer_drag_gradio.py
```

访问 http://127.0.0.1:7860 即可到达 GUI 界面

## 使用说明

在 `Pickle` 中选择模型，选好模型后在 `Latent` 中的 `Seed` 选择图片，然后在图片中选择需要拖动的目标位置，再次选择拖动的目的地，点击 `Start` 开始。

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Ai/img/DragGAN-2.gif)
