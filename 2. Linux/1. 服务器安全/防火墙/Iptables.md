---
title: "Iptables"
date: 2021-02-12

---

`iptables` 默认维护着四个表和五个链。

## 四表
**“四表”**是指 `iptables` 以下四张表：

1. **filter表**：过滤规则表，控制数据包是否允许进出及转发，可以控制的链路有 `INPUT、FORWARD、OUTPUT`

2. **nat表**：地址转换规则表，控制数据包中地址转换，可以控制的链路有 `PREROUTING、INPUT、OUTPUT、POSTROUTING`。

3. **mangle表**：修改数据标记位规则表，修改数据包中的原数据，可以控制的链路有 `PREROUTING、INPUT、OUTPUT、FORWARD、POSTROUTING`。

4. **raw表**：跟踪数据表规则表，控制 nat 表中连接追踪机制的启用状况，可以控制的链路有 `PREROUTING、OUTPUT`。

## 五链

**“五链”**是指内核中控制网络的 NetFilter 定义的 5 个规则链。每个规则表中包含多个数据链

1. INPUT（入站数据过滤）

2. OUTPUT（出站数据过滤）

3. FORWARD（转发数据过滤）

4. PREROUTING（路由前过滤）

5. 和POSTROUTING（路由后过滤）

# 安装

```shell
# CentOS
yum -y install iptables iptables-services
systemctl start iptables && systemctl enable iptables
```

# 使用

```shell
# 语法
iptables [-t table] command [match] [target]
iptables [-t 表名] <-A|I|D|R> 链名 [规则编号] [-i|o 网卡名称] [-p 协议类型] [-s 源ip|源子网] [--sport 源端口号] [-d 目的IP|目标子网] [--dport 目标端口号] [-j 动作]

# -t： 用于指定所要操作的表，不指定则默认 filter 表
# command：具体的命令动作，比如对指定链添加/删除规则
# match：对所要处理包的匹配规则
# target：数据包的处理动作
# 大小写敏感
```

### command
每个链由一条条的规则组成，对于一个链可以添加规则、删除规则、检测是否存在该条规则等操作，相应的命令选项如下：

| 命令 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| -A   | iptables -A chain rule-specification 在指定链表chain末尾添加规则 |
| -C   | iptables -C chain rule-specification 检测是否存在该规则      |
| -D   | iptables -D chain rule-specification 删除指定规则，需要将规则完整的写出来 |
| -D   | iptables -D chain rulenum 删除指定规则序号对应的那条规则，上面的rulenum 可通过 iptables -L –line-numbers 显示，每个链表的第一条规则对应序号1 |
| -I   | iptables -I chain [rulenum] rule-specification 向指定链表的对应规则序号前面插入规则，如果不指定 rulenum，则默认是序号1 |
| -R   | iptables -R chain rulenum rule-specification 替换规则        |
| -L   | iptables -L [chain] 显示所有的规则，一般紧跟使用-n 选项，避免转换成主机名形式；跟-v选项可以看更详细的信息。默认显示所有链（[] 中括号表示该参数是可选的） |
| -S   | iptables -S [chain] 显示所有的规则                           |
| -F   | iptables -F [chain] 默认删除所有链表里的规则                 |
| -P   | iptables -P chain target 指定该链表的默认操作（DROP和ACCEPT） |

### match
#### 通用匹配
| 匹配 选项 | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| [!] -p    | iptables -A INPUT -p protocol …1、指定协议，如tcp、udp等，不区分大小写，也可以是协议对应的数字编号，都可以在/etc/protocols查看。2、数字0和‘all’表示所有的协议，也是缺省值，注意只匹配 TCP、UDP、ICMP。而不是/etc/protocols里的所有协议。3、可以同时指定多个匹配协议，以逗号分隔，如tcp,udp4、可选参数 ！ 表示取反的意思，如 ! -p tcp 则表示匹配UDP和ICMP |
| [!] -s    | 示例：iptables -A INPUT -s 192.168.1.0/24 …指定源地址，可以是主机名也可以是IP形式的地址，主机名会先dns解析得到相应的IP地址再添加到过滤表当中；可以是单个IP地址，也可以像上面示例一样是某个网段 |
| [!] -d    | 匹配目的地址，跟 -s 用法一致                                 |
| [!] -i    | 示例：iptables -A INPUT -i eth0 …1、对于链表INPUT、FORWARD、PREROUTING的数据指定接口名2、可以使用通配符，如 eth+，则可以匹配 eth0、eth1 等所有eth开头的网口3、这个尤其适用于多核设备内部地址通信默认允许策略配置 |
| [!] -o    | 指定离开本地所用的网口                                       |
| –sport    | iptables -A INPUT -p tcp –sport 22 …1、可以指定 tcp 或者 udp 的源端口号…2、可以使用连续的端口号，如 –sport 22:100，则表示从22到100的所有端口…3、可以进行取反操作如，! –sport 22，即除22以外的端口 |
| –dport    | 指定目标端口，用法和 –sport 一样                             |

#### 显示匹配
通过 `-m` 选项指定所要加载的匹配模块名称，后面再跟相应的选项即可。
如过滤 mac 地址操作，指定模块 mac，选项如下：

| 匹配选项               | 说明                                                         |
| ---------------------- | ------------------------------------------------------------ |
| -m mac [!] –mac-source | 示例：iptables -A INPUT -m mac –mac-source XX:XX:XX:XX:XX:XX 匹配的源MAC地址，格式必须是XX:XX:XX:XX:XX:XX，只能用于过滤进入的数据 |
| -m multiport           | 示例：iptables -A INPUT -p tcp -m multiport –sport 22,23,24 前面匹配端口时只写了连续的端口匹配方式，如果想指定多个端口，则需要使用 -m multiport |
| -m iprange             | 示例：iptables -A INPUT -m iprange –src-range 192.168.1.1-192.168.1.10 -j ACCEPT 匹配连续的多个IP地址 |

#### target
最后说下数据包的处理动作，通过参数-j指定

| 选项 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| -j   | 示例：iptables -A INPUT -p tcp -sport 22 -j DROP –jump target 指定要进行的处理动作 ACCEPT ：允许，匹配后就不会去匹配当前链中的其他规则 DROP ：丢弃 |

## 实例
```shell
# 清空已有 iptables 规则
iptables -F
iptables -X
iptables -Z

# 删除已添加的规则
## 删除 INPUT 里序号为 110 的规则
## 需使用：iptables -L -n --line-numbers，查看序号
iptables -D INPUT 110
```
```shell
# 放行端口
iptables -I INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT	# 允许本地回环接口(即运行本机访问本机)
iptables -A OUTPUT -j ACCEPT	# 允许所有本机向外的访问
```
```shell
# 屏蔽IP
iptables -I INPUT -s 123.45.6.7 -j DROP		# 屏蔽单个IP的命令
iptables -I INPUT -s 123.0.0.0/8 -j DROP	# 封整个段即从123.0.0.1到123.255.255.254的命令
iptables -I INPUT -s 124.45.0.0/16 -j DROP	# 封IP段即从123.45.0.1到123.45.255.254的命令
iptables -I INPUT -s 123.45.6.0/24 -j DROP	# 封IP段即从123.45.6.1到123.45.6.254的命令是
```
```shell
# 查看已添加的规则
## -L 表示查看当前表的所有规则，默认查看的是 filter 表，如果要查看 nat 表，可以加上 -t nat 参数。
## -n 表示不对 IP 地址进行反查，加上这个参数显示速度将会加快。
## -v 表示输出详细信息，包含通过该规则的数据包数量、总字节数以及相应的网络接口。
## --line-numbers：以序号标记显示
iptables -L -n -v
iptables -nvL
iptables -L -n --line-numbers
```

---


参考文档：

> https://glory.blog.csdn.net/article/details/123690660