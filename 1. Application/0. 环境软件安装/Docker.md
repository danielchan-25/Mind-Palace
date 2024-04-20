---
title: "Docker"

date: 2020-07-10

---

# Linux

```shell
# Centos & Ubuntu 共用
curl -sSL https://get.daocloud.io/docker | sh
curl -fsSL https://test.docker.com -o test-docker.sh
```

# Windows
`Windows` 下最好使用 `WSL2` 安装管理容器，因为 `Docker Desktop` 占用内存太高了不建议使用

> https://zhuanlan.zhihu.com/p/543280130


# 配置文件

`Docker` 一般不会建立配置文件，可以自行创建。

- Linux: `/etc/docker/daemon.json`

- Windows: `C:\ProgramData\docker\config\daemon.json`

```json
{
	"registry-mirrors":[
		"https://docker.mirrors.ustc.edu.cn/",	// 科大镜像
		"https://hub-mirror.c.163.com/"	// 网易镜像
	],
	"dns": ["202.96.128.86","202.96.128.166","114.114.114.114"]	// DNS配置
}
```

阿里云镜像获取地址：[https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)，登陆后，左侧菜单选中镜像加速器就可以看到你的专属地址了