# FFmpeg

# 1. 简介

FFmpeg 安装后有三个命令：`ffmpeg` `ffplay` `ffprobe`

- ffmpeg：一般用于视频、音频的处理
- ffplay：一般用于播放视频、音频
- ffprobe：一般用于查看视频、音频的信息


## 1.1 基本概念
 ## 1.2 帧率

  帧率(frames per second, fps)是每秒画面刷新的次数，帧率越高视频越流畅。
  一般来说 30fps 就是可以接受的，60fps 则可以明显提升交互感和逼真感。
  但是一般超过 75fps 一般就不容易察觉到有明显的流畅度提升了。

## 1.3 分辨率

  分辨率表示画面的精细程度，通常用像素密度来表示，常用的单位为 ppi (像素每英寸)。
  通常像素密度越高画面越精细，模糊程度越低。
  我们通常用视频的像素数来表示它的分辨率如：1080x640, 640x320 等。

# 2. 安装

  ```shell
  # MacOS
  brew install ffmpeg
  ```

  ```shell
  # Linux
  curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
  curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
  yum -y install yasm yasm-devel
  wget http://ffmpeg.org/releases/ffmpeg-4.4.tar.gz
  tar -xvf ffmpeg-4.4.tar.gz
  cd ffmpeg-4.4
  ./configure --enable-shared --prefix=/usr/local/ffmpeg --enable-openssl
  make && make install
  echo 'export PATH:$PATH:/usr/local/ffmpeg/bin' >> /etc/profile
  source /etc/profile
  echo '/usr/local/ffmpeg/lib' > /etc/ld.so.conf.d/ffmpeg.conf
  ldconfig
  ffmpeg -version
  ```

  # 3. 语法命令

  ## 3.1 ffmpeg

  ```shell
  ffmpeg 语法格式：
  ffmpeg \
    [global_options] \
    [input_file_options] -i input_url \
    [actions] \
    [output_file_options] output_url
  ```

  ## 3.2 scale

  `scale` 滤镜用于缩放视频，`in_w` 和 `in_h` 代表输入的宽和高

  ```shell
  ffmpeg -y -i video.mp4 -vf "scale=2*in_w:2*in_h" output.mp4
  ```

  ## 3.3 overlay

  `overlay` 滤镜将一个视频叠放在另一个视频上，可用于在视频中添加水印和动画等操作。
  `overlay` 的第一个输入为底层视频流，第二个输入为叠加视频流。
  `main_w` 和 `main_h` 为底层视频的宽和高
  `overlay_w` 和 `overlay_h` 为叠加视频的宽和高。

# 常用功能

## 视频处理

格式转换

```shell
ffmpeg -i input.mp4 output.mov
ffmpeg -i input.mp4 output.ts
```

提取音频

```shell
ffmpeg -i video.mp4 -vn music.mp3
```

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

分辨率修改

```shell
# 将输入的视频分辨率，缩小到 960x540 输出
ffmpeg -i input.mp4 -vf scale=960:540 output.mp4
# 如果写为：scale=960:-1，ffmpeg 会通知缩放滤镜再输出时保持原始的宽高比。
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

## 推/拉流

- 拉流
  - TCP：
  - UDP：`ffmpeg -i udp://192.168.0.123:6666 output.mp4`

- 推流

```shell
ffmpeg -re -i video.mp4 -codec copy -f flv 'rtmp://server/live/streamName'

# 循环推流
## n：次数
## -1：无限循环
ffmpeg -re -stream_loop {n} -i video.mp4 -codec copy -f flv 'rtmp://server/live/streamName'
```

## 播放音视频

```shell
ffplay music.mp4/music.mp3

# -showmode 0:无 1:波形图 2:频谱图
ffplay -showmode 0/1/2 music.mp3
```

### 拼接

#### 视频拼接

```shell
# 先转换为 ts 格式
ffmpeg -i 1.mp4 1.ts
ffmpeg -i 2.mp4 2.ts

# 合并 ts 视频，输出为 mp4
ffmpeg -i "concat:1.ts|2.ts" -c copy output.mp4
```

#### 图片合并为视频

```shell
ffmpeg -i img%3d.png output.gif
ffmpeg -i img%3d.png output.mp4
```

### 下载网页的视频音频流

```shell
# 语法：
# ffmpeg -i <m3u8-path> -c copy OUTPUT.mp4
# ffmpeg -i <m3u8-path> -vcodec copy -acodec copy OUTPUT.mp4
ffmpeg -i https://169.vgemv.com:48801/live/15012/index.m3u8 -c copy OUTPUT.mp4
```

### 生成视频
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

## 参考文献
> **https://www.cnblogs.com/frost-yen/p/5848781.html**
