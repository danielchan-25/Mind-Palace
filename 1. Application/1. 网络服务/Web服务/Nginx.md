---
title: "Nginx"

---

`Nginx` 是一个轻量级/高性能的反向代理 Web 服务器，用于 `HTTP`、`HTTPS`、`SMTP`、`POP3` 和 `IMAP` 协议。

它实现非常高效的反向代理、负载平衡，可以处理2-3万并发连接数，官方监测能支持5万并发，现在中国使用 `Nginx` 网站用户有很多，例如：新浪、网易、 腾讯等。

# 1. 简介

## 1.1 有哪些优点

- 跨平台、配置简单。
- 非阻塞、高并发连接：处理 2-3 万并发连接数，官方监测能支持 5 万并发。
- 内存消耗小：开启 10 个 `Nginx` 才占 150M 内存。
- 成本低廉，且开源。
- 稳定性高，宕机的概率非常小。
- 内置的健康检查功能：如果有一个服务器宕机，会做一个健康检查，再发送的请求就不会发送到宕机的服务器了。重新将请求提交到其他的节点上

## 1.2 应用场景
- `HTTP` 服务器。`Nginx` 是一个 `HTTP` 服务可以独立提供 `HTTP` 服务。可以做网页静态服务器。
- 虚拟主机。可以实现在一台服务器虚拟出多个网站，例如个人网站使用的虚拟机。
- 反向代理，负载均衡。当网站的访问量达到一定程度后，单台服务器不能满足用户的请求时，需要用多台服务器集群可以使用 `Nginx` 做反向代理。并且多台服务器可以平均分担负载，不会应为某台服务器负载高宕机而某台服务器闲置的情况。
- `Nginx` 中也可以配置安全管理、比如可以使用 `Nginx` 搭建 `API` 接口网关,对每个接口服务进行拦截。

## 1.3 目录结构

```nginx
tree /usr/local/nginx
/usr/local/nginx
├── client_body_temp
├── conf # Nginx所有配置文件的目录
│ ├── fastcgi.conf # fastcgi相关参数的配置文件
│ ├── fastcgi.conf.default         # fastcgi.conf的原始备份文件
│ ├── fastcgi_params # fastcgi的参数文件
│ ├── fastcgi_params.default       
│ ├── koi-utf
│ ├── koi-win
│ ├── mime.types # 媒体类型
│ ├── mime.types.default
│ ├── nginx.conf # Nginx主配置文件
│ ├── nginx.conf.default
│ ├── scgi_params # scgi相关参数文件
│ ├── scgi_params.default  
│ ├── uwsgi_params # uwsgi相关参数文件
│ ├── uwsgi_params.default
│ └── win-utf
├── fastcgi_temp # fastcgi临时数据目录
├── html # Nginx默认站点目录
│ ├── 50x.html # 错误页面优雅替代显示文件，例如当出现502错误时会调用此页面
│ └── index.html # 默认的首页文件
├── logs # Nginx日志目录
│ ├── access.log # 访问日志文件
│ ├── error.log # 错误日志文件
│ └── nginx.pid # pid文件，Nginx进程启动后，会把所有进程的ID号写到此文件
├── proxy_temp # 临时目录
├── sbin # Nginx命令目录
│ └── nginx # Nginx的启动命令
├── scgi_temp # 临时目录
└── uwsgi_temp # 临时目录
```

## 1.4 请求过程

```nginx
server {                            # 第一个Server区块开始，表示一个独立的虚拟主机站点
   listen 80；                      # 提供服务的端口，默认80
   server_name localhost;           # 提供服务的域名主机名
   location / {                     # 第一个location区块开始
     root   html;                   # 站点的根目录，相当于Nginx的安装目录
     index  index.html index.html;  # 默认的首页文件，多个用空格分开
}                                   # 第一个location区块结果
```

- 首先，`Nginx` 在启动时，会解析配置文件，得到需要监听的端口与 IP 地址，然后在 `Nginx` 的 `Master` 进程里面先初始化好这个监控的 `Socket` (创建 `Socket`，设置 `addr`、`reuse` 等选项，绑定到指定的 ip 地址端口，再 listen 监听)。
- 然后，再 `fork` (一个现有进程可以调用 `fork` 函数创建一个新进程。由 `fork` 创建的新进程被称为子进程 )出多个子进程出来。
- 之后，子进程会竞争 `accept` 新的连接。此时，客户端就可以向 `Nginx` 发起连接了。当客户端与 `Nginx` 进行三次握手，与 `Nginx` 建立好一个连接后。此时，某一个子进程会 `accept` 成功，得到这个建立好的连接的 `Socket` ，然后创建 `Nginx` 对连接的封装，即 `ngx_connection_t` 结构体。
- 接着，设置读写事件处理函数，并添加读写事件来与客户端进行数据的交换。
- 最后，`Nginx` 或客户端来主动关掉连接，到此，一个连接就寿终正寝了。



# 2. 配置文件

## 2.1 结构

```nginx
...              #全局块

events {         #events块
   ...
}

http      #http块
{
    ...   #http全局块
    server        #server块
    { 
        ...       #server全局块
        location [PATTERN]   #location块
        {
            ...
        }
    }
}
```

`Nginx`配置文件分为三大块：

- 全局块
- events块
- http块

## 2.2 全局块

配置影响`nginx`全局的指令。

一般有运行`nginx`服务器的用户组

`nginx`进程 `pid` 存放路径

日志存放路径

配置文件引入

允许生成`worker process`数等

```nginx
# 定义Nginx运行的用户和用户组
user www www;

# nginx进程数，建议设置为等于CPU总核心数。
worker_processes 8;

# 全局错误日志定义类型，[ debug | info | notice | warn | error | crit ]
error_log /usr/local/nginx/logs/error.log info;

# 进程pid文件
pid /usr/local/nginx/logs/nginx.pid;
```

## 2.3 events块

配置影响nginx服务器或与用户的网络连接。

有每个进程的最大连接数

选取哪种事件驱动模型处理连接请求

是否允许同时接受多个网路连接

开启多个网络连接序列化等

```nginx
events {
# 标识单个worker进程的最大并发数
    worker_connections  1024;
}
```

## 2.4 http块

可以嵌套多个`server`，配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置。

如文件引入，`mime-type`定义，日志自定义，是否使用`sendfile`传输文件，连接超时时间，单连接请求数等。

```nginx
```

### 2.4.1 server

虚拟主机是一种特殊的软硬件技术，它可以将网络上的每一台计算机分成多个虚拟主机。

每个虚拟主机都可以独立对外提供www服务。

从而实现一台主机能对外提供多个web服务，而且每个虚拟主机之间是互不影响的。

Nginx 提供了三种虚拟主机配置方式，最常用的是第三种，相对于 ip 地址和端口号，域名更方便记忆和使用。

1. 基于IP的虚拟主机
2. 基于端口的虚拟主机
3. 基于域名的虚拟主机



1. 基于 IP

   1. 第一步：执行命令`ip addr`打印协议地址,得知网卡名是`ens33`，ip地址是`192.168.225.131`

   2. 第二步：进入到`/etc/sysconfig/network-scripts/`修改`ifcfg-ens33`文件添加两个ip地址

   3. 第三步：重启网络，并检查配置是否生效，发现`ens33`对应三个ip地址

   4. 第四步：进入到`/usr/local/nginx/`目录下，拷贝三份`html`目录，并分别修改`index.html`文件便于区分测试

   5. 第五步：修改`Nginx`配置文件，监听的端口不变，修改`server_name`为对应ip地址，修改`root`为对应的`html`目录

   6. 第六步：重启`Nginx`服务，在浏览器上分别访问三个ip地址，观察页面变化

      若你发现不同的ip地址打印不同页面，和效果图相似，则代表配置成功。

      

2. 基于端口

   1. 基于端口的虚拟主机和基于ip的虚拟主机配置几乎一样
   2. 只是在修改`Nginx`配置文件时，只修改监听的端口和`root`对应的目录，其他的没有变。这里就不贴命令了。

   

3. 基于域名

   1. 这里通过修改`window`系统下的`host`文件来模拟DNS服务器。

   2. 第一步：在`window`环境中，修改`host`文件，添加ip 域名映射关系，用来模拟DNS服务器

   3. 第二步：进入到`/usr/local/nginx/`目录下，拷贝两份`html`目录，分别修改`index.html`文件便于区分测试

   4. 第三步：修改`Nginx`配置文件，监听的端口不变，修改`server_name`为对应域名地址，修改`root`为对应的`html`目录

   5. 第四步：重启`Nginx`服务，在浏览器上分别访问两个域名地址，观察页面变化

      若你发现不同的域名地址打印不同页面，和效果图相似，则代表配置成功。

```nginx
# Windows
C:\Windows\System32\drivers\etc\hosts文件
# nginx 域名配置虚拟主机
192.168.225.131 www.itdragon.com
192.168.225.131 picture.itdragon.com
192.168.225.131 search.itdragon.com

# CentOS
[root@itdragon nginx]# cp -r html/ html-search
[root@itdragon nginx]# cp -r html/ html-picture
[root@itdragon nginx]# vim html-search/index.html 
[root@itdragon nginx]# vim html-picture/index.html
[root@itdragon nginx]# vim conf/nginx.conf
server {
	listen       80;
	server_name  search.itdragon.com;
	location / {
	   root   html-search;
	   index  index.html index.htm;
	}
}
server {
	listen       80;
	server_name  picture.itdragon.com;
	location / {
	   root   html-picture;
	   index  index.html index.htm;
	}
}
[root@itdragon nginx]# sbin/nginx -s reload
```

### 2.4.2 location

`location` 指令的作用是根据用户请求的URI来执行不同的应用，也就是根据用户请求的网站URL进行匹配，匹配成功即进行相关的操作。

| 匹配符 | 匹配规则                     | 优先级 |
| ------ | ---------------------------- | ------ |
| =      | 精确匹配                     | 1      |
| ^~     | 以某个字符串开头             | 2      |
| ～     | 区分大小写的正则匹配         | 3      |
| ~*     | 不区分大小写的正则匹配       | 4      |
| !~     | 区分大小写不匹配的正则       | 5      |
| !~*    | 不区分大小写不匹配的正则     | 6      |
| /      | 通用匹配，任何请求都会匹配到 | 7      |

```nginx
# 优先级1,精确匹配，根路径
location =/ {
    return 400;
}

# 优先级2,以某个字符串开头,以av开头的，优先匹配这里，区分大小写
location ^~ /av {
   root /data/av/;
}

# 优先级3，区分大小写的正则匹配，匹配/media*****路径
location ~ /media {
      alias /data/static/;
}

# 优先级4 ，不区分大小写的正则匹配，所有的****.jpg|gif|png 都走这里
location ~* .*\.(jpg|gif|png|js|css)$ {
   root  /data/av/;
}

# 优先7，通用匹配
location / {
    return 403;
}
```

# 3. 常用配置

## 3.1 日志

Nginx 的日志有以下几个主要功能：

1. 记录访问日志（access log）：记录每个请求的信息，如客户端 IP 地址、请求时间、请求的 URI、HTTP 状态码、发送给客户端的数据大小等。
2. 记录错误日志（error log）：记录服务器运行过程中的错误信息，如语法错误、请求处理错误、服务无响应等。
3. 实时监控日志文件：Nginx 支持实时监控日志文件，可以通过配置实现将日志信息发送到指定的远程服务器或者以邮件的形式发送到管理员的邮箱。
4. 日志文件的切割：为了防止日志文件过大，Nginx 支持将日志文件自动分割成多个较小的文件，以方便管理和备份。
5. 自定义日志格式：Nginx 支持自定义日志格式，可以按照用户的需求定义日志输出的格式和内容，以方便日志分析和处理。
6. 日志格式化：Nginx 支持将日志信息格式化成可读性更好的形式，以便日志的分析和处理。

### 3.1.1 日志格式化

以下是一些常用的 Nginx 日志格式变量：

- `$remote_addr`：客户端 IP 地址；
- `$remote_user`：客户端用户名；
- `$time_local`：本地时间，格式为 `[day/month/year:hour:minute:second zone]`；
- `$request`：请求的方法、URI 和协议；
- `$status`：HTTP 状态码；
- `$body_bytes_sent`：发送给客户端的数据字节数；
- `$http_referer`：来自客户端的 HTTP Referer 头；
- `$http_user_agent`：来自客户端的 User-Agent 头；
- `$http_x_forwarded_for`：来自代理服务器的 X-Forwarded-For 头；
- `$server_name`：当前请求被处理的服务器名称；
- `$request_time`：客户端请求到收到响应的时间，单位为秒，精度为毫秒；
- `$upstream_response_time`：Nginx 接收到响应的时间和发送请求给后端服务器的时间之差，单位为秒，精度为毫秒；

在配置日志格式时，变量需要使用 `$` 符号进行引用，变量和普通字符之间可以插入任意的字符，例如空格、短横线等。

以下是一个常用的日志格式：

```nginx
log_format  main  '"$remote_addr" - "$remote_user" - "$time_local" - "$request_method" - "$request_uri" "$server_protocol"'
                  '"$status" "$body_bytes_sent" "$http_referer" '
                  '"$http_user_agent" "$http_range" "$request_time" "$http_x_forwarded_for"';
```

### 3.1.2 日志切割

日志轮换是一种将日志文件切割成多个文件，以便于管理和备份的技术。

可以通过配置日志轮换（log rotation）的方式实现日志切割。



Nginx 提供了两种日志轮换方式：基于时间的轮换和基于文件大小的轮换。

1. 基于时间的轮换方式，可以通过在Nginx配置文件中设置access_log和error_log指令的参数，使用日期和时间格式来指定日志文件名，例如：

   ```nginx
   access_log /var/log/nginx/access.log.%Y%m%d;
   error_log /var/log/nginx/error.log.%Y%m%d;
   ```

   上述配置会将每天的访问日志和错误日志分别存储在以日期命名的文件中，例如 `/access.log.20220310`

   

2. 基于文件大小的轮换方式，可以通过使用Linux系统自带的logrotate工具来实现。logrotate可以根据一定的策略，定期轮换日志文件，以防止日志文件无限增长占满磁盘空间。

   1. 创建一个名为 nginx 的 `logrotate` 配置文件，配置文件路径一般为 `/etc/logrotate.d/nginx`

      ```nginx
      /var/log/nginx/*.log {
          daily
          rotate 7
          missingok
          compress
          delaycompress
          notifempty
          create 0640 nginx adm
          sharedscripts
          postrotate
              /usr/sbin/nginx -s reopen
          endscript
      }
      ```

   2. 配置logrotate定时任务，使其每天自动执行轮换操作。可以编辑/etc/crontab文件，添加以下一行：

      ```sh
      0 0 * * * root /usr/sbin/logrotate /etc/logrotate.d/nginx
      
      # 上述配置表示每天0点0分执行一次logrotate命令，轮换/etc/logrotate.d/nginx中指定的所有日志文件。
      ```

      

另外我们也可以使用 Shell 脚本来进行日志切割：

```sh
#!/bin/bash
#此脚本用于自动分割Nginx的日志，包括access.log和error.log
#每天00:00执行此脚本 将前一天的access.log重命名为access-xxxx-xx-xx.log格式，并重新打开日志文件

#Nginx日志文件所在目录
LOG_PATH=/data/nginx/logs

#获取昨天的日期
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)

#获取pid文件路径
PID=/data/nginx/logs/nginx.pid

#分割日志
mv ${LOG_PATH}/access.log ${LOG_PATH}/access-${YESTERDAY}.log
mv ${LOG_PATH}/error.log ${LOG_PATH}/error-${YESTERDAY}.log

#向Nginx主进程发送USR1信号，重新打开日志文件
kill -USR1 `cat ${PID}`
```

### 3.1.3 多个 access_log

在Nginx中可以为每个server、location或http段配置多个access_log，来分别记录不同类型的访问日志，方便统计分析。

在Nginx配置文件中，可以通过在server、location或http段中配置多个access_log指令来实现：

```nginx
http {
    # 全局默认的 access_log
    access_log /var/log/nginx/access.log;

    server {
        # 记录该 server 下的 access_log
        access_log /var/log/nginx/example.access.log;

        location /static/ {
            alias /var/www/example.com/static/;
            # 记录 /static/ 路径下的 access_log
            access_log /var/log/nginx/example.static.access.log;
        }

        location / {
            proxy_pass http://127.0.0.1:8000/;
            # 记录 proxy_pass 的请求的 access_log
            access_log /var/log/nginx/example.proxy.access.log;
        }
    }
}
```

在这个示例中，我们设置了多个 access_log

包括全局默认的 access_log，每个 server 都有一个单独的 access_log，以及每个 location 都有一个单独的 access_log。

可以根据需要在不同的作用域（全局、server、location）下设置不同的 access_log，以记录不同范围和类型的请求。

## 3.2 反向代理

### 3.2.1 什么是反向代理

代理服务器：是一个夹在客户机和目标主机中间的服务器。能提高客户机访问响应速度，还能设置防火墙过滤不安全信息。

响应速度快：客户机发送请求，代理服务器接收请求后，再转发给目标主机。目标主机接收请求并将数据返回给代理服务器，代理服务器将数据返回给客户机同时也会保存数据到本地。若客户机下次有相同的请求，则直接从本地数据返回。从而提高了响应的速度。

设置防火墙：因为代理服务器夹在客户机和目标主机中间。客户机所有的请求都会经过代理服务器，所以如果在代理服务器上设置防火墙，则可以过滤一些不安全的信息，同时也方便管理。

清楚了代理服务器后，我们再来了解正向代理和反向代理的区别：

正向代理：顾客："服务员，我就要厨师A做的七彩红烧肉"; 服务员："好嘞，我这就安排厨师A给您做！"
反向代理：顾客："服务员，我要一份七彩红烧肉"; 服务员："好嘞，我们的厨师B炒菜贼好吃！"
不知道大家看懂没有。顾客就是客户机，服务员就是代理服务器，厨师们就是目标主机。
正向代理就相当于客户机明确指定目标主机提供服务(目标主机被动接收请求)。
反向代理就相当于客户机提供需求，代理服务器从一群目标主机中找一台去实现该需求(目标主机主动接收请求)。

### 3.2.2 怎么配置反向代理

第一步：准备两个`tomcat`服务器，端口分别是`8081`和`8082`，并分别修改`index.jsp`文件便于区分测试
第二步：进入到`/usr/local/nginx/`目录下，修改`Nginx`配置文件。`upstream`定义每个设备的状态，`server`配置服务，`server_name`指定域名，`proxy_pass`代理转发到那台设备上
第三步：重启服务，在浏览器上输入不同的域名，会跳到对应的页面
Nginx的反向代理其实是在做请求的转发，后台有多个http服务器提供服务，Nginx的功能就是把请求转发给后面的服务器，并决定把请求转发给哪台服务器。

```nginx
[root@itdragon ~]# vim /usr/local/solr/tomcat1/webapps/ROOT/index.jsp 
[root@itdragon ~]# vim /usr/local/solr/tomcat2/webapps/ROOT/index.jsp
[root@itdragon ~]# cd /usr/local/nginx
[root@itdragon nginx]# vim conf/nginx.conf
upstream searchserver {
    server 192.168.225.133:8081;
}
upstream pictureserver {
	server 192.168.225.133:8082;
}
server {
	listen       80;
	server_name  search.itdragon.com;
	location / {
	   proxy_pass   http://searchserver;
	   index  index.html index.htm;
	}
}
server {
	listen       80;
	server_name  picture.itdragon.com;
	location / {
	   proxy_pass   http://pictureserver;
	   index  index.html index.htm;
	}
}
[root@itdragon nginx]# sbin/nginx -s reload
```

### 3.2.3 流程

浏览器访问`search.itdragon.com`，通过本地host文件域名解析，找到`192.168.225.131` `Nginx`虚拟主机，`Nginx`接收客户机请求，找到`server_name`为`search`.`itdragon.com`的节点，再根据`proxy_pass`对应的`http`路径，将请求转发到`upstream searchserver`上，即端口号为`8081`的`tomcat`服务器。
客户机访问 ---> search.itdragon.com ---> host ---> Nginx ---> server_name ---> proxy_pass ---> upstream---> tomcat

### 3.2.4 举例

现有两台机器：192.168.1.1、192.168.1.2、192.168.1.3

其中：192.168.1.1 是 zabbix 服务器

192.168.1.2正常连接外网，192.168.1.3不能联网

那我要在192.168.1.3上安装zabbix，怎么办？

思路：使用 192.168.1.2 反向代理到 192.168.1.3

先设置192.168.1.2为服务端，设置

```nginx
# 192.168.1.2 的Nginx配置
upstream zabbix_server{
	server 192.168.1.1:8080;
}
server{
	listen 8081;
	proxy_pass zabbix_server;
}

# 192.168.1.3 的Nginx配置
upstream zabbix_server{
	server 192.168.1.2:8081;
}
server{
	listen 8082;
	proxy_pass zabbix_server;
}
```

## 3.3 负载均衡
### 3.3.1 什么是负载均衡
为了避免服务器崩溃，大家会通过负载均衡的方式来分担服务器压力。
将对台服务器组成一个集群，当用户访问时，先访问到一个转发服务器，再由转发服务器将访问分发到压力更小的服务器。

### 3.3.2 怎么做负载均衡
负载均衡实现的策略有以下五种：
1. 轮询(默认)
    每个请求按时间顺序逐一分配到不同的后端服务器
    如果后端某个服务器宕机，能自动剔除故障系统。
    ```nginx
    upstream backserver { 
        server 192.168.0.12; 
        server 192.168.0.13; 
    }
    ```
2. 权重 weight
    weight的值越大，分配到的访问概率越高
    主要用于后端每台服务器性能不均衡的情况下。其次是为在主从的情况下设置不同的权值，达到合理有效的地利用主机资源。
    ```nginx
    # 权重越高，在被访问的概率越大，如上例，分别是20%，80%。
    upstream backserver { 
        server 192.168.0.12 weight=2; 
        server 192.168.0.13 weight=8; 
    }
    ```
3. ip_hash(IP绑定)
    每个请求按访问IP的哈希结果分配，使来自同一个IP的访客固定访问一台后端服务器，并且可以有效解决动态网页存在的session共享问题
    ```nginx
    upstream backserver { 
        ip_hash; 
        server 192.168.0.12:88; 
        server 192.168.0.13:80; 
    }
    ```
4. fair(第三方插件)
    ** 必须安装upstream_fair模块。**
    对比 weight、ip_hash更加智能的负载均衡算法
    fair算法可以根据页面大小和加载时间长短智能地进行负载均衡，响应时间短的优先分配。
    ```nginx
    # 哪个服务器的响应速度快，就将请求分配到那个服务器上。
    upstream backserver { 
        server server1; 
        server server2; 
        fair; 
    }
    ```
5. url_hash(第三方插件)
    ** 必须安装Nginx的hash软件包 **
    按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，可以进一步提高后端缓存服务器的效率。
    ```nginx
    upstream backserver { 
        server squid1:3128; 
        server squid2:3128; 
    hash $request_uri; 
        hash_method crc32; 
    }
    ```
	

## 3.4 动静分离

### 3.4.1 什么是动静分离

动态资源、静态资源分离简单的概括是：**动态文件与静态文件的分离**

动态资源、静态资源分离，是让动态网站里的动态网页根据一定规则把不变的资源和经常变的资源区分开来，动静资源做好了拆分以后我们就可以根据静态资源的特点将其做缓存操作，这就是网站静态化处理的核心思路。

### 3.4.2 怎么做动静分离

在我们的软件开发中，有些请求是需要后台处理的（如：.jsp,.do 等等），有些请求是不需要经过后台处理的（如：css、html、jpg、js 等等文件），这些不需要经过后台处理的文件称为静态文件，否则动态文件。
因此我们后台处理忽略静态文件。这会有人又说那我后台忽略静态文件不就完了吗？当然这是可以的，但是这样后台的请求次数就明显增多了。在我们对资源的响应速度有要求的时候，我们应该使用这种动静分离的策略去解决动、静分离将网站静态资源（HTML，JavaScript，CSS，img等文件）与后台应用分开部署，提高用户访问静态代码的速度，降低对后台应用访问
这里我们将静态资源放到 `Nginx` 中，动态资源转发到 `Tomcat` 服务器中去。
当然，因为现在七牛、阿里云等 CDN 服务已经很成熟，主流的做法，是把静态资源缓存到 CDN 服务中，从而提升访问速度。
相比本地的 `Nginx` 来说，CDN 服务器由于在国内有更多的节点，可以实现用户的就近访问。并且，CDN 服务可以提供更大的带宽，不像我们自己的应用服务，提供的带宽是有限的
只需要指定路径对应的目录。`location/` 可以使用正则表达式匹配。并指定对应的硬盘中的目录。

```nginx
location /image/ {
    root /usr/local/static/;
    autoindex on;
}
步骤：
mkdir /usr/local/static/image   # 创建目录
cd  /usr/local/static/image     # 进入目录
photo.jpg                       # 上传照片
sudo nginx -s reload            # 重启nginx
```

打开浏览器 输入 `server_name/image/1.jpg` 就可以访问该静态图片了

## 3.5 地址重写

获得一个来访的URL请求，然后改写成服务器可以处理的另一个URL，也就是地址栏被重写。
优点：缩短URL，隐藏实际路径提高安全性，易于用户记忆和键入，易于被搜索引擎收录

> http://jd123.com ---> http://jd.com

支持地址重写的模块有以下三个：

1. `ngx_http_rewrite_module`：这是 Nginx 的默认地址重写模块，提供了丰富的地址重写功能，可以根据 URL 匹配规则对请求进行重写、重定向、反向代理等操作。
2. `ngx_http_proxy_module`：这是 Nginx 的反向代理模块，可以实现将请求转发到后端服务器进行处理，同时还可以进行地址重写、负载均衡等操作。
3. `ngx_http_map_module`：这是 Nginx 的映射模块，可以实现将一些特定的 URL 映射为另一个 URL，或根据 URL 中的参数值进行不同的处理。它可以用来简化复杂的地址重写规则，提高配置的可读性和可维护性。

使用说明： `rewrite` 参数，可以放在`server{}`, ` if{}`, `location{}`段中

```nginx
# 语法：
rewrite < regex > < replacement > [flag]
rewrite 旧地址 新地址 [选项]
```

| flag参数  | 说明                                     |
| --------- | ---------------------------------------- |
| break     | 停止执行其他的重写规则，完成本次请求     |
| last      | 停止执行其他重写规则，地址栏不改变       |
| redirect  | 302临时重定向，地址栏改变，爬虫不更新URL |
| permanent | 301永久重定向，地址栏改变，爬虫更新URL   |

### 3.5.1 怎么做地址重写

- 根据客户端类型，进行地址重写

```nginx
# 当检测到客户端包含 iPhone，访问 / 下的所有网页都会跳转到 /status
if ( $http_user_agent ~* "iPhone" ) {
rewrite	^/	/status	last;
}
# 当检测到客户端包含 Android，访问 / 下的所有网页都会跳转到 baidu.com
if ( $http_user_agent ~* "Android" ) {
rewrite	^/ http://baidu.com/;
}
```

- 也是根据客户端类型，进行地址重写

```nginx
# 先设置一个变量为0
# 当客户端包含有 iPhone 时，设置变量为1，返回 /status
# 当客户端包含有 Android 时，设置变量为2，返回 www.zhihu.com
# 当客户端包含有 curl 时，设置变量为3，返回 baidu.com
# 当客户端包含有 wget 时，设置变量为4，返回 Nginx的安装包

set $device_type 0;
if ( $http_user_agent ~* "iPhone" ) {
set $device_type 1;
}
if ( $http_user_agent ~* "Android") {
set $device_type 2;
}
if ( $http_user_agent ~* "curl" ) {
set $device_type 3;
}
if ( $http_user_agent ~* "wget" ) {
set $device_type 4;
}

if ( $device_type = 1 ) {
rewrite ^(.*)$ /status last;
}
if ( $device_type = 2 ) {
rewrite ^(.*)$ https://www.zhihu.com/ last;
}
if ( $device_type = 3 ) {
rewrite ^/ http://baidu.com/ last;
}
if ( $device_type = 4 ) {
rewrite ^/ftp https://nginx.org/download/nginx-1.22.0.tar.gz last;
}
```

- 根据账号尾号，进行地址重写

```nginx
# 潮阳 iPtv 例子
## 当账号尾号为：0 的用户，都会通过地址重写，重新访问 URL

# 先设置一个变量（生成变量的意思，暂不赋值）
# 当账号尾数为：0 的时候，设置变量为：flag1
# 当账号等于 “” 的时候，设置变量为：flag2
set $flag 0;
if ($arg_account ~ .*[0]$) {
set $flag 1;
}
if ($arg_account = "08099800" ) {
set $flag 2;
}
# 当变量为 1 的时候，地址重写到 XXX
# 当变量为其它的时候，则不执行任何操作
if ($flag = 1) {
rewrite ^/public/(.*)$ http://172.16.64.36:8000/public/$1 last;
}
```

- 根据IP地址，进行地址跳转

有些公司可能有这样的需求
如:我的网站或者网页游戏需要更新，所有的用户或者玩家访问到的是一个停服更新页面
而本公司的IP可以访问，甚至说本公司的某个内网IP可以访问，用于确认更新成功与否

```nginx
# Nginx多重条件判断(只是一个简单的例子，自己可以更改或者增加更多的判断条件)，下面是两个例子和写法:
# 1、可以作为nginx的停服更新使用，仅允许222.222.222.222或者内网的两个IP访问,其他IP都rewrite到停服页面
set $my_ip ''; 
if ( $remote_addr = 222.222.222.222) {set $my_ip 1;} #注意这里的$remote_addr如何用了负载均衡的话,这里应该是$http_x_forwarded_for
if ( $remote_addr = 192.168.1.170 ) { set $my_ip 1;}
if ( $remote_addr = 192.168.1.169 ) { set $my_ip 1;}
if ( $my_ip != 1) {rewrite ^/design/(.*)\.php$ /tingfu.html?$1&;}  #将*.php转到tingfu.html

# 2、访问某个php应用的时候我只想让内部的某个IP访问，其他的IP都转到另一个PHP上。如下:
访问test.php，且IP不等222.222.222.222的跳转到55555.php:
set $test '';
if ( $request_uri ~* /img/test.php ) {
set $test P;
}
if ( $http_x_forwarded_for !~* ^222\.222\.222\.222.* ) {
set $test "${test}C";
}
if ( $test = PC ) {  # 当条件符合 访问test.php并且 ip不是222.222.222.222的 转发到55555.php
rewrite ^(.*)$ /img/55555.php permanent;  
}
```



# 4. 其它配置

## 4.1 文件服务器

1. 安装 `vsftpd`：`yum install vsftpd -y`

2. `HTTP模块` 下新增配置：

   ```nginx
   autoindex	on;		# 开启索引功能
   autoindex_localtime	on;		# 显示本本机时间
   autoindex_exact_size	on;		#显示文件大小
   ```

3. `server`  下新增：

   ```nginx
   server {
   	listen	10001;				# 注意端口
   	server_name	localhost;
   
   	location / {
   		root	/data/images;		# 目录
   	}
   }
   ```

## 4.2 定时备份HTML

`01 00 * * * nginx_backup_html.sh`

```shell
#!/bin/bash
# nginx路径
NGINX_PATH=/data/nginx
# 获取昨天的日期
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
# 备份html目录
tar -cvf /data/backup/html-{$YESTERDAY}.tar.gz /data/nginx/html
# 移动备份文件到/data/backup
#mv /data/nginx/html-{$YESTERDAY}.tar.gz /data/backup/
```

## 4.3 统计Nginx访问IP

```shell
#!/bin/sh
##################################
# Date: 2023/03/28
# Author: cc
# Function: 统计Nginx上访问的IP地址
##################################

nginx_dir=/data/nginx/logs

cd ${nginx_dir}

# 统计 access.log/access-bitwarden.log/access-https.log

access_ip=`cat access.log|grep -vi 'uptime' | awk '{print $1}'|sort |uniq -c | sort -k1 -nr`

# 将IP地址写入

echo ${access_ip} > ${nginx_ip_dir}/access_ip_`date "+%F"`

```bash
## 解析 PHP

Nginx 要解析 PHP 文件，需要在 `Server{}` 下新增一个 `location`

```bash
location ~ \.php$ {
    root           html;
	# 根据端口/文件路径设置
    fastcgi_pass   unix:/var/run/php/php-fpm.sock;
    fastcgi_index  index.php;
    fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
    include        fastcgi_params;
}
```

```bash
vim /etc/php/7.4/fpm/pool.d/www.conf

user = nginx
group = nginx
listen.owner=nginx
listen.group=nginx
```

```bash
systemctl restart php7.4-fpm
nginx/sbin -s reload
echo "<?php phpinfo(); ?>" > nginx/html/phpinfo.php
```

如果出现:`No input file specified.`，需要在`php.ini`中添加路径：`open_basedir`

---

> 参考文档：
> gzip：https://blog.csdn.net/securitit/article/details/109104477
> RTMP服务器：https://blog.csdn.net/XuHang666/article/details/103290810
> RTMP服务器：https://blog.csdn.net/qq_38040638/article/details/120676351