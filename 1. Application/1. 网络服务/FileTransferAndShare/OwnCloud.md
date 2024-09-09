# OwnCloud

## 简介
OwnCloud 是一个基于云存储的文件同步和共享平台。你可以使用 Docker 容器来快速搭建自己的 OwnCloud 服务器，以便于自己管理文件和数据。

## 部署
### docker部署

你可以使用以下命令来下载 OwnCloud 镜像：
```bash
docker pull owncloud/server
```
这个命令将从 Docker Hub 上下载 OwnCloud 镜像。你可以使用 docker images 命令来检查下载的镜像是否已经准备好。

需要创建一个 OwnCloud 容器。你可以使用以下命令来创建一个容器：
```bash
docker run -d -p 8080:80 \
--name owncloud-server \
-v /path/to/owncloud:/var/www/html/data \
owncloud/server
```

部署完毕，这个命令将在后台运行一个名为 owncloud-server 的容器，并将 OwnCloud 的 Web 服务映射到本地的 8080 端口上。容器还将持久化 OwnCloud 的数据，存储在本地的 /path/to/owncloud 目录中。你可以根据自己的需求修改这些参数。


### docker-compose部署

需要创建一个名为 `docker-compose.yml` 的文件，用来定义和运行 OwnCloud 和 MySQL 两个容器。

```yml

version: '3'

services:
  owncloud:
    image: owncloud/server
    ports:
      - "8080:80"
    volumes:
      - /path/to/owncloud:/var/www/html/data
    depends_on:
      - db

  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw
      MYSQL_DATABASE: owncloud
      MYSQL_USER: owncloud
      MYSQL_PASSWORD: owncloud
    volumes:
      - /path/to/mysql:/var/lib/mysql
```

这个文件定义了两个服务：OwnCloud 和 MySQL。

- OwnCloud 服务使用 OwnCloud 镜像，将 Web 服务映射到本地的 8080 端口，并持久化 OwnCloud 的数据到本地的 /path/to/owncloud 目录中。

- MySQL 服务使用 MySQL 镜像，设置了一些环境变量来创建一个名为 owncloud 的数据库，并持久化 MySQL 的数据到本地的 /path/to/mysql 目录中。

### 使用说明

访问 OwnCloud：现在，你已经成功地创建了 OwnCloud 容器。你可以在浏览器中访问 http://localhost:8080 或者 http://your-server-ip:8080 来访问 OwnCloud。

配置 OwnCloud：当你第一次访问 OwnCloud 时，你将需要配置一些基本设置，例如用户名和密码、数据库设置等。按照 OwnCloud 的提示进行操作，完成配置后，你就可以开始使用 OwnCloud 了。
