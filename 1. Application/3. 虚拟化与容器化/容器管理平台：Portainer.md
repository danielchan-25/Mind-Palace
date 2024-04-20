---
title: "容器管理平台：Portainer"
date: 2024-02-12

---

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Portainer-1.png)

## 简介
Portainer是一个轻量级的容器管理平台，为用户提供了一个简单易用的Web界面来管理Docker环境。

Portainer的用户界面直观友好，支持多种容器编排技术，例如Docker Compose、Kubernetes、Swarm等。

Portainer还提供了丰富的图形化操作和监控功能，使得用户可以轻松地管理和监控自己的Docker容器。

同时，Portainer还支持多用户和权限控制，可以帮助企业管理多个Docker环境和团队。

总之，Portainer是一个非常实用和便捷的容器管理工具，能够大大简化用户对Docker环境的管理和操作，提高工作效率。

## 部署
## docker部署

1. 终端中输入以下命令拉取Portainer镜像：
```shell
docker pull portainer/portainer-ce
```

2. 运行以下命令启动Portainer容器：

```shell
docker run -d -p 9000:9000 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v portainer_data:/data \
--restart always \
--name portainer_container \
portainer/portainer-ce

# -d 表示在后台运行容器
# -p 表示将主机的9000端口映射到容器的9000端口
# -v 表示将主机的/var/run/docker.sock文件挂载到容器中
# --restart always 表示容器在退出后总是重新启动
# --name 表示为容器指定一个名称
# portainer/portainer-ce 是从Docker Hub上下载的Portainer镜像。
```

### docker-compose部署
```yml
version: '2.9.0'
services:
  portainer:
    image: portainer/portainer-ce
    restart: always
    container_name: portainer
    network_mode: 'bridge'
    ports:
      - "0.0.0.0:61010:9000"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: "0.5"
```

## 使用说明
启动后，可以通过在Web浏览器中输入 `http://IP:9000` 访问Portainer。

### 管理Docker容器和镜像

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Portainer-2.png)

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Portainer-3.png)

Portainer可以帮助用户管理Docker容器和镜像，例如创建、启动、停止、删除容器，以及拉取、删除、构建、推送镜像等操作。

此外，Portainer还提供了用于搜索和过滤容器和镜像的功能，以便用户更轻松地找到所需的资源。

### 使用Docker Compose管理多个容器

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Portainer-4.png)

Portainer还支持使用Docker Compose管理多个容器，用户可以上传Docker Compose文件，创建、更新、删除堆栈，以及查看堆栈中的服务和容器。

以上这些都是我使用 Docker Compose 启动的容器，方便管理。

### 监控Docker环境

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Portainer-5.png)

Portainer提供了用于监控Docker环境的各种指标的功能，

例如CPU、内存、网络、磁盘等指标的图表，以及容器和镜像的日志。

这些指标可以帮助用户了解Docker环境的运行情况，及时发现和解决问题。

### 管理用户和团队

Portainer支持管理用户和团队，用户可以创建新用户和团队，授权用户和团队访问特定的Docker环境和资源。这些功能可以帮助团队协作，保证环境的安全和可控性。
