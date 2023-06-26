# Docker

# 安装

```sh
# Centos & Ubuntu 共用
curl -sSL https://get.daocloud.io/docker | sh
```
# 常用命令

## 镜像操作

```sh
# 拉取镜像
docker pull 镜像
```

## 容器操作

### 列出容器

```sh
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

```sh
# 使用 docker commit 命令来创建快照，会生成一个容器快照，可以通过 docker image 来查找

root@cc-desktop:/# docker commit -p 3df8dbf717b1 ql_jd_backup
root@cc-desktop:/# docker images
REPOSITORY                     TAG       IMAGE ID       CREATED         SIZE
ql_jd_backup                   latest    ea36abb08bef   2 hours ago     930MB
root@cc-desktop:/# docker save -o /data/soft/ql_jd_backup.tar.gz ql_jd_backup


# 容器恢复
root@cc-desktop:/# docker load -i ~/ql_jd_backup.tar.gz
root@cc-desktop:/# docker images
```

### 网络
```sh
docker network connect '网络' '容器'
docker network disconnect '网络' '容器'
```

### 其它

```sh
# 进入容器
docker exec -it '容器id' sh
## 使用 root 权限进入容器
docker exec -u 0 -it '容器id' sh
# 查看日志
docker logs '容器ID' -f

```

## --restart 策略

| 命令           | 作用                                                         |
| -------------- | ------------------------------------------------------------ |
| no             | 默认策略，容器退出时不重启容器                               |
| on-failure     | 在容器非正常退出时（退出状态非0），才会重启容器              |
| on-failure:3   | 在容器非正常退出时重启容器，最多重启3次                      |
| always         | 在容器退出时总是重启容器                                     |
| unless-stopped | 在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器（推荐） |

给容器设置 `restart` 策略

```sh
# 设置重启docker时，容器自动启动：
1. 启动时添加参数：docker run -d --restart always tomcat
2. 后期添加参数：docker container update --restart=always 容器名
```

# 调用Nvidia显卡
> 参考资料：
> https://www.cnblogs.com/chester-cs/p/14444247.html

当机器上已安装有 `Nvidia` 时，如果让 `Docker` 能调用宿主机的 `nvidia-smi` 命令呢？

 `docker run` 运行时添加参数：`--gpus all`
```bash
docker run -it --name test --gpus all -d ubuntu:20.04
```
此时在 docker 里使用 `nvidia-smi` 命令即可调用宿主机的显卡

还有一个需要注意的点是 `nvidia-smi` 的输出：`CUDA Version: N/A`

其实是环境变量的问题，添加两个参数即可：
```bash
docker run -itd --gpus all \
--name test \
-e NVIDIA_DRIVER_CAPABILITIES=compute,utility \
-e NVIDIA_VISIBLE_DEVICES=all \
ubuntu:20.04
```