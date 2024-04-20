---
title: "文档系统：MrDoc"
date: 2023-12-05

---

# 文档系统：MrDoc

> 官网: [MrDoc](https://www.mrdoc.pro/)
> 
> GitHub: [MrDoc](https://github.com/zmister2016/MrDoc)
> 
> Demo: [MrDoc](https://doc.mrdoc.pro/)


## 简介
MrDoc 是基于 Python 开发的在线文档系统，适合作为个人和小型团队的私有云文档、云笔记和知识管理工具。致力于成为优秀的私有化在线文档部署方案。

MrDoc 拥有 8 大特点，分别是：

书写便捷、沉浸阅读、权限管控、导入导出、多端扩展、管理强大、私有部署和持续更新。

我最喜欢的是私有部署，将所有的文档都存放在本地的服务器上，就算存一些密码之类的也不用担心会被有心人盗用。

## 部署
### docker部署
```shell
docker run \
--name mrdoc \
-p 10086:10086 \
-d jonnyan404/mrdoc-nginx
```
挂载本地目录安装

1 创建文件夹

`mkdir -p ~/mrdoc/media`

2 运行容器
```shell
docker run --name mrdoc \
-p 10086:10086 \
-v ~/mrdoc:/app/MrDoc/config \
-v ~/mrdoc/media:/app/MrDoc/media \
-d jonnyan404/mrdoc-nginx
# nginx版本,更换mrdoc-alpine为mrdoc-nginx即可
```

3 自定义端口
```shell
docker run --name mrdoc \
-e LISTEN_PORT=port -p xxx:port \
-v ~/mrdoc:/app/MrDoc/config \
-v ~/mrdoc/media:/app/MrDoc/media \
-d jonnyan404/mrdoc-alpine
### nginx版本,更换mrdoc-alpine为mrdoc-nginx即可
```

其中：

- xxx为宿主机端口

- port为容器端口

自行替换 `xxx` 与 `port` 即可。

查看密码
```shell
docker logs mrdoc 2>&1 | grep pwd
```

### docker-compose部署
```yml
version: '2.9.0'
services:
  mrdoc:
    image: jonnyan404/mrdoc-nginx
    container_name: mrdoc
    network_mode: bridge
    restart: always
    ports:
      - "61086:10086"
    volumes:
      - "/data/docker-data/mrdoc:/app/MrDoc/config"
      - "/data/docker-data/mrdoc/media:/app/MrDoc/media"
```
## 备份
### 手动备份
```shell
# 先备份
docker cp mrdoc:/app/MrDoc/config /tmp/config
docker cp mrdoc:/app/MrDoc/media /tmp/media
# 再还原
docker cp /tmp/config mrdoc:/app/MrDoc
docker cp /tmp/media mrdoc:/app/MrDoc
# 重启
docker restart mrdoc
```

### 编写脚本自动备份

`00 03 * * 1 /bin/bash /data/scripts/mrdoc_scripts.sh`

```shell
#!/bin/sh
BACKUP_FILE=/data/backup
DAY=`date +%Y-%m-%d`
TIME=`date +%Y-%m-%d-%H-%M-%S`
mkdir -p /data/backup/mrdoc/${DAY}
docker cp mrdoc:/app/MrDoc/config /data/backup/mrdoc/${DAY}/config
docker cp mrdoc:/app/MrDoc/media /data/backup/mrdoc/${DAY}/media
```

---
> [Nginx反向代理](https://doc.mrdoc.pro/doc/44910/)
