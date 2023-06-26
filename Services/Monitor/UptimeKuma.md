# UptimeKuma

![](/media/202303/2023-03-10_144826_2459370.6542228258808808.png)
> 项目地址：https://github.com/louislam/uptime-kuma

## 简介
Uptime Kuma 是一个开源的监控工具，功能类似于 Uptime Robot。相较于其它同类工具，Uptime Kuma 支持自托管服务，并且限制更少。

## 部署
### docker部署
1. 先在本地创建文件夹

```sh
mkdir -p /opt/uptime-kuma/data
```

2. 运行命令

```sh
docker run \
--restart=always \
-p 3001:3001 \
-v /opt/uptime-kuma/data:/app/data \
--name uptime-kuma \
-d louislam/uptime-kuma
```

3. 访问 Web 端： `http://IP:3001`

4. admin密码重置：`docker exec -it <container name> npm run reset-password`

### docker-compose部署
```yml
version: '2.9.0'
services:
  uptimekuma:
    image: louislam/uptime-kuma
    restart: always
    container_name: uptimekuma
    network_mode: "bridge"
    volumes:
      - "/data/docker-data/uptimekuma/data:/app/data"
    ports:
      - "63001:3001"
```

## 使用说明

这里介绍两种最常用也是最简单的监控类型，URL & TCP Port

### 监控

#### URL 监控

进入页面后，我们可以在左上角添加需要监控的服务，例如：MrDoc文档系统。

已知 MrDoc 是通过 `http://IP:10086` 的方式访问，那么就可以监听 `http://IP:10086` 这个URL。

在左上角「添加监控项」，输入 URL 的地址即可，点击最下方的保存测试，显示成功即可。
![](/media/202303/2023-03-10_144922_6924640.558220541312339.png)

#### TCP Port 监控

部署了 MySQL 服务，但 MySQL 是没有网页 URL 地址的，只能通过服务器端口号监听，所以可以选择 TCP Port 监控。

「监控类型」选择 TCP Port，填入主机名与端口号，点击保存，显示成功即可。
![](/media/202303/2023-03-10_144939_4148180.42146450591476603.png)

### 通知
监控搭建完成了，但怎么通知我呢？

一样很简单，右上角的「设置」里找到「通知」，即可选择通知类型，支持钉钉企业微信邮箱等一系列的APP。

我选择的是：钉钉机器人，填入 Webhook 地址跟加签密钥即可。（记得点击测试查看是否正常）

![](/media/202303/2023-03-10_145005_9502700.7980195551692946.png)
