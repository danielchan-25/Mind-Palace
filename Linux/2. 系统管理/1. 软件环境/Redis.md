# Redis

## 服务端安装

> 下载地址：https://redis.io/download/

### 编译安装

```shell
tar -xzvf redis-stable.tar.gz
cd redis-stable
make
make install
```

如果编译成功，您将在src目录中找到几个Redis二进制文件，包括：

- redis-server：Redis 服务器本身
- redis-cli是与 Redis 交互的命令行界面实用程序。

```shell
whereis redis-server	# 查看安装路径
```

### Docker 部署

```shell
docker pull redis
docker run --name my-redis-container -d redis
```

这将在 Docker 中创建一个名为 `my-redis-container` 的Redis容器并在后台运行。


现在，您可以使用Redis客户端连接到容器并开始使用Redis。运行以下命令以连接到Redis容器：

```shell
docker exec -it my-redis-container redis-cli
```

# 