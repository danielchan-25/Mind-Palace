# OpenVPN
## 服务端部署
### 二进制包安装
> 参考地址：https://ubuntu.com/server/docs/service-openvpn

由于太复杂导致安装失败，故放弃

### 一键部署
> 开源地址：https://github.com/Nyr/openvpn-install

```bash
root@cc-ubuntu:/opt# bash Install-OpenVPN.sh
Welcome to this OpenVPN road warrior installer!

Which IPv4 address should be used?
     1) 192.168.2.10
     2) 192.168.122.1
     3) 172.17.0.1
     4) 172.20.0.1
IPv4 address [1]: 1

This server is behind NAT. What is the public IPv4 address or hostname?
Public IPv4 address / hostname [119.134.111.117]: abc.cn

Which protocol should OpenVPN use?
   1) UDP (recommended)
   2) TCP
Protocol [1]: 1

What port should OpenVPN listen to?
Port [1194]: 1194

Select a DNS server for the clients:
   1) Current system resolvers
   2) Google
   3) 1.1.1.1
   4) OpenDNS
   5) Quad9
   6) AdGuard
DNS server [1]: 1

Enter a name for the first client:
Name [client]: abc
...................................
```

等待最后的输出信息

```bash
Finished!

The client configuration is available in: /root/abc.ovpn
New clients can be added by running this script again.
```

将 `/root/abc.ovpn` 导出存放，客户端连接需要使用。

## 客户端使用
### Windows

> 客户端下载地址：https://openvpn.net/community-downloads/

下载客户端后，导入以上的 `abc.ovpn` 文件后即可。


![](/media/202306/2023-06-13_132000_5357670.6487410347898129.png)