---
title: "Image Source"
date: 2020-12-04

---

# 常用镜像源地址

- 阿里云：[developer.aliyun.com](https://developer.aliyun.com/mirror/)
- 清华源：

# 更换镜像源
## Ubuntu

由于 `Ubunutu` 20.04 与 22.04 镜像源基本一致，只是名称的不同

- `Ubuntu 20.04` 为：

- `Ubuntu 22.04` 为：

1. 备份原镜像源文件

```shell
cp /etc/apt/sources.list{,.bak}
```

2. 修改镜像源

```shell
deb https://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

# deb https://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
```

## CentOS

1. 备份原镜像源文件
```shell
cp /etc/yum.repos.d/CentOS-Base.repo{,.bak}
```

2. 下载镜像源文件
```shell
# CentOS 7
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
```

```shell
yum makecache
yum update
```
