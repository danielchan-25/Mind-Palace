---
title: "PHP"

---

> 源码包下载: [php](https://www.php.net/releases/)

# 包管理器安装
## Apt 安装

```shell
apt install php
ps -ef | grep php
```

## Yum 安装

```shell
# 安装 epel-release
rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

# 安装 PHP7 的 rpm 源
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

# 安装PHP7
yum install php70w
```

# 源码安装

```shell
# 依赖安装
yum install -y \
libxml2 libxml2-devel \
openssl openssl-devel \
bzip2 bzip2-devel \
libcurl libcurl-devel \
libjpeg libjpeg-devel jpeg6 \
libpng libpng-devel \
freetype freetype-devel \
gmp gmp-devel \
libmcrypt libmcrypt-devel \
readline readline-devel \
libxslt libxslt-devel \
libtool sqlite-devel\
php-bcmath php-mbstring \
php-gd php-xml
```

```shell
# 编译参数：
# https://www.php.net/manual/zh/migration74.other-changes.php#migration74.other-changes.pkg-config
tar -xvf php7.tar.gz
cd php-7.0.4

./configure \
--prefix=/usr/local/php-7.4.0 \
--with-config-file-path=/etc \
--with-fpm-user=nginx \
--with-fpm-group=nginx \
--enable-fpm \
--enable-calendar \
--enable-bcmath \
--enable-inline-optimization \
--enable-dom \
--enable-gd-native-ttf \
--enable-gd-jis-conv \
--enable-exif \
--enable-fileinfo \
--enable-filter \
--enable-ftp \
--enable-gd \
--enable-shared \
--enable-soap \
--enable-json \
--enable-mbstring \
--enable-mbregex \
--enable-session \
--enable-shmop \
--enable-simplexml \
--enable-sockets \
--enable-sysvmsg \
--enable-sysvsem \
--enable-sysvshm \
--enable-wddx \
--enable-mbregex-backtrack \
--enable-mysqlnd-compression-support \
--enable-pdo \
--enable-opcache \
--disable-debug \
--disable-rpath \
--with-libxml-dir \
--with-xmlrpc \
--with-openssl=/data/software/openssl-1.1.1s/ \
--with-mcrypt \
--with-mhash \
--with-sqlite3 \
--with-zlib=/data/software/zlib-1.2.13/ \
--with-zlib-dir=/data/software/zlib-1.2.13/ \
--with-iconv \
--with-bz2 \
--with-curl \
--with-cdb \
--with-openssl-dir \
--with-jpeg=/usr/include \
--with-freetype=/usr/include/freetype2/ \
--with-gettext \
--with-gmp \
--with-mhash \
--with-libmbfl \
--with-onig \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
--with-pdo-sqlite \
--with-readline \
--with-libxml-dir \
--with-xsl \
--with-pear

# 根据报错查看对应的模块安装
make -j4
make install -j4
```

```shell
# 添加环境变量
echo 'export PATH=$PATH:/usr/local/php/bin' >> /etc/profile
source /etc/profile

# 配置php-fpm
cp php.ini-production /etc/php.ini
cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf
cp /usr/local/php/etc/php-fpm.d/www.conf.default /usr/local/php/etc/php-fpm.d/www.conf
cp sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm
chmod +x /etc/init.d/php-fpm

# 启动
/etc/init.d/php-fpm start
```