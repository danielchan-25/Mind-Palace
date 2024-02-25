# Apache

## 安装

> 下载地址：https://httpd.apache.org/download.cgi

以 `Ubuntu 20.04` 为例

```shell
apt install -y libpcre3 libpcre3-dev libapr1 libapr1-dev libaprutil1 libaprutil1-dev
```

```shell
wget http://10.17.174.64/download/linux/httpd-2.4.58.tar.gz
tar -xvf httpd-2.4.58.tar.gz
cd httpd-2.4.58/
./configure --prefix=/usr/local/apache2
make && make install
```

## 