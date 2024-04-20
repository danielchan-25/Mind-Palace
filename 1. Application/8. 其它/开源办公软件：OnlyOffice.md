---
title: "开源办公软件：OnlyOffice"
date: 2024-04-21

---


# 服务端

## 安装

部署 `OnlyOffice` 服务器时，必须要 `HTTPS` 协议，所以要映射 **443** 端口

```shell
docker run -itd \
-p 80:80 -p 443:443 \
--restart = always \
--name onlyoffice \
onlyoffice/documentserver
```

## 自签名 SSL 证书
可以使用 SSL 保护对 onlyoffice 应用程序的访问，从而防止未经授权的访问。

虽然 CA 认证的 SSL 证书允许通过 CA 验证信任，但自签名证书也可以提供同等级别的信任验证，只要每个客户端采取一些额外的步骤来验证您网站的身份。

```shell
openssl genrsa -out onlyoffice.key 2048
openssl req -new -key onlyoffice.key -out onlyoffice.csr
openssl x509 -req -days 365 -in onlyoffice.csr -signkey onlyoffice.key -out onlyoffice.crt
```

将以上两个证书添加进`Nginx`配置文件中即可：
```nginx
ssl_certificate "/etc/nginx/onlyoffice.crt";
ssl_certificate_key "/etc/nginx/onlyoffice.key";
```

## 反向代理

```nginx
user www-data;
worker_processes 1;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 1048576;
}

http {
	sendfile on;
	tcp_nopush on;
	types_hash_max_size 2048;
	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;
	access_log off;
	error_log /var/log/nginx/error.log;
	gzip on;
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
	ssl_certificate "/etc/nginx/onlyoffice.crt";
	ssl_certificate_key "/etc/nginx/onlyoffice.key";
}
```

```nginx
include /etc/nginx/includes/http-common.conf;
server {
	listen 0.0.0.0:80;
	listen [::]:80 default_server;

	listen 0.0.0.0:443 ssl;
	listen [::]:443 ssl;
	server_tokens off;

	set $secure_link_secret yZ4R9BHtpgeMiEY7V4Yy;
	include /etc/nginx/includes/ds-*.conf;
}
```

## 测试

使用浏览器访问：https://localhost:443/welcome/


# 客户端

这里以 `NextCloud` 安装客户端为例

## 安装
下载地址: [onlyoffice](https://apps.nextcloud.com/apps/onlyoffice)

离线安装方法：

1. 下载资源包后，放入 `nextcloud/custom_apps/` 下，解压，并赋予对应权限。

2. `NextCloud`【应用】->【已禁用的应用】->【OnlyOffice】启用

3. `NextCloud`【管理设置】->【OnlyOffice】


## 配置

使用 NextCloud 管理员账户，进入设置，点击保存测试。

![](/media/202312/2023-12-12_192407_1568640.5498009809830777.png)

## 报错处理
文档服务内部发生异常: Invalid token

查看
```bash
docker exec onlyoffice \ 
/var/www/onlyoffice/documentserver/npm/json -f /etc/onlyoffice/documentserver/local.json 'services.CoAuthoring.secret.session.string'
```

服务器重启后，无法访问 `https://10.17.174.115:8443/welcome/` 时，先进 `onlyoffice` 容器，检查 `Nginx` 是否启动了 443 端口，如果没有，则查看上面的配置文件添加 443 端口。

## 加密解密

在使用 OwnCloud 的时候，将文件都加密了，导致下载的文件都无法打开，这个时候回到 OwnCloud 打开，发现报错：
```php
Sabre\DAV\Exception\Forbidden Encryption not ready: Module with id: OC_DEFAULT_MODULE does not exist.
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<d:error xmlns:d="DAV:" xmlns:s="http://sabredav.org/ns">
<s:exception>Sabre\DAV\Exception\Forbidden</s:exception>
<s:message>Encryption not ready: Module with id: OC_DEFAULT_MODULE does not exist.</s:message>
...
</d:error>
```

其中主要报错是：`OC_DEFAULT_MODULE`，解决方法：

1. 回到 OwnCloud，将加密模块（Default encryption module）打开

2. 重新在页面下载文件，然后发现能直接打开。