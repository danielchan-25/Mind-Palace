---
title: "Apache"

---

# 服务端安装
> 下载地址：https://httpd.apache.org/download.cgi

以 `Ubuntu 20.04` 为例

```bash
apt install -y libpcre3 libpcre3-dev libapr1 libapr1-dev libaprutil1 libaprutil1-dev
```

```bash
wget http://10.17.174.64/download/linux/httpd-2.4.58.tar.gz
tar -xvf httpd-2.4.58.tar.gz
cd httpd-2.4.58/
./configure --prefix=/usr/local/apache2
make && make install
```

## 查看正在使用的配置文件
```shell
apache2ctl -t -D DUMP_INCLUDES
```

这个命令将显示 Apache2 配置中所有被包含的文件，包括正在使用的文件。在输出中，你可以看到哪些配置文件当前正在被 Apache2 服务器加载和使用。
