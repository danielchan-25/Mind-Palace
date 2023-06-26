# Firewall

在Linux中，防火墙是一种网络安全机制，用于保护计算机免受恶意网络流量和未经授权的访问。它是一个软件或硬件设备，位于计算机和网络之间，通过控制网络流量的进出规则来保护计算机系统。

Linux操作系统通常使用Netfilter项目的iptables软件包来实现防火墙功能。它允许管理员定义规则和策略来过滤、转发或修改进出系统的网络流量。

防火墙在网络层面起作用，通过检查网络数据包的源地址、目标地址、端口号和协议等信息来决定是否允许流量通过。它可以根据预先定义的规则来允许或阻止特定类型的流量，从而实现网络安全控制。

Linux防火墙可以实现以下功能：

1. 包过滤：根据规则过滤进出系统的网络数据包，以允许或阻止特定流量。

2. 网络地址转换（NAT）：通过修改数据包的源地址和目标地址来实现网络地址转换，用于连接多个私有网络到公共网络。

3. 服务端口映射：将外部网络请求的端口映射到内部服务器的特定端口，以实现内部服务的访问。

4. 状态跟踪：跟踪网络连接的状态，例如建立、终止和超时，以便进行连接状态的管理和安全性检查。

5. 拒绝服务（DoS）防护：通过限制来自特定源的流量或应用特定规则来防止拒绝服务攻击。

Linux防火墙可以通过命令行工具（如iptables、nftables）进行配置和管理，也可以使用图形界面工具（如ufw、firewalld）来简化管理过程。

请注意，不同的Linux发行版可能有不同的防火墙工具和配置方式，因此具体的配置和管理方法可能会有所差异。在设置和管理防火墙时，确保参考适用于你所使用Linux发行版的文档和指南。

## Iptables
### 介绍
`iptables` 默认维护着四个表和五个链。

**四表**

**“四表”**是指 `iptables` 以下四张表：

1. **filter表**：过滤规则表，控制数据包是否允许进出及转发，可以控制的链路有 `INPUT、FORWARD、OUTPUT`

2. **nat表**：地址转换规则表，控制数据包中地址转换，可以控制的链路有 `PREROUTING、INPUT、OUTPUT、POSTROUTING`。

3. **mangle表**：修改数据标记位规则表，修改数据包中的原数据，可以控制的链路有 `PREROUTING、INPUT、OUTPUT、FORWARD、POSTROUTING`。

4. **raw表**：跟踪数据表规则表，控制 nat 表中连接追踪机制的启用状况，可以控制的链路有 `PREROUTING、OUTPUT`。

**五链**

**“五链”**是指内核中控制网络的 NetFilter 定义的 5 个规则链。每个规则表中包含多个数据链

1. INPUT（入站数据过滤）

2. OUTPUT（出站数据过滤）

3. FORWARD（转发数据过滤）

4. PREROUTING（路由前过滤）

5. 和POSTROUTING（路由后过滤）

### 安装
```sh
# CentOS
yum -y install iptables iptables-services
systemctl start iptables && systemctl enable iptables
```
### 语法
```bash
# 语法
iptables [-t table] command [match] [target]
iptables [-t 表名] <-A|I|D|R> 链名 [规则编号] [-i|o 网卡名称] [-p 协议类型] [-s 源ip|源子网] [--sport 源端口号] [-d 目的IP|目标子网] [--dport 目标端口号] [-j 动作]

# -t： 用于指定所要操作的表，不指定则默认 filter 表
# command：具体的命令动作，比如对指定链添加/删除规则
# match：对所要处理包的匹配规则
# target：数据包的处理动作
# 大小写敏感
```
### 命令
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

### 规则
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

### 实例
```bash
# 清空已有 iptables 规则
iptables -F
iptables -X
iptables -Z

# 删除已添加的规则
## 删除 INPUT 里序号为 110 的规则
## 需使用：iptables -L -n --line-numbers，查看序号
iptables -D INPUT 110
```
```bash
# 放行端口
iptables -I INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT	# 允许本地回环接口(即运行本机访问本机)
iptables -A OUTPUT -j ACCEPT	# 允许所有本机向外的访问
```
```bash
# 屏蔽IP
iptables -I INPUT -s 123.45.6.7 -j DROP		# 屏蔽单个IP的命令
iptables -I INPUT -s 123.0.0.0/8 -j DROP	# 封整个段即从123.0.0.1到123.255.255.254的命令
iptables -I INPUT -s 124.45.0.0/16 -j DROP	# 封IP段即从123.45.0.1到123.45.255.254的命令
iptables -I INPUT -s 123.45.6.0/24 -j DROP	# 封IP段即从123.45.6.1到123.45.6.254的命令是
```
```bash
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

## Firewalld

### 介绍

Firewalld 是 CentOS 及其衍生发行版（如RHEL）中默认的动态防火墙管理工具。它提供了一种简化的方式来管理网络防火墙规则，并具有动态更新和配置更改的能力。Firewalld使用D-Bus系统总线来与网络管理器和其他系统组件进行通信。

### 常用命令

```sh
sudo systemctl start firewalld   # 启动Firewalld服务
sudo systemctl stop firewalld    # 停止Firewalld服务
sudo systemctl restart firewalld # 重启Firewalld服务

sudo systemctl status firewalld	 # 检查Firewalld服务状态
sudo systemctl enable firewalld	 # 设置开机启动
```

### 基本语法

```sh
sudo firewall-cmd --zone=public --add-service=http     # 添加HTTP服务规则到public区域
sudo firewall-cmd --zone=public --remove-service=http  # 从public区域删除HTTP服务规则

sudo firewall-cmd --zone=public --add-service=http --permanent  # 添加永久性HTTP服务规则到public区域
sudo firewall-cmd --reload  # 重载规则，使永久性设置生效


sudo firewall-cmd --list-all  # 显示所有区域和规则的详细信息
sudo firewall-cmd --zone=public --list-services  # 显示特定区域中启用的服务
```

