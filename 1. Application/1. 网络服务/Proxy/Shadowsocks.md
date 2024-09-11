Shadowsocks 分为服务端与客户端，服务端用于给客户端代理。

# 服务端
本次展示的服务端为：shadowsocksR-b

## 部署

## 启动
```shell
# 启动 shadowsocks
/usr/bin/python3 /usr/local/bin/ssserver -c /etc/ssadmin/shadowsocks.json -d start
```

## 加速
由于国外VPS服务器与国内用户距离较远，连接线路错综复杂，在数据传输过程中的拥堵和丢包较为严重，从而造成连接速度极速下降，极大影响使用体验。

通过加速工具对网络加速处理后，可以明显改善网络传输速度，提升用户体验。
```shell
cd /root/
wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh" && chmod +x tcp.sh && ./tcp.sh
```

## 其它
1. 新建客户端

```shell
python3 mujson_mgr.py \
-a -u test_user -p 55000 \
-k Jr123321Jr \
-m aes-256-cfb -O auth_aes128_md5 \
-G 5 -o tls1.2_ticket_auth_compatible \
-s 500 -S 1000 -t 10 \
-f "25,465,233-266"
```

2. 查看当前客户端使用数量

```shell
netstat -anp |grep 'ESTABLISHED' |grep 'python' |grep 'tcp6' |awk '{print $4}' |sort -u |wc -l

>>> 1
```

3. 查看当前客户端的IP地址

```shell
netstat -anp |grep 'ESTABLISHED' |grep 'python' |grep 'tcp6' |awk '{print $5}' |awk -F ":" '{print $1}' |sort -u
>>> 58.62.203.188
```

4. 流量限制
已在创建 ssr 链接时限制，后期可修改。

5. MAC地址限制

使用防火墙的白名单，限制客户端MAC地址的通信，如：
```shell
# 阻止MAC地址为：B8:EE:65:DE:17:E3的设备所有通信
iptables -A INPUT -m mac --mac-source B8:EE:65:DE:17:E3 -j DROP

# 允许MAC地址为B8:EE:65:DE:17:E3主机访问 55000 端口：
iptables -A INPUT -p tcp --destination-port 55000 -m mac --mac-source B8:EE:65:DE:17:E3 -j ACCEPT
```
6. 访问限制

为防止访问色情、政治等网页，在服务器上做了 DNS 过滤 + 防火墙限制。

---
# 参考
> https://www.quchao.net/ShadowsocksR-User.html

> https://www.quchao.net/Shadowsocks-View.html

> https://github.com/Elder-Wu/SSServerDeviceLimit
