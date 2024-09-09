# 简介
Transmission 是一个免费的开源 bt 客户端，适用于Windows, macOS, Linux和FreeBSD。

传输是 BitTorrent 用户的热门选择，因为它快速，可靠，易于使用。由于它支持加密，它也是最安全的bt客户端之一。

传输对于任何想要使用 BitTorrent 下载文件的人来说都是一个很好的选择。它快速、可靠、安全、易于使用。

以下是 Transmission 的一些特点:

- 用户友好的界面:传输有一个干净和易于使用的界面，使它简单的下载和管理种子。

- 带宽优先级:传输时，您可以为特定的种子设置带宽优先级，以确保优先下载最重要的种子。

- RSS订阅:传输支持RSS订阅，所以当你最喜欢的节目的新剧集发布时，你可以自动下载种子。

- 远程访问:传输可以从任何web浏览器远程访问，所以你可以从任何地方管理你的种子。

- 加密:传输支持加密，所以你的种子是保护免受窥探的眼睛。

- 传输对于任何想要使用BitTorrent下载文件的人来说都是一个很好的选择。它快速、可靠、安全、易于使用。

# 部署
## docker 部署
```shell
docker pull transmission
```
```shell
docker run -d -p 9091:9091 transmission
```
## docker-compose 部署

```yml
version: '3'

services:
  transmission:
    image: transmission
    container_name: transmission
    ports:
      - 9091:9091
    volumes:
      - /path/to/download/directory:/downloads
    restart: unless-stopped
```
```shell
docker-compose up -d
```
## 使用

