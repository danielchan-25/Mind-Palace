# 前言

由于家里的服务器存储了一些视频、电影，所以搭建了一个媒体服务器：Jellyfin

# 简介

Jellyfin 是一款自由开源的媒体中心软件，类似于 Plex 和 Emby。它是针对家庭用户设计的媒体中心，可以帮助你在多种设备上管理和播放你的媒体内容，如电影、电视节目、照片和音乐等。Jellyfin 可以在多个操作系统平台上运行，如 Windows、Linux、macOS 和 FreeBSD，并且支持了所有主流的设备平台，例如 Web、Android、iOS、Apple TV、Android TV 和 Kodi 等。Jellyfin 功能丰富，用户界面友好，可以作为家庭媒体的主要中心，同时也可以用来分享自己的媒体内容给家庭成员或者朋友。它还支持客制化插件，可以根据用户的需要添加各种功能。

# 部署

我使用的是 docker-compose 的方式部署，先创建一个 `jellyfin.yml` 文件，将以下内容添加进去

（注意修改路径）

```yml
version: "3"
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    restart: always
    volumes:
      - /data/docker-data/jellyfin/media/folder:/media
      - /data/docker-data/jellyfin/config/folder:/config
      - /data/docker-data/jellyfin/cache/folder:/cache
    ports:
      - "8096:8096"
      - "8920:8920"
    environment:
      - TZ=Asia/Shanghai
```

拉取镜像并启动容器：

```sh
docker pull jellyfin/jellyfin
docker-compose -f jellyfin.yml up -d
```

开放 8096 端口

```sh
iptables -I INPUT -p tcp --dport 8096 -j ACCEPT
```

# 使用

将本地的视频存放在： `media/folder` 中，然后访问 `http://localhost:8096` 进入 Web 后台，创建完用户后进入控制台，点击”扫描所有媒体库“即可查看到。
