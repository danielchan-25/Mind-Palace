# MySQL

## 服务端安装

### 源码安装
> MySQL源码包下载地址：https://downloads.mysql.com/archives/community/

#### CentOS

> 下载地址：https://dev.mysql.com/downloads/mysql/5.7.html#downloads

1. 环境

```shell
yum install -y cmake make gcc gcc-c++ bison ncurses ncurses-devel libaio libaio-devel 
```

2. 添加用户和用户组

```shell
groupadd mysql
useradd -M -s /sbin/nologin -r -g mysql mysql
```

3. 开始安装

```shell
mv mysql-5.7/ /usr/local/mysql
cd /usr/local/mysql/bin

# 初始化 MySQL，务必记住初始化输出日志结尾的密码
## --datadir=数据存放目录
## --basedir=/usr/local/mysql=安装程序目录
./mysqld --initialize --user=mysql --datadir=/usr/local/mysql/data --basedir=/usr/local/mysql
```

4. 修改配置文件

```shell
vim /etc/my.cnf

[mysqld]
character_set_server=utf8
init_connect='SET NAMES utf8'
# 根据初始化命令填写
basedir=/usr/local/mysql
datadir=/usr/local/mysql/data
socket=/tmp/mysql.sock
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
```

5. 创建对应文件/目录，并赋予权限

```shell
mkdir -p /usr/local/mysql/data
touch /var/log/mysqld.log

mkdir -p /var/run/mysqld
touch /var/run/mysqld/mysqld.pid

chown -R mysql.mysql /usr/local/mysql
chown -R mysql.mysql /var/run/mysqld
chown -R mysql.mysql /var/log/mysqld.log

chmod 777 /var/log/mysqld.log
chmod 777 /var/run/mysqld/mysqld.pid
```

6. 启动服务并修改密码

```shell
/usr/local/mysql/support-files/mysql.server start

./bin/mysql -uroot -p

# 修改密码
ALTER USER 'root'@'localhost' IDENTIFIED BY 'mysql';
```

#### Ubuntu
操作系统：`Ubuntu 20.04 LTS`

![](/media/202309/2023-09-06_103654_1114900.4229205151838523.png)

```shell
# 这几个deb的下载地址：https://pkgs.org/
dpkg -i libmecab2_0.996-1.2ubuntu1_amd64.deb
dpkg -i libaio1_0.3.110-2_amd64.deb
dpkg -i libtinfo5_6.2-0ubuntu2_amd64.deb
```

```shell
#解压 mysql-server_5.7.41-1ubuntu18.04_amd64.deb-bundle.tar：
tar -xvf mysql-server_5.7.41-1ubuntu18.04_amd64.deb-bundle.tar
 
#依次执行以下命令进行安装：
dpkg -i mysql-common_5.7.41-1ubuntu18.04_amd64.deb
dpkg-preconfigure mysql-community-server_5.7.41-1ubuntu18.04_amd64.deb //这里需要输入数据库root的密码
dpkg -i libmysqlclient20_5.7.41-1ubuntu18.04_amd64.deb
dpkg -i libmysqlclient-dev_5.7.41-1ubuntu18.04_amd64.deb
dpkg -i libmysqld-dev_5.7.41-1ubuntu18.04_amd64.deb
dpkg -i mysql-community-client_5.7.41-1ubuntu18.04_amd64.deb
dpkg -i mysql-client_5.7.41-1ubuntu18.04_amd64.deb
dpkg -i mysql-common_5.7.41-1ubuntu18.04_amd64.deb
dpkg -i mysql-community-server_5.7.41-1ubuntu18.04_amd64.deb
dpkg -i mysql-server_5.7.41-1ubuntu18.04_amd64.deb
 
#检查MySQL的安装：
mysql -u root -p    //刚刚输入的密码
```

修改配置文件

```shell
vim /etc/mysql/mysql.conf.d/mysqld.cnf

datadir = /data/mysql
bind-address = 0.0.0.0
```

重启服务端
```shell
service mysql restart
```

#### MacOS

1. 使用 `brew` 安装。

   ```shell
   brew install mysql@5.7
   ```

2. 启动：

   ```shell
   brew services start mysql@5.7
   ```

### 服务端包管理安装

#### yum

```shell
# 查看是否已经安装 MySQL ，如果存在则使用 yum remove -y 包名 卸载
rpm -qa | grep -i mariadb
```

```shell
# 写入 Mariadb 软件库
vim /etc/yum.repos.d/MariaDB.repo
[mariadb]
name = MariaDB
baseurl = https://mirrors.cloud.tencent.com/mariadb/yum/10.4/centos7-amd64
gpgkey=https://mirrors.cloud.tencent.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1
```

```shell
# 安装 MySQL
yum -y install MariaDB-client MariaDB-server
systemctl start mariadb && systemctl enable mariadb
```
#### apt

```shell
# 查看有没有安装MySQL：
dpkg -l | grep mysql
# 安装MySQL：
apt install mysql-server
# 安装完成之后可以使用如下命令来检查是否安装成功：
netstat -tap | grep mysql
```
```shell
# 数据库重置
> mysql_secure_installation
Securing the MySQL server deployment.
Connecting to MySQL using a blank password.
VALIDATE PASSWORD PLUGIN can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD plugin? # 要安装验证密码插件吗?
Press y|Y for Yes, any other key for No: N # 这里我选择N
Please set the password for root here.
New password: # 输入要为root管理员设置的数据库密码
Re-enter new password: # 再次输入密码

By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.
Remove anonymous users? (Press y|Y for Yes, any other key for No) : y # 删除匿名账户
Success.

Normally, root should only be allowed to connect from
‘localhost’. This ensures that someone cannot guess at
the root password from the network.
Disallow root login remotely? (Press y|Y for Yes, any other key for No) : N # 禁止root管理员从远程登录，这里我没有禁止
… skipping.
By default, MySQL comes with a database named ‘test’ that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.

Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y # 删除test数据库并取消对它的访问权限
- Dropping test database…
Success.
- Removing privileges on test database…
Success.
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y # 刷新授权表，让初始化后的设定立即生效
Success.
All done!
```

## 客户端安装

## 服务端降级
MySQL 8 降级为： MySQL5.7，卸载完后，需要将以下目录删除：`cd /var/lib/mysql`

## 服务端安装报错
```shell
[root@localhost bin]# ./mysqld --initialize --user=mysql --datadir=/usr/local/mysql-5.7/data --basedir=/usr/local/mysql-5.7
2023-12-08T07:12:36.331949Z 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
2023-12-08T07:12:36.339463Z 0 [ERROR] --initialize specified but the data directory has files in it. Aborting.
2023-12-08T07:12:36.339559Z 0 [ERROR] Aborting
```
数据目录中已经存在文件，这是导致初始化失败的主要原因。只需把数据目录中的文件清空，重新执行即可：
```shell
rm -f /usr/local/mysql-5.7/data/*
```


## 服务端启动报错
```shell
[root@localhost mysql-5.7]# ./bin/mysql -uroot -p 
Enter password: 
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (111)
```
编译时没有指定 `sockect`，所以 mysql 连接时还是使用默认值 `/tmp/mysql.sock`，只需在 `/etc/my.cnf` 文件中，重新指定 `socket` 文件路径：

```ini
[mysqld]
#socket=/var/lib/mysql/mysql.sock
socket=/tmp/mysql.sock
```

# 服务器架构

## 主从架构

实验环境：

- 两台 MySQL 服务器

适用环境：一主一从/一主多从

**主库配置**

1. 修改 **主数据库** 的 `my.cnf` 文件
   1. 修改 *server-id* ，与从库不一致即可
   2. 添加：`log-bin=/usr/local/mysql/logs/mysql-bin.log`
   3. 指定 同步/不同步 的数据库
      1. 同步的数据库：`binlog_do_db=test binlog_do_db=test1`
      2. 不同步的数据库：`binlog_ignore_db=mysql`
   4. 其它
      1. 日志缓存时间：`expire_logs_days=10`
      2. 日志最大大小：`max_binlog_size=200M`
   5. 重启 MySQL
2. 创建用户
   1. 创建用户：`create user 'TEST'@'%' IDENTIFIED BY 'QWERasdf1234';`
   2. 赋予权限：`GRANT ALL ON *.* to 'TEST'@'%'';`
3. 查看主从状态：`show master status;`

**从库配置**

1. 配置从数据库

   ```mysql
   # master_log_file：主数据库的 show master status 命令下的 file 值
   # master_log_pos：主数据库的 show master status 命令下的 Position 值
   
   change master to \
   master_host='192.168.193.123', \
   master_port=3306, \
   master_user='save', \
   master_password='QWERasdf1234', \
   master_log_file='mysql-bin.000012', \
   master_log_pos=154;
   ```

2. 常用命令

   ```mysql
   # 启动/停止/重置
   start/stop slave;
   reset slave all;
   ```

---
> https://blog.csdn.net/checkjiji/article/details/131189893
>
> 安装教程：https://blog.csdn.net/qq_37973665/article/details/123390336
>
> 主从：https://www.cnblogs.com/Mr-shen/p/15936761.html
