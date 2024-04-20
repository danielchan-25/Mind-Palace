---
title: "Docker-Compose"

date: 2024-01-21

---

> 参考文档：
> https://blog.csdn.net/weixin_43695104/article/details/121035401

# 简介

`Compose` 是用于定义和运行多容器 `Docker` 应用程序的工具。
通过 `Compose`，您可以使用 YML 文件来配置应用程序需要的所有服务。
然后，使用一个命令，就可以从 YML 文件配置中创建并启动所有服务。

`Compose` 使用的三个步骤：

- 使用 `Dockerfile` 定义应用程序的环境。
- 使用 `docker-compose.yml` 定义构成应用程序的服务，这样它们可以在隔离环境中一起运行。
- 最后，执行 `docker-compose up` 命令来启动并运行整个应用程序。

# 安装

Github: [Docker-compose](https://github.com/docker/compose/releases)

```shell
wget https://github.com/docker/compose/releases/download/v2.9.0/docker-compose-linux-x86_64
chmod +x docker-compose-linux-x86_64
ln -s /data/soft/docker-compose-linux-x86_64 /usr/bin/docker-compose
docker-compose --version
```

# 使用

```yml
version           # 指定 compose 文件的版本，必写
services          # 定义所有的 service 信息, 必写
   image         # 镜像名称或镜像ID。如果镜像在本地不存在，Compose 将会尝试拉取这个镜像。
   restart: always # 容器总是重新启动。
   container_name # 容器名
   volumes       # 挂载，可用于挂载配置文件，data等
   command       # 容器内执行什么命令
   ports         # 对外暴露的端口
   environment   # 添加环境变量
   network_mode  # 设置网络连接模式
   如：
   network_mode: "bridge"
   network_mode: "host"
   network_mode: "none"
   network_mode: "service:[service name]"
   network_mode: "container:[container name/id]"
```

# 常用命令

| 命令               | 解释                   |
| ------------------ | ---------------------- |
| build              | 生成或重建服务         |
| config             | 校验 compose 文件      |
| create             | 创建服务               |
| down               | 停止并删除服务         |
| events             | 实时接收容器事件       |
| exec               | 在执行的容器中运行命令 |
| images             | 查看所有镜像           |
| kill               | 结束运行容器           |
| logs               | 查看容器运行日志       |
| pause              | 暂停服务               |
| port               | 打印容器绑定的端口     |
| ps                 | 查看启动的容器         |
| pull               | 拉取服务               |
| push               | 上传服务               |
| start/stop/restart | 开始/停止/重启服务     |
| rm                 | 删除容器               |
| run                | 运行命令               |
| top                | 显示正在运行的进程     |

| 命令 | 解释              |
| ---- | ----------------- |
| -f   | 指定 compose 文件 |
| -    |                   |
|      |                   |
|      |                   |
|      |                   |
|      |                   |
|      |                   |
|      |                   |
|      |                   |

| 常用命令                            | 解释                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| docker-compose config -q            | 验证（docker-compose.yml）文件配置，当配置正确时，不输出任何内容，当文件配置错误，输出错误信息。 |
| docker-compose ps                   | 显示所有容器                                                 |
| docker-compose up -d                | 构建启动容器                                                 |
| docker-compose down                 | 删除当前容器（顺便清除数据）                                 |
| docker-compose logs service_name    | 查看指定service日志                                          |
| docker-compose logs -f service_name | 实时查看指定service日志                                      |
| docker-compose pause service_name   | 暂停指定服务（数据还在）                                     |
| docker-compose unpause server_name  | 恢复指定服务                                                 |
| docker-compose stop service_name    | 停止指定服务的容器                                           |
| docker-compose start service_name   | 启动指定服务的容器                                           |
| docker-compose restart service_name | 重启指定服务                                                 |
| docker-compose rm service_name      | 删除指定服务的容器（删除前需关闭此容器）                     |