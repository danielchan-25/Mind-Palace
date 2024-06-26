---
title: "ApacheBench"
date: 2024-04-20

---

# 原理
ab命令会创建多个并发访问线程，模拟多个访问者同时对某一URL地址进行访问。它的测试目标是基于URL的，因此，它既可以用来测试apache的负载压力，也可以测试nginx、lighthttp、tomcat、IIS等其它Web服务器的压力。
ab命令对发出负载的计算机要求很低，它既不会占用很高CPU，也不会占用很多内存。但却会给目标服务器造成巨大的负载，其原理类似CC攻击。自己测试使用也需要注意，否则一次上太多的负载。可能造成目标服务器资源耗完，严重时甚至导致死机。

#  测试指标
在进行性能测试过程中有几个指标比较重要：
- TPS吞吐量：请求数/请求响应的时间(s) ，即每秒请求数，对应 Request per second一项，tps=13.24 req/s
- 响应时间：请求发送到接受到请求的时间差，单位为ms，一般看90%的响应时间，此时RT=862ms
- 并发连接数：每秒服务器端能处理的连接数。并发连接数 = 吞吐量*响应时间，并发连接数=11.4 req
- PV:Page View网页的浏览次数,或者点击量
- UV:Unique Visitor,一台ip地址为一个访客。00:00-24:00内相同的客户端只被计算一次
- 峰值QPS:每天80%的访问集中在20%的时间里，这20%时间叫做峰值时间
( 总PV数 * 80% ) / ( 每天秒数 * 20% ) = 峰值时间每秒请求数(QPS)
- 峰值机器数：保证机器数量抗住峰值QPS，机器数 = 峰值QPS/单台机器QPS

# QPS和TPS有什么区别？
TPS是每秒处理的请求数，是统计每秒用户的请求次数。QPS是每秒处理的查询次数，是统计每秒对于服务器查询的次数。用户一次请求，tps+1，而可能该请求中对应3次服务器查询次数，则qps+3。
例如输入一个url，返回html内容，对应查询服务器一次，而有可能在html中再次出现一个url，还需查询同样的服务器一次，则此时QPS>TPS。
二、每天300w PV 的在单台机器上，这台机器需要多少QPS？如果一台机器的QPS是58，需要几台机器来支持？

( 3000000 * 0.8 ) / (86400 * 0.2 ) = 139 (QPS)
139 / 58 = 3

# 安装

```shell
# 安装 apache bench
yum -y install httpd-tools
ab -V
```

# 使用
```shell
ab -r -c 1000 -n 300000 "http://172.22.4.24/api/liveRoom/listRoomInfoByIds.action?ids=54&sys=szplus”
```

## 命令参数
```shell
-A auth-username:password    向服务器提供基本认证信息。用户名和密码之间":"分割，以base64编码形式发送。无论服务器是否需要(即是否发送了401)都发送。 

-b windowsize    TCP发送/接收缓冲区大小，以字节为单位。

-c concurrency    并发数，默认为1。

-C cookie-name=value    添加Cookie。典型形式是name=value对。name参数可以重复。 

-d不显示"percentage served within XX [ms] table"消息(兼容以前的版本)。 

-e csv-file    输出百分率和对应的时间，格式为逗号份额的csv。由于这种格式已经"二进制化"，所以比"gnuplot"格式更有用。

-f protocol    SSL/TLS protocol (SSL2, SSL3, TLS1, 或ALL).

-g gnuplot-file    把所有测试结果写入"gnuplot"或者TSV(以Tab分隔)文件。该文件可以方便地导入到Gnuplot, IDL, Mathematica甚至Excel中，第一行为标题。

-h    显示使用方法。

-H custom-header    附加额外头信息。典型形式有效的头信息行，包含冒号分隔的字段和值(如："Accept-Encoding: zip/zop;8bit")。

-i    执行HEAD请求，而不是GET 。

-k    启用KeepAlive功能，即在HTTP会话中执行多个请求。默认关闭。

-n requests    会话执行的请求数。默认为1。 

-p POST-file    附加包含POST数据的文件。注意和-T一起使用。

-P proxy-auth-username:password    代理认证。用户名和密码之间":"分割，以base64编码形式发送。无论服务器是否需要(即是否发送了407)都发送。

-q    quiet，静默模式。不在stderr输出进度条。

-r    套接字接收错误时不退出。

-s timeout     超时，默认为30秒。

-S    不显示中值和标准偏差值，而且在均值和中值为标准偏差值的1到2倍时，也不显示警告或出错信息。默认显示最小值/均值/最大值。(兼容以前的版本)-t timelimit
    测试进行的最大秒数。内部隐含值是"-n 50000"。默认没有时间限制。

-T content-type    POST/PUT的"Content-type"头信息。比如“application/x-www-form-urlencoded”，默认“text/plain”。

-v verbosity    详细模式，4以上会显示头信息，3以上显示响应代码(404，200等)，2以上显示告警和info。

-V    显示版本号并退出。

-w    以HTML表格形式输出。默认是白色背景的两列。

-x <table>-attributes    设置<table>属性。此属性填入<table 这里 > 。

-X proxy[:port]    使用代理服务器。

-y <tr>-attributes    设置<tr>属性。

-z <td>-attributes    设置<td>属性。 

-Z ciphersuite    设置SSL/TLS加密
```



---
> https://cloud.tencent.com/developer/article/1635288
> https://www.cnblogs.com/myvic/p/7703973.html
> https://blog.csdn.net/vainfanfan/article/details/90176481
> https://www.cnblogs.com/zhengah/p/4334314.html