# 简介
Aria2 是一个多平台轻量级，支持 HTTP、FTP、BitTorrent 等多协议、多来源的命令行下载工具。Aria2 可以从多个来源、多个协议下载资源，最大的程度上利用了你的带宽。

很多人在 Windows 可能用过 Internet Download Manager，是很好用的多线程下载工具。Aria2 跟 IDM 类似，不仅可以多线程下载，还可以通过多来源进行下载，简单地说就是从多个镜像服务器同时下载一个文件，Aria2 还支持 BT 协议，弥补了 IDM 只支持 HTTP 和 FTP 的痛点。

# 部署

## docker部署
```shell
docker run -d \
--name aria2 \
--restart unless-stopped \
--log-opt max-size=1m \
-e PUID=$UID \
-e PGID=$GID \
-e UMASK_SET=022 \
-e RPC_SECRET=123456 \
-e RPC_PORT=6800 \
-e LISTEN_PORT=6888 \
-p 6800:6800 \
-p 6888:6888 \
-p 6888:6888/udp \
-v $PWD/aria2/config:/config \
-v $PWD/Downloads:/downloads \
p3terx/aria2-pro
```

## docker-compose部署
```yml
version: '2.9.0'
services:
  aria2:
    image: p3terx/aria2-pro
    container_name: aria2
    network_mode: bridge
    restart: always
    environment:
      - PUID = 65534
      - PGID = 65534
      - UMASK_SET=022
      - RPC_PORT=6800
      - RPC_SECRET=123456
      - LISTEN_PORT=6888
      - TZ=Asia/Shanghai
      - IPV6_MODE=false
      - DISK_CACHE=64M
      - UPDATE_TRACKERS=true
    volumes:
      - "/data/docker-data/aria2:/downloads"
      - "/data/docker-data/aria2/config:/config"
    ports:
      - "6800:6800"
      - "6888:6888"
      - "6888:6888/udp"
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: "0.5"
```

# 客户端部署
部署完成后，应该怎么下载呢？总不能一直用命令行下载吧，这里推荐一个网页端工具：**AriaNG GUI**，非常好用。

> 项目地址：https://github.com/Xmader/aria-ng-gui

将以上的文件下载并存放在 `Nginx/Apache` 服务器的 `html/`页面中，然后访问该页面即可。
