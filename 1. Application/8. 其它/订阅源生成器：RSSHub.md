# 订阅源生成器：RSSHub
![](/media/202303/2023-03-10_144122_5681660.7493394231495037.png)
> 项目地址：https://github.com/DIYgod/RSSHub

## 简介
RSSHub 是一个开源、简单易用、易于扩展的 RSS 生成器，可以给任何奇奇怪怪的内容生成 RSS 订阅源。RSSHub 借助于开源社区的力量快速发展中，目前已适配数百家网站的上千项内容。

可以配合浏览器扩展 RSSHub Radar 和 移动端辅助 App RSSBud (iOS) 与 RSSAid (Android) 食用。

支持非常多的订阅，如：BiliBili、知乎、微博、微博绿洲、小红书、豆瓣、简书、大众点评等，对国内媒体软件的友好度还是很高的。

我最常用的是订阅：微博、小红书、豆瓣，不用打开专门的APP就能看到关注博主的消息，不用接受其它的信息流，够专注，对我来说还是挺好用的。

## 部署

### docker部署
```sh
docker pull diygod/rsshub
docker run -d --name rsshub -p 1200:1200 diygod/rsshub
curl 127.0.0.1:1200 -I

# 订阅微博号
http://127.0.0.1:1200/weibo/user/{userid}
```
### docker-compose 部署
```yml
version: '2.9.0'
services:
  rsshub:
    image: diygod/rsshub:latest
    network_mode: "bridge"
    container_name: rsshub
    pid: "host"
    restart: always
    ports:
      - "61200:1200"
    deploy:
      resources:
        limits:
          memory: 256M
          cpus: "0.1"
```
部署成功后访问 61200 端口，即可看到服务端。

## 使用说明

> https://docs.rsshub.app/

服务端部署完成后，我们只需在客户端添加订阅地址即可

在 Windows 平台我使用的客户端是：irreader。

添加地址：服务器地址+1200端口+参数。

例如要订阅微博的博主，就可以填入：`/weibo/user/{userid}` 即可