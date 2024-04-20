---
title: "FFmpeg"

date: 2021-05-11

---

# 简介

FFmpeg 安装后有三个命令：`ffmpeg` `ffplay` `ffprobe`

- ffmpeg：一般用于视频、音频的处理
- ffplay：一般用于播放视频、音频
- ffprobe：一般用于查看视频、音频的信息

## 帧率

帧率(frames per second, fps)是每秒画面刷新的次数，帧率越高视频越流畅。
一般来说 30fps 就是可以接受的，60fps 则可以明显提升交互感和逼真感。
但是一般超过 75fps 一般就不容易察觉到有明显的流畅度提升了。

## 分辨率

分辨率表示画面的精细程度，通常用像素密度来表示，常用的单位为 ppi (像素每英寸)。
通常像素密度越高画面越精细，模糊程度越低。
我们通常用视频的像素数来表示它的分辨率如：1080x640, 640x320 等。

# 安装

```shell
# MacOS
brew install ffmpeg
```

## 编译安装

以 Linux 为例：

1. 环境安装

```shell
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum -y install yasm yasm-devel
```

2. 下载源码包

```shell
wget http://ffmpeg.org/releases/ffmpeg-4.4.tar.gz
tar -xvf ffmpeg-4.4.tar.gz
cd ffmpeg-4.4
```

3. 编译安装

```shell
./configure --enable-shared --prefix=/usr/local/ffmpeg --enable-openssl
make && make install
```

4. 添加环境变量

```shell
echo 'export PATH:$PATH:/usr/local/ffmpeg/bin' >> /etc/profile
source /etc/profile
echo '/usr/local/ffmpeg/lib' > /etc/ld.so.conf.d/ffmpeg.conf
ldconfig
ffmpeg -version
```

# 使用

## 参数说明

- `scale` 

  - 用于缩放视频，`in_w` 和 `in_h` 代表输入的宽和高

  - ```shell
    ffmpeg -y -i video.mp4 -vf "scale=2*in_w:2*in_h" output.mp4
    ```



- `overlay` 滤镜将一个视频叠放在另一个视频上，可用于在视频中添加水印和动画等操作。
  - `overlay` 的第一个输入为底层视频流，第二个输入为叠加视频流。
  - `main_w` 和 `main_h` 为底层视频的宽和高
  - `overlay_w` 和 `overlay_h` 为叠加视频的宽和高

## ffmpeg

```shell
ffmpeg 语法格式：
ffmpeg \
  [global_options] \
  [input_file_options] -i input_url \
  [actions] \
  [output_file_options] output_url
```

| 常用功能   | 说明                                   | 命令                                                         |
| ---------- | -------------------------------------- | ------------------------------------------------------------ |
| 格式转换   | 不仅能视频格式互转，还能转换为音频格式 | ffmpeg -i input.mp4 output.mov<br/>ffmpeg -i input.mp4 output.ts<br />ffmpeg -i video.mp4 -vn music.mp3 |
| 修改分辨率 | scale=x:-1表示保持原始的宽高比         | ffmpeg -i input.mp4 -vf scale=960:540 output.mp4<br />ffmpeg -i input.mp4 -vf scale=960:-1 output.mp4 |
| 推流       | n=-1，一直重复                         | ffmpeg -re -stream_loop {n} -i video.mp4 -codec copy -f flv 'rtmp://server/live/streamName' |
| 拉流       |                                        | ffmpeg -i udp://192.168.0.123:6666 output.mp4                |
| 下载       |                                        | ffmpeg -i <m3u8-path> -c copy OUTPUT.mp4                     |
|            |                                        |                                                              |

视频剪切

```shell
# 下面的命令，可以从时间为00:00:15开始，截取5秒钟的视频。
# -ss表示开始切割的时间，-t表示要切多少。上面就是从15秒开始，切5秒钟出来。
ffmpeg -ss 00:00:15 -t 00:00:05 -i input.mp4 -vcodec copy -acodec copy output.mp4
```

视频压缩

```shell
ffmpeg -i video.mp4 -c:v libx265 -x265-params crf=18 video1.mp4
ffmpeg -i video.flv -vcodec h264 -acodec mp2 video1.mp4
```

添加水印

```shell
# 在视频的左上角添加水印
ffmpeg -i input.mp4 -i iQIYI_logo.png -filter_complex overlay output.mp4
# 右上角
ffmpeg -i input.mp4 -i iQIYI_logo.png -filter_complex overlay=W-w output.mp4
# 左下角：
ffmpeg -i input.mp4 -i iQIYI_logo.png -filter_complex overlay=0:H-h output.mp4
# 右下角：
ffmpeg -i input.mp4 -i iQIYI_logo.png -filter_complex overlay=W-w:H-h output.mp4
```

去除水印

```shell
# 语法：-vf delogo=x:y:w:h[:t[:show]]
# x:y 离左上角的坐标
# w:h logo的宽和高
# show：若设置为1有一个绿色的矩形，默认值0

ffmpeg -i input.mp4 -vf delogo=1:1:220:90:0 output.mp4
```

视频拼接

```shell
# 先转换为 ts 格式
ffmpeg -i 1.mp4 1.ts
ffmpeg -i 2.mp4 2.ts

# 合并 ts 视频，输出为 mp4
ffmpeg -i "concat:1.ts|2.ts" -c copy output.mp4
```

图片合并为视频

```shell
ffmpeg -i img%3d.png output.gif
ffmpeg -i img%3d.png output.mp4
```

生成视频

```shell
# 生成纯色测试视频
ffmpeg -re -f lavfi -i color=c=red@0.2:s=vga:r=25 -vcodec libx264 -r:v 25 out_color.mp4

# 生成随机雪花样式测试视频
ffmpeg -re -f lavfi -i "nullsrc=s=1024x768,geq=random(1)*1024:384:384" -vcodec libx264 -r:v 25 out_snow.mp4
```
- `-re`: 表示按输入视频帧率读取
- `-f`：指定输出格式，生成测试视频使用lavfi
- `-i`:  指定输入的内容，本例中生成纯色测试视频，通过color滤镜指定；生成随机雪花样式通过nullsrc指定
- `s/size`: 表示分辨率大小，可以为vga或wxh（1024x768）两种形式
- `c`: 表示颜色，本例中为red(红色)
- `geq`：表示随机数生成的标签，random为随机数生成函数   
- `-vcodec`: 指定视频编码库，本例中为libx264
- `-r:v`：设置视频的帧率，本例中为25

## ffplay

| 功能 | 说明                                  | 命令                         |
| ---- | ------------------------------------- | ---------------------------- |
|      | -showmode参数：0:无 1:波形图 2:频谱图 | ffplay music.mp3 / video.mp4 |
|      |                                       |                              |
|      |                                       |                              |



## ffprobe

参考文献

> **https://www.cnblogs.com/frost-yen/p/5848781.html**