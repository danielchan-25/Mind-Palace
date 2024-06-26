---
title: "Desktop"

date: 2023-01-20

---

Ubuntu 自带了 Gnome桌面，但如想在其它电脑上进行远程，无法实现，所以需安装 Xrdp
```shell
# 安装 xrdp
apt install xrdp
systemctl start xrdp && systemctl enable xrdp

# 添加用户进 xrdp 组：/etc/ssl/private/ssl-cert-snakeoil.key
adduser cc ssl-cert

# 查看 xrdp 端口
netstat -tnlp | grep 3389

# 配置环境变量
echo "gnome-session" > /home/cc/.xsession
```

# 环境变量

在 Linux 中，环境变量一般有这几个文件：

- `/etc/profile`

- `~/.bashrc`

---
## 添加环境变量
```shell
export PATH=/opt/MegaRAID/MegaCli:$PATH
```

---
## 其它
Linux 中新建用户后，登录用户时没有加载环境变量配置文件

这个因为该用户通过 `/usr/bin/sh` 时没有加载配置文件，可以修改 `bash`，如：
```sh
painer:x:1001:1001::/home/painer:/usr/bin/sh

# 更改为：
painer:x:1001:1001::/home/painer:/usr/bin/bash
```
