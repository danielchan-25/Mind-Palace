---

title: "Redis"

date: 2024-02-12

---

![](/media/202303/2023-03-10_150708_7948300.14238269035577744.png)

# 简介
Redis 通常被称为数据结构服务器，因为值（value）可以是字符串(String)、哈希(Hash)、列表(list)、集合(sets)和有序集合(sorted sets)等类型。

**优势**

- 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
- 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
- 原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。
- 丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。


# 安装

## 服务端安装

> 下载地址: [redis](https://redis.io/download/)

### 编译安装

```shell
tar -xzvf redis-stable.tar.gz
cd redis-stable
make
make install
```

如果编译成功，您将在src目录中找到几个Redis二进制文件，包括：

- redis-server：Redis 服务器本身
- redis-cli是与 Redis 交互的命令行界面实用程序。

```shell
whereis redis-server	# 查看安装路径
```

### Docker 部署

```shell
docker pull redis
docker run --name my-redis-container -d redis
```

这将在 Docker 中创建一个名为 `my-redis-container` 的Redis容器并在后台运行。


现在，您可以使用Redis客户端连接到容器并开始使用Redis。运行以下命令以连接到Redis容器：

```shell
docker exec -it my-redis-container redis-cli
```

# 配置文件

```ini
# 修改守护进程
daemonize yes
# 当 Redis 以守护进程方式运行时，Redis 默认会把 pid 写入 /var/run/redis.pid 文件，可以通过 pidfile 指定
pidfile /var/run/redis.pid
# 如果想要设置指定IP连接redis，如果不限IP，将127.0.0.1修改成0.0.0.0即可
bind 0.0.0.0
# 修改端口号
port 6379
# 当客户端闲置多长秒后关闭连接，如果指定为 0 ，表示关闭该功能
timeout 300
# 指定日志记录级别，Redis 总共支持四个级别：debug、verbose、notice、warning，默认为 notice
loglevel notice
# 设置日志
logfile "redis.log"
# 数据库数量
databases 16
# 最大内存
maxmemory 512mb
# 指定本地数据库存放目录
dir ./
# 设置 Redis 连接密码，如果配置了连接密码，客户端在连接 Redis 时需要通过 AUTH <password> 命令提供密码，默认关闭
requirepass xxxxxxx
# 当 master 服务设置了密码保护时，slave 服务连接 master 的密码
masterauth <master-password>
```
## 数据类型
Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

### string 字符串
- string 是 redis 最基本的类型，一个 key 对应一个 value。
- string 类型是二进制安全的。意思是 redis 的 string 可以包含任何数据。比如jpg图片或者序列化的对象。
- string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。

```shell
# 增/改
## 新增键值对，语法：SET 键 值
127.0.0.1:6379> SET leon_age "18"
127.0.0.1:6379> GET leon_age
"18"
## 若键已存在，则修改值
127.0.0.1:6379> SET leon_age "26"
127.0.0.1:6379> GET leon_age
"26"
## 添加多个键值对
127.0.0.1:6379> MSET amy_height "149" amy_weight "45" amy_age "19"
## 追加值
127.0.0.1:6379> APPEND amy_weight "kg"
127.0.0.1:6379> GET amy_weight
"45kg"

# 查
## 查找键
127.0.0.1:6379> KEYS *
127.0.0.1:6379> KEYS leon_age
## 查看键值
127.0.0.1:6379> GET amy_height
## 批量查看键值
127.0.0.1:6379> MGET amy_height amy_weight amy_age
## 查看键值类型
127.0.0.1:6379> TYPE leon_age
string

# 删
## 删除键值
127.0.0.1:6379> DEL leon_age leon_age1 leon_age2

# exists：判断键是否存在，不存在返回0
127.0.0.1:6379> EXISTS leon_home
0
127.0.0.1:6379> EXISTS amy_height amy_age
2
127.0.0.1:6379> EXISTS amy_height amy_age amy_home
2

# 过期时间（单位为秒）
## 设置键值并添加过期时间，3秒后此键值消失
127.0.0.1:6379> SETEX leon_age 3 "44"
## 设置已有的键值并添加过期时间
### 语法：expire 键值 秒
127.0.0.1:6379> EXPIRE leon_age 3
## 查看键的有效时间
### 语法：ttl 键
127.0.0.1:6379> TTL leon_age
```
### HASH 哈希
- hash用于存“储键值”对集合；
- 每个hash中的键可以理解为字段（field），一个字段（field）对应一个值（value）；
- hash中的值（value）类型为字符串（string）；
- 同一个hash中字段名（field）不可重复。

```shell
# 添加hash
## 添加一个键leon，字段：age，值：48
127.0.0.1:6379> HSET leon_age "age" "48"
## 设置多个键值
127.0.0.1:6379> HMSET leon_weight "weight" "55kg"  leon_height "height" "177cm"
```
### List 列表
```shell
127.0.0.1:6379> lpush myname "!" "World" "Hello"
(integer) 3

127.0.0.1:6379> lrange myname 0 3
1) "Hello"
2) "World"
3) "!"
```
### Set 集合

## 参考文档
> https://blog.csdn.net/qq_43535322/article/details/118255933
> https://blog.csdn.net/qq_43535322/article/details/118255933