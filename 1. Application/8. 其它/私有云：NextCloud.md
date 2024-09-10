---
title: "私有云：NextCloud"
date: 2024-04-21

---

NextCloud 需要依赖以下环境：

![](/media/202312/2023-12-07_112341_9259590.7213429769607876.png)

建议使用：`Ubuntu 20.04 LTS` + `MySQL 8.0+` + `Nginx` + `PHP 8.2`

# 简介
Nextcloud是一种自由开源的协作平台和云存储解决方案。它允许用户在他们自己的服务器上存储、同步和共享文件、日历、联系人、音乐、图片和视频等信息。Nextcloud可以被用作企业级的云存储服务，也可以被个人用来管理他们的数据。

Nextcloud提供了许多功能，如文件共享、协作、版本控制、文档编辑、视频会议、加密和备份等。它还支持在各种设备和平台上的访问，包括Web浏览器、移动应用程序和桌面客户端。Nextcloud也有一个广泛的插件生态系统，用户可以利用插件来扩展其功能。

由于Nextcloud是自由开源软件，因此任何人都可以查看和修改其源代码，从而使其更适合他们的需求。这也意味着Nextcloud可以自由地在任何地方使用，而不需要向第三方提供数据。

# 安装

## All-In-One

## Docker

**记得先部署好 `MySQL` 服务器，设置好账号密码，创建好数据库，赋予对应的权限**

**防火墙必须开起来，不然没法运行该容器**

```shell
docker run  \
--name nextcloud --network nextcloud-net \
-p 443:443 -p 8080:80 \
-e MYSQL_DATABASE=nextcloud -e MYSQL_USER=nextCloud \
-e MYSQL_PASSWORD=yb4wXCrQ3DLjwUPPjxzU \
-v ~/nextcloud:/var/www/html \
-d 8bd17975f256
```

或者直接使用 Docker 部署一个 MySQL 服务器：

```shell
docker run -d --name nextcloud-mariadb \
    -e MYSQL_ROOT_PASSWORD=your_password \
    -e MYSQL_DATABASE=nextcloud \
    -e MYSQL_USER=nextcloud \
    -e MYSQL_PASSWORD=your_password \
    --restart always \
    mariadb:latest \
    --transaction-isolation=READ-COMMITTED --binlog-format=ROW
   
# 启动时指向 MySQL 服务器
docker run -d --name nextcloud \
    -p 8080:80 \
    --link nextcloud-mariadb:mariadb \
    -v /your/nextcloud/data:/var/www/html \
    --restart always \
    nextcloud:latest
```

## Docker-Compose

在本地计算机上创建一个名为 `docker-compose.yml` 的文件，并将以下内容复制到文件中。

```yml
version: '3'

services:
  db:
    image: mariadb
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW
    restart: always
    volumes:
      - db:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=your_password
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_PASSWORD=your_password

  app:
    image: nextcloud:fpm
    links:
      - db
    restart: always
    volumes:
      - nextcloud:/var/www/html
    environment:
      - MYSQL_HOST=db
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_PASSWORD=your_password

  web:
    image: nginx
    restart: always
    ports:
      - 8080:80
    volumes:
      - nextcloud:/var/www/html:ro
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app

volumes:
  db:
  nextcloud:
```

*请注意替换your_password为您自己的密码。*

#### 创建 nginx 配置文件

在与 `docker-compose.yml` 文件相同的目录中，创建一个名为 `nginx.conf` 的文件，并将以下内容复制到文件中。

```yml
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
  worker_connections  1024;
}

http {
  include       /etc/nginx/mime.types;
  default_type  application/octet-stream;

  log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

  access_log  /var/log/nginx/access.log  main;

  sendfile        on;
  #tcp_nopush     on;

  keepalive_timeout  65;

  #gzip  on;

  upstream php-handler {
    server app:9000;
  }

  server {
    listen 80;
    server_name localhost;

    # Add headers to serve security related headers
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Robots-Tag none;
    add_header X-Download-Options noopen;
    add_header X-Permitted-Cross-Domain-Policies none;
    add_header Referrer-Policy no-referrer;

    # Path to the root of your installation
    root /var/www/html;

    location = /robots.txt {
      allow all;
      log_not_found off;
      access_log off;
    }

    # The following 2 rules are only needed for the user_webfinger app.
    # Uncomment it if you're planning to use this app.
    #rewrite ^/.well-known/host-meta /public.php?service=host-meta last;
    #rewrite ^/.
```

## 源码部署

> 下载地址：https://download.nextcloud.com/server/releases/latest.zip

部署前提：需安装 Web服务器，以及 PHP

将源码包解压后放在 Web服务器 的 `html/` 目录下，然后访问该源码包的 `index.php` 即可提示安装。

### 使用说明

在浏览器中访问：`http://your_server_ip:8080`

其中your_server_ip是您的服务器IP地址。

您将被重定向到Nextcloud的安装页面。根据提示完成安装即可。

请注意，在生产环境中，应采取适当的安全措施，如使用HTTPS加密通信，并保护数据库和数据存储的访问。

因自带中文界面，且上手容易，所以没有什么使用说明，上手即用。

## 开启日志

修改 `/var/www/html/nextcloud/config/config.php` 文件：
```php
<?php
$CONFIG = array (
  'instanceid' => 'oc5n5kga7wb4',
  'log_type' => 'file',
  'logfile' => 'nextcloud.log',
  "loglevel" => 3,
  "logdateformat" => "F d, Y H:i:s",
);
```
然后就可以在 `/var/www/html/nextcloud` 查看到 `nextcloud.log` 日志，便于分析报错。


## 安装过程报错处理
```json
{"reqId":"5tPQE6zjZfdz40WC8wlG","level":3,"time":"December 07, 2023 07:00:32","remoteAddr":"10.17.174.135","user":"--","app":"base","method":"GET","url":"/nextcloud/status.php","message":"Failed to start session","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36","version":"","exception":{"Exception":"Exception","Message":"Failed to start session","Code":0,"Trace":[{"file":"/var/www/html/nextcloud/lib/base.php","line":446,"function":"__construct","class":"OC\\Session\\Internal","type":"->"},{"file":"/var/www/html/nextcloud/lib/base.php","line":705,"function":"initSession","class":"OC","type":"::"},{"file":"/var/www/html/nextcloud/lib/base.php","line":1196,"function":"init","class":"OC","type":"::"},{"file":"/var/www/html/nextcloud/status.php","line":37,"args":["/var/www/html/nextcloud/lib/base.php"],"function":"require_once"}],"File":"/var/www/html/nextcloud/lib/private/Session/Internal.php","Line":62,"message":"Failed to start session","exception":{},"CustomMessage":"Failed to start session"}}
```

在 `php.ini` 中的 `session.save_path` 新增路径：`/var/www/html`


# 安全与设置警告处理

![](/media/202312/2023-12-07_112430_5343820.8682267867421302.png)

- PHP 内存限制：修改`php.ini`文件，将`memory_limit`修改成大于512MB。
- PHP OPcache 模块没有正确配置：修改`php.ini`文件，将`OPcache`按照官网修改。
- intl：修改`php.ini`文件，将`intl`取消注释。
- PHP 模块“imagick”没有被启用：修改`php.ini`文件，将`imagick`取消注释。
- “Strict-Transport-Security”HTTP 头未设为至少“15552000”秒：修改`nginx.conf`文件，新增：`add_header Strict-Transport-Security "max-age=15552000; includeSubDomains;" always;`。
- HTTP 请求头“X-Robots-Tag”没有配置为“noindex, nofollow”：add_header X-Robots-Tag "noindex, nofollow" always;
- PHP 的安装似乎不正确，无法访问系统环境变量。getenv("PATH") 函数测试返回了一个空值：修改`php-fpm.conf`文件，取消注释即可。

```conf
env[HOSTNAME] = $HOSTNAME
env[PATH] = /usr/local/bin:/usr/bin:/bin
env[TMP] = /tmp
env[TMPDIR] = /tmp
env[TEMP] = /tmp
```


---
参考文档：
> Nginx配置：https://wiki.mageia.org/en/Nextcloud_server_installation_with_NGINX
> OnlyOffice官方文档：https://helpcenter.onlyoffice.com/installation/docs-community-install-docker.aspx
> OnlyOffice官方文档：https://github.com/ONLYOFFICE
> 加密解密：https://blog.csdn.net/qq_35590198/article/details/106574495
> 加密解密：https://www.orgleaf.com/3077.html
> config.php：https://www.moewah.com/archives/1025.html
> config.php：https://www.limvs.cn/archives/2490
> config.php：https://mrlin.net/1443.html
> 设置超时注销：https://tieba.baidu.com/p/7456600701
