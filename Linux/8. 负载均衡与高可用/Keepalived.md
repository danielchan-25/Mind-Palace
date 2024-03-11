# Keepalived

# 简介

keepalived 是集群管理中保证集群高可用的一个服务软件，其功能类似于 heartbeat，用来防止单点故障。

keepalived是以VRRP协议为实现基础的。

VRRP全称Virtual Router Redundancy Protocol，即虚拟路由冗余协议。

虚拟路由冗余协议，可以认为是实现路由器高可用的协议，即将N台提供相同功能的路由器组成一个路由器组。

这个组里面有一个master和多个backup，master上面有一个对外提供服务的vip（该路由器所在局域网内其他机器的默认路由为该vip），master会发组播，当backup收不到vrrp包时就认为master宕掉了，这时就需要根据VRRP的优先级来选举一个backup当master。这样的话就可以保证路由器的高可用了。

keepalived主要有三个模块，分别是 core、check 和 vrrp。

- core模块为keepalived的核心，负责主进程的启动、维护以及全局配置文件的加载和解析。
- check负责健康检查，包括常见的各种检查方式。
- vrrp模块是来实现VRRP协议的。

# 配置文件

keepalived 只有一个配置文件 `keepalived.conf`

里面主要包括以下几个配置区域，分别是

- global_defs
- static_ipaddress
- static_routes
- vrrp_script
- vrrp_instance
- virtual_server

## global_defs

主要是配置故障发生时的通知对象以及机器标识

```shell
global_defs {
   # notification_email：故障发生时给谁发邮件
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   
   # notification_email_from：通知邮件从哪个地址发出
   notification_email_from Alexandre.Cassen@firewall.loc
   
   # smtp_server：通知邮件的smtp地址
   smtp_server 192.168.200.1
   
   # smtp_connect_timeout：连接smtp服务器的超时时间
   smtp_connect_timeout 30
   
   # router_id：标识本节点的字条串，通常为 hostname，故障发生时会用到
   router_id LVS_DEVEL
   
   # enable_traps：开启SNMP陷阱
   enable_traps
   vrrp_skip_check_adv_addr
   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}
```

## static_ipaddress

配置本节点的IP。

如果机器上已经配置了IP，那么这个区域不用配置。

一般情况下机器都会有IP地址，所以没必要配置。

## static_routes

配置本节点的路由。

如果机器上已经配置了路由，那么这个区域不用配置。

一般情况下机器都会有路由地址，所以没必要配置。

## vrrp_script

用来做健康检查，当检查失败时会将 `vrrp_instance` 的 `priority` 减少相应的值。

## vrrp_instance

定义对外提供服务的 VIP 区域及其相关属性。

```shell
vrrp_instance VI_1 {
		# state 可以是 MASTER/BACKUP
    state MASTER
    
    # 节点固有IP（非VIP）的网卡
    interface ens160
    
    # 用来区分多个 intance，取值（1～255），master与backup节点需要一致，但同一网段中不能重复
    virtual_router_id 51
    
    # 用来选举 MASTER 的，如果要成为 MASTER，最好高于其它机器 50 个点 （1～255）
    priority 100
    
    # 发送 VRRP 包的时间间隔
    advert_int 1
    
    # 认证区域，推荐 PASS
    authentication {
        auth_type PASS	# 鉴权，默认通过
        auth_pass 1111	# 鉴权访问密码
    }
    virtual_ipaddress {
        192.168.200.16	# 虚拟 IP
        192.168.200.17
        192.168.200.18
    }
}
```

## vrrp_sync_group

定义`vrrp_intance`组，使得这个组内成员动作一致。

例如：两个 `vrrp_intance` 属于同一个 `vrrp_sync_group` ，那么其中一个 `vrrp_intance` 发生故障切换时，另一个 `vrrp_intance` 也会切换（即使这个无故障）

# 安装部署

> 官网：https://www.keepalived.org
>
> 下载地址：https://www.keepalived.org/download.html

```bash
wget https://www.keepalived.org/software/keepalived-2.2.7.tar.gz
tar -xvf keepalived-2.2.7.tar.gz
cd keepalived-2.2.7
./configure --prefix=/usr/local/keepalived
make
make install
```
# 常用命令
```shell
# 启/停命令
# -D：详细日志信息
# -f：指定配置文件
./sbin/keepalived -D -f ./etc/keepalived/keepalived.conf

killall keepalived
```

# 实战项目

项目名称：Keepalived + Nginx

实验环境

操作系统：ubuntu20.04 LTS x2

serverA：10.211.55.22（MASTER）

serverB：10.211.55.23（BACKUP）

VIP：10.211.55.50（虚拟IP）

## Nginx 配置

两台服务器都安装 Nginx

```sh
apt install nginx -y
```

将本机 IP 写入 index.html，便于区分

```sh
echo "10.211.55.22" > index.html
echo "10.211.55.23" > index.html
```

## Keepalived 配置

### serverA 配置

```yml
global_defs {
        router_id       master
}
vrrp_script check_nginx {
        script  "/usr/local/keepalived/check_nginx.sh"
        interval        2
        weight  2
}
vrrp_instance VI_1 {
        state   MASTER
        interface       eth0
        mcast_src_ip    10.211.55.22
        virtual_router_id       50
        priority        100
        advert_int      1
        authentication  {
                auth_type       PASS
                auth_pass       1111
        }
        virtual_ipaddress {
                10.211.55.50
        }
}
```

### serverB配置

```yml
global_defs {
        router_id       backup
}
vrrp_script check_nginx {
        script  "/usr/local/keepalived/check_nginx.sh"
        interval        2
        weight  2
}
vrrp_instance VI_1 {
        state   BACKUP
        interface       eth0
        mcast_src_ip    10.211.55.23
        virtual_router_id       50
        priority        50
        advert_int      1
        authentication  {
                auth_type       PASS
                auth_pass       1111
        }
        virtual_ipaddress {
                10.211.55.50
        }
}
```

出现问题：

当 Nginx 宕机或整个机子宕机后，Keepalived仍在启动，所以无法进行自动切换。

所以为了解决上一问题，可以利用脚本，当检测到 nginx 进程宕掉后，自动关闭 keepalived 进程，从而实现热备份。

脚本

```sh
#!/bin/bash
A=`ps -C nginx --no-header |wc -l`
if [ $A -eq 0 ]
then
    echo 'nginx server is died'
    sudo killall keepalived
fi
```

## 测试

查看 MASTER 的 ip 地址，发现有 10.211.55.50 ，成功

访问 10.211.55.50，得出是 MASTER 的网页，成功

kill 掉 10.211.55.50 的 Nginx，keepalived 也关闭了，此时访问到了 BACKUP 的 Nginx，成功。

参考文档

> https://blog.csdn.net/ebdbbd/article/details/126402572
