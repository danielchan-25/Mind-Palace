# Nginx

Nginx 分为源码编译安装、包管理器安装、Docker容器安装

> 源码包下载地址：https://nginx.org/

## 1. 程序安装

### 1.1 源码编译安装

源码编译需要先安装依赖以下基础模块：

- Pcre：是一套兼容 Perl 的正则表达式库，Nginx 中的 PCRE 是指使用 PCRE 正则表达式语法的模块。
- Zlib：
- OpenSSL

安装完成后，就可以执行以下安装步骤了：

```shell
# 最好不要使用 Root 用户运行 Nginx
useradd nginx -s /sbin/nologin -M

tar -xvf nginx-1.22.1.tar.gz
cd nginx-1.22.1/

# 注意路径
./configure --prefix=/data/nginx \
--with-pcre=/opt/pcre-8.45 \
--with-zlib=/opt/zlib-1.2.13 \
--with-openssl=/opt/openssl-1.1.1s

# 注意：./configure --with-pcre=指向的是pcre安装包的目录，非pcre安装的路径
```

### 1.2 包管理器安装

#### 1.2.1 CentOS
```shell
yum update -y
yum install -y make gcc gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel
yum install epel-release -y
yum install nginx -y
```

#### 1.2.2 Ubuntu
```shell
apt install nginx -y
```

### 1.3 Docker容器安装

1. 本地创建目录

```shell
mkdir nginx/html
mkdir nginx/conf/
mkdir nginx/conf.d
mkdir nginx/logs

touch nginx/conf/nginx.conf
touch nginx/conf.d/default.conf
```

2. 编写配置文件：`vim nginx/conf/nginx.conf`

```nginx
user  nginx;
worker_processes  auto;
error_log  /var/log/nginx/error.log notice;
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
	keepalive_timeout  65;
	gzip  on;
	include /etc/nginx/conf.d/*.conf;
}
```

3. 编写配置文件：`vim nginx/conf.d/defalut.conf`

```nginx
server {
	listen       80;
	listen  [::]:80;
	server_name  localhost;

	location / {
		root   /usr/share/nginx/html;
		index  index.html index.htm;
	}

	error_page  404              /404.html;
	error_page   500 502 503 504  /50x.html;

	location = /50x.html {
		root   /usr/share/nginx/html;
	}
}
```

4. 安装

```shell
docker run --name nginx -p 8080:80 \
-v ./nginx/html/:/usr/share/nginx/html/ \
-v ./nginx/conf/nginx.conf:/etc/nginx/nginx.conf \
-v ./nginx/conf.d:/etc/nginx/conf.d \
-v ./nginx/logs:/var/log/nginx \
-d nginx
```

## 2. 模块安装

### 2.1 正则表达式：Pcre

PCRE 提供了强大的正则表达式功能，支持正则表达式分组、捕获、回溯引用、零宽断言等特性，可以用于匹配、搜索、替换、分割字符串等操作。在 Nginx 中，PCRE 主要用于地址重写模块、反向代理模块、限制模块等模块中，通过正则表达式匹配、替换、转发请求。

Nginx 中使用 PCRE 的主要优点包括：

1. 支持 Perl 正则表达式语法：PCRE 是一套兼容 Perl 的正则表达式库，具有丰富的正则表达式特性和语法，可以方便地处理各种复杂的字符串匹配问题。
2. 支持高效的正则表达式引擎：PCRE 提供了高效的正则表达式引擎，能够快速地处理大规模的字符串匹配操作。
3. 支持广泛的平台和语言：PCRE 支持在多种平台和语言中使用，包括 C、C++、Java、PHP、Python 等，能够方便地进行跨平台开发和集成。

需要注意的是，在使用 PCRE 进行正则表达式匹配时，需要注意正则表达式的复杂度和性能影响，避免出现性能瓶颈和安全漏洞。

> 官网地址：https://www.pcre.org/

```bash
# 源码安装
wget https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.40/pcre2-10.40.tar.gz
tar -xvf pcre2-10.40.tar.gz
cd pcre2-10.40
./configure --prefix=/usr/local/pcre-10.4
make && make install
```

```bash
# apt 安装
apt install build-essential libtool libpcre3-dev libpcre3
```

**使用说明**

```sh
^ ：匹配输入字符串的起始位置
$ ：匹配输入字符串的结束位置
* ：匹配前面的字符零次或多次。如“ol*”能匹配“o”及“ol”、“oll”
+ ：匹配前面的字符一次或多次。如“ol+”能匹配“ol”及“oll”、“olll”，但不能匹配“o”
? ：匹配前面的字符零次或一次，例如“do(es)?”能匹配“do”或者“does”，”?”等效于”{0,1}”
. ：匹配除“\n”之外的任何单个字符，若要匹配包括“\n”在内的任意字符，请使用诸如“[.\n]”之类的模式
\ ：将后面接着的字符标记为一个特殊字符或一个原义字符或一个向后引用。如“\n”匹配一个换行符，而“\$”则匹配“$”
\d ：匹配纯数字
{n} ：重复 n 次
{n,} ：重复 n 次或更多次
{n,m} ：重复 n 到 m 次
[] ：定义匹配的字符范围
[c] ：匹配单个字符 c
[a-z] ：匹配 a-z 小写字母的任意一个
[a-zA-Z0-9] ：匹配所有大小写字母或数字
() ：表达式的开始和结束位置
| ：或运算符
```

### 2.2 Zlib

> 官网地址：http://www.zlib.net/

```bash
# 源码安装
wget http://www.zlib.net/zlib-1.2.13.tar.gz
tar -xvf zlib-1.2.13.tar.gz
cd zlib-1.2.13
./configure --prefix=/usr/local/zlib-1.2.13
make && make install
```

### 2.3 通信加密：Openssl

Nginx 使用 OpenSSL 的主要优点包括：

1. 安全性强：OpenSSL 提供了可靠的加密和解密机制，能够有效保护客户端和服务端之间的数据安全。
2. 高效性能：OpenSSL 提供了高效的加密和解密算法，能够快速地处理大量的数据流量。
3. 可靠稳定：OpenSSL 是一个经过长期测试和验证的开源软件库，稳定性和可靠性较高，能够满足大规模的生产环境需求。

需要注意的是，在使用 OpenSSL 时，需要及时升级和更新版本，以防止出现安全漏洞和攻击。此外，还需要配置 SSL 证书和密钥等相关参数，确保 HTTPS 通信的正确性和安全性。

> 官网地址：https://www.openssl.org/source/

```bash
# 源码安装
wget https://www.openssl.org/source/openssl-3.0.7.tar.gz
tar -xvf openssl-3.0.7.tar.gz
cd openssl-3.0.7
./config --prefix=/usr/local/openssl
make && make install
```

### 2.4 重新添加模块步骤

1. 先使用 `nginx -V` 命令，查看现有的模块。
2. 使用相同版本的 Nginx 源码包文件，按编译安装的步骤进行，命令：`./configure --add-module=/path/to/your/module/source`
3. 但在执行完 `make` 命令后立马停止，**不要执行 `make install` 命令**，否则就覆盖安装了。
4. 执行完 `make` 命令后，在源码包下会生成一个文件：`objs/nginx` 
5. 这个可执行的 `nginx` 就是新编译出来的文件，可替换原 `sbin/nginx` 
6. 执行 `nginx -V` 即可查看编译的模块。

### 2.5 常用模块

#### 2.5.1 状态模块

模块名称：**http_stub_status_module**

功能介绍：启用 `nginx` 的 `NginxStatus` 功能，监控 `Nginx` 的当前状态

`location /status { stub_status on; }`

访问：`/status` 

- `Active connections` ：活动连接数

- `Server accepts handled requests`：总共处理的连接数、成功握手的连接数量，处理的请求数（正常情况下握手和连接数是相等的，表示没有丢失）

- `Reading`：读取到客户端的`Header`信息数

- `Writing`：返回给客户端的`Header`信息数

- `Waiting`：开启`keep-alive`的情况下,这个值等于 `active – (reading + writing)`，意思就是`Nginx`已经处理完成,正在等候下一次请求指令的驻留连接（在`nginx`开启了`keep-alive`,也就是长连接的情况下，客户端跟服务端建立了连接但是没有读写操作的空闲状态）

#### 2.5.2 地址重写

获得一个来访的URL请求，然后改写成服务器可以处理的另一个URL，也就是地址栏被重写。
优点：缩短URL，隐藏实际路径提高安全性，易于用户记忆和键入，易于被搜索引擎收录

> http://jd123.com ---> http://jd.com

支持地址重写的模块有以下三个：

1. `ngx_http_rewrite_module`：这是 Nginx 的默认地址重写模块，提供了丰富的地址重写功能，可以根据 URL 匹配规则对请求进行重写、重定向、反向代理等操作。
2. `ngx_http_proxy_module`：这是 Nginx 的反向代理模块，可以实现将请求转发到后端服务器进行处理，同时还可以进行地址重写、负载均衡等操作。
3. `ngx_http_map_module`：这是 Nginx 的映射模块，可以实现将一些特定的 URL 映射为另一个 URL，或根据 URL 中的参数值进行不同的处理。它可以用来简化复杂的地址重写规则，提高配置的可读性和可维护性。

使用说明： `rewrite` 参数，可以放在`server{}`, ` if{}`, `location{}`段中

#### 2.5.3 白/黑名单模块

模块名称：`ngx_http_access_module`

功能介绍：允许限制某些IP地址的客户端访问，也可以通过密码来限制访问。

可以在 `http` 下新增 `include whitelist;`，在 `conf` 下新增这样一个文件写入白/黑明单即可。

```nginx
location / {
	deny 192.168.1.1;
	allow 192.168.1.0/24;
	allow 192.168.2.0/24;
	deny all;
}
```

#### 2.5.4 身份认证

模块名称：`ngx_http_auth_basic_module`

功能介绍：Nginx 内置的 HTTP 认证模块，用于对客户端请求进行基于 HTTP 的身份验证。该模块可以使得通过 Nginx 访问的资源进行身份认证，只有在客户端提供正确的用户名和密码时，才会允许客户端访问该资源。

安装步骤：

1. `ngx_http_auth_basic_module` 是 Nginx 内置的 HTTP 认证模块，通常情况下已经包含在 Nginx 的源代码中，无需单独安装。
2. 如果您使用的是预编译的 Nginx 软件包，可能需要安装包含该模块的 Nginx 软件包或重新编译 Nginx 并在编译选项中启用该模块。

```bash
apt install build-essential libpcre3 libpcre3-dev zlib1g-dev libssl-dev

./configure --with-http_ssl_module --with-http_v2_module --with-http_auth_request_module
# --with-http_ssl_module 表示启用 SSL 功能
# --with-http_v2_module 表示启用 HTTP/2 功能
# --with-http_auth_request_module 表示启用 ngx_http_auth_basic_module 模
```

Nginx 安装完模块后，还需安装一个工具：`htpasswd`

`htpasswd` 是 Apache HTTP Server 项目提供的命令行工具，用于管理 HTTP 认证的用户和密码。

```bash
# Ubuntu
apt update
apt install apache2-utils
```

```bash
# CentOS
yum update
yum install httpd-tools
```

使用说明：

1. 在 `http` 块中定义一个认证域，用于指定客户端在输入用户名和密码时将要看到的提示信息。

```nginx
http {
	...
	auth_basic "Restricted Area";
	...
}
```

2. 在需要进行身份验证的 `location` 块中启用 `auth_basic` 指令，并指定一个认证文件。

```nginx
location /protected {
	auth_basic "Restricted Area";
	auth_basic_user_file /path/to/.htpasswd;
}

# /protected 是需要进行身份验证的资源路径
# auth_basic_user_file 指令用于指定存储用户名和密码的文件路径
# /path/to/.htpasswd 是存储用户名和密码的文件路径，该文件需要使用 htpasswd 工具生成，username 是需要进行身份验证的用户名
htpasswd -c /path/to/.htpasswd username
```

3. 当客户端访问 `/protected` 资源时，会弹出一个对话框，要求客户端输入用户名和密码，输入正确的用户名和密码后才能访问该资源。如果输入的用户名和密码不正确，客户端将会收到一个 401 Unauthorized 的响应。

#### 2.5.5 压缩

Nginx 提供了多种压缩模块，可以用于对 HTTP 数据进行压缩和解压缩，主要包括以下几个模块：

1. `ngx_http_gzip_module`：该模块用于实现 GZIP 压缩功能，即对 HTTP 响应的数据流进行 GZIP 压缩，从而减少数据传输的大小，提高响应速度。
2. `ngx_http_brotli_filter_module`：该模块用于实现 Brotli 压缩功能，即对 HTTP 响应的数据流进行 Brotli 压缩，可以进一步减少数据传输的大小，提高响应速度。
3. `ngx_http_deflate_module`：该模块用于实现 Deflate 压缩功能，即对 HTTP 响应的数据流进行 Deflate 压缩，可以减少数据传输的大小，但与 GZIP 和 Brotli 相比，性能和压缩比略低。
4. `ngx_http_gunzip_module`：该模块用于实现 GZIP 解压缩功能，即对 HTTP 请求中的 GZIP 压缩数据进行解压缩，从而得到原始的数据流。
5. `ngx_http_brotli_static_module`：该模块用于实现 Brotli 静态压缩功能，即对 Nginx 服务器上的静态资源进行 Brotli 压缩，并将压缩后的文件缓存到本地磁盘，从而减少磁盘空间和网络带宽的消耗。

需要注意的是，使用压缩模块时，需要根据实际情况选择适合的压缩算法和配置参数，避免出现性能瓶颈和数据丢失的问题。此外，还需要注意压缩和解压缩算法的兼容性和安全性，避免出现安全漏洞和攻击。

以`ngx_http_gzip_module`为例：

是 Nginx 自带的模块之一，通常情况下已经包含在 Nginx 的源码中，可以直接通过编译安装 Nginx 时开启该模块。

```bash
./configure --with-http_gzip_static_module=/path
# 可以替换为你实际安装 ngx_http_gzip_module 的位置
```

**使用说明**

```nginx
gzip on;
gzip_min_length 1k;
gzip_buffers 16 64k;
gzip_http_version 1.1;
gzip_comp_level 6;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml
application/xml+rss text/javascript;
gzip_vary on;

# 开启 Gzip 压缩功能
# 设置需要压缩的最小文件大小，小于该值的文件不会被压缩
# 设置压缩缓冲区大小，第一个参数表示缓冲区数量，第二个参数表示缓冲区大小
# 限制 Gzip 压缩功能只在 HTTP/1.1 协议中生效
# 设置 Gzip 压缩级别，取值范围为 1~9，值越大压缩比越高，但消耗的 CPU 资源也越多
# 设置需要压缩的 MIME 类型
# 在 HTTP 响应头中添加 Vary: Accept-Encoding，告知客户端已对响应进行了 Gzip 压缩
```

#### 2.5.6 RTMP服务器

模块名称：`nginx-rtmp-module`

> 下载地址：https://github.com/arut/nginx-rtmp-module

功能说明：可以提供简单的 `RTMP` 服务

使用说明：在与 `http` 同级下编写配置：

```nginx
rtmp {
        server {
                listen  41001;
                chunk_size      4096;
                application live {
                        live    on;
                        hls     on;
                        hls_path        /tmp/hls;
                        hls_fragment    15s;
                        pull    rtmp://169.vgemv.com:8800/push/720p7?vhost=tv_live;
                }
        }
}
http {
    ...
}
```

- Server：标识为一个服务
- listen：监听端口
- chunk_size：流复用块的大小，值越大cpu消耗越低
- application：每一个应用的名称，此处不支持正则匹配
- live：当on时表示开启实时（相当于直播）
- hls：当on时表示开启把一段视频流，分成一个个小的基于HTTP的文件来下载
- hls_path：生成的视频slice切片临时目录
- hls_fragment：每一个切片的长度
- pull：去其他流媒体服务器拉流，相当于nginx http模块中的proxy_pass功能 
- push：推流到其他流媒体服务器与pull作用相似

上面配置文件中，pull了一个 `rtmp` ，可以直接在 VLC 播放器中播放此地址。