---
title: "私有云：NextCloud"
date: 2024-04-21

---

NextCloud 需要依赖以下环境：

![](/media/202312/2023-12-07_112341_9259590.7213429769607876.png)

建议使用：`Ubuntu 20.04 LTS` + `MySQL 8.0+` + `Nginx` + `PHP 8.2`

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