# LaWGPT
> 项目地址：https://github.com/pengxiao-song/LaWGPT

## 环境
经测试，无 GPU 机器也能使用 CPU 运行，速度感人

## 部署
```sh
# 下载代码
git clone git@github.com:pengxiao-song/LaWGPT.git
cd LaWGPT
```

```sh
# 创建环境
conda create -n lawgpt python=3.10 -y
conda activate lawgpt
pip install -r requirements.txt
```

启动 web ui
```sh
bash scripts/webui.sh
# 访问： http://127.0.0.1:7860
```
