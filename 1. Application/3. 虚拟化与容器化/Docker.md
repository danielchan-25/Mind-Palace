---
title: "Docker"
date: 2024-04-27

---

# 概念
Docker 的镜像（Image）和容器（Container）是两个关键概念：

- 定义：

	- 镜像（Image）：镜像是一个只读的文件，包含了运行容器所需的所有信息，包括文件系统、运行时环境、应用程序代码和依赖项。镜像可以看作是容器的模板。
	- 容器（Container）：容器是基于镜像创建的运行实例，它包括了镜像的内容以及在运行时的进程、文件系统的可写层等，可以被启动、停止、删除和暂停。

- 可变性：

	- 镜像是不可变的：一旦创建了一个镜像，它的内容是只读的，不能被修改。要修改一个镜像，需要创建一个新的镜像。
	- 容器是可变的：容器是可以启动、停止、修改和删除的，容器的状态可以随着运行时的需求而变化。

- 用途：

	- 镜像用于分发和部署应用程序：镜像通常由开发人员或运维团队创建，然后分发给其他人在其本地或远程环境中运行容器。
	- 容器用于运行应用程序：容器是实际运行应用程序的实体，它们可以启动多个副本以扩展应用程序的能力，并且可以在不同的环境中轻松部署。

- 生命周期：

	- 镜像生命周期较长：镜像的生命周期通常比容器长，它可以被多次使用来创建多个容器实例。
	- 容器生命周期较短：容器的生命周期通常是短暂的，一旦容器停止或删除，它的状态和数据通常会丢失。


# 使用

## 修改镜像源

新建文件：`/etc/docker/daemon.json`

```json
{
  "registry-mirrors": [
    "https://cr.console.aliyun.com",
    "https://mirror.ccs.tencentyun.com",
    "http://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn"
  ]
}
```

修改完成后重启生效：`systemctl restart docker`

## 镜像

```shell
docker pull [IMAGE ID] # 拉取镜像
docker save [IMAGE ID] > abc_20231115.tar.gz	# 导出镜像到本地
docker load [IMAGE ID] < abc_20231115.tar.gz	# 导入镜像
docker tag [IMAGE ID] acb/abc:1.0	# 修改镜像标签
```

## 容器

### 列出容器

```shell
# 列出容器
docker ps [option]
-a :显示所有的容器，包括未运行的。
-f :根据条件过滤显示的内容。
-l :显示最近创建的容器。
-n :列出最近创建的n个容器。
--no-trunc :不截断输出。
-q :静默模式，只显示容器编号。
-s :显示总的文件大小。
```

### 备份容器

```shell
# 使用 docker commit 命令来创建快照，会生成一个容器快照，可以通过 docker image 来查找

root@cc-desktop:/# docker commit 3df8dbf717b1 ql_jd_backup
root@cc-desktop:/# docker images
REPOSITORY                     TAG       IMAGE ID       CREATED         SIZE
ql_jd_backup                   latest    ea36abb08bef   2 hours ago     930MB
root@cc-desktop:/# docker save -o /data/soft/ql_jd_backup.tar.gz ql_jd_backup


# 容器恢复
root@cc-desktop:/# docker load -i ~/ql_jd_backup.tar.gz
root@cc-desktop:/# docker images
```

### 网络
```shell
docker network connect '网络' '容器'
docker network disconnect '网络' '容器'
```

### 端口

> https://www.cnblogs.com/kingsonfu/p/11578073.html
> 
> https://cloud.tencent.com/developer/article/1833131
> 
> https://www.cnblogs.com/junlin623/p/17365848.html

新建容器时，忘记添加端口映射了，但又不想重建容器时，就可以参考上面文章，在不新建容器的情况下添加端口映射。

需要修改两个文件：

### 其它

```shell
# 进入容器
docker exec -it '容器id' sh
## 使用 root 权限进入容器
docker exec -u 0 -it '容器id' sh
# 查看日志
docker logs '容器ID' -f
```

## update

## --restart 策略

| 命令           | 作用                                                         |
| -------------- | ------------------------------------------------------------ |
| no             | 默认策略，容器退出时不重启容器                               |
| on-failure     | 在容器非正常退出时（退出状态非0），才会重启容器              |
| on-failure:3   | 在容器非正常退出时重启容器，最多重启3次                      |
| always         | 在容器退出时总是重启容器                                     |
| unless-stopped | 在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器（推荐） |

给容器设置 `restart` 策略

```shell
# 设置重启docker时，容器自动启动：
1. 启动时添加参数：docker run -d --restart always tomcat
2. 后期添加参数：docker container update --restart=always 容器名
```

# 其它
## 当容器无法启动，如何修改容器的配置文件？
> https://blog.csdn.net/weixin_40881502/article/details/106294110

```shell
docker inspect [CONTAINER ID]| grep 'MergedDir'

找到这个目录，进去就可以修改容器的部分配置文件
```

## 调用Nvidia显卡

> 参考资料：
> https://www.cnblogs.com/chester-cs/p/14444247.html

当机器上已安装有 `Nvidia` 时，如果让 `Docker` 能调用宿主机的 `nvidia-smi` 命令呢？

 `docker run` 运行时添加参数：`--gpus all`
```shell
docker run -it --name test --gpus all -d ubuntu:20.04
```
此时在 docker 里使用 `nvidia-smi` 命令即可调用宿主机的显卡

还有一个需要注意的点是 `nvidia-smi` 的输出：`CUDA Version: N/A`

其实是环境变量的问题，添加两个参数即可：

```shell
docker run -itd --gpus all \
--name test \
-e NVIDIA_DRIVER_CAPABILITIES=compute,utility \
-e NVIDIA_VISIBLE_DEVICES=all \
ubuntu:20.04
```
