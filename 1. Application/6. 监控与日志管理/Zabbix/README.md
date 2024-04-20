# 基本概念

Zabbix最重要的五个组成部分：

1. Item ——> 监控项 ——> 需要监控的内容
2. Trigger ——> 触发器 ——> 监控的内容满足什么条件时报警
3. Action ——> 动作 ——> 触发器出发时怎么告警
4. Media ——> 报警介质 ——> 告警采用什么方式
5. User ——> 用户 ——> 用户

# 工作原理

一个监控系统运行的大概的流程是这样的：

Zabbix agent 需要安装到被监控的主机上，它负责定期收集各项数据，并发送到 server 端

Zabbix server 将数据存储到数据库中，zabbix web根据数据在前端进行展现和绘图。



这里agent收集数据分为主动和被动两种模式：

- 主动：agent 请求 server 获取主动的监控项列表，并主动将监控项内需要检测的数据提交给 server/proxy
- 被动：server 向 agent 请求获取监控项的数据，agent 返回数据。

# 组件及进程

Zabbix 由以下几个组件部分构成：

1. Zabbix Server：负责接收agent发送的报告信息的核心组件， 所有配置，统计数据及操作数据均由其组织进行；
2. Database Storage：专用于 存储所有配置信息，以及由zabbix收集的数据；
3. Web interface： zabbix的GUI接口，通常与Server运行在同一台主机上；
4. Proxy：可 选组件，常用于分布监控环境中，代理Server收集部分被监控端的监控数据并统一发往Server端；
5. Agent： 部署在被监控主机上，负责收集本地数据并发往Server端或Proxy端；

# 专有名词

1. 主机（host）：要监控的网络设备，可由IP或DNS名称指定
2. 主机组（host group）：主机的逻辑容器，可以包含主机和模版，但同一个组内的主机和模版不能互相链接；主机组通常在给用户或用户组指派监控权限时使用
3. 监控项（item）：一个特定监控指标的相关的数据，这些数据来自于被监控对象；item是zabbix进行数据采集的核心，没有item将没有数据；相对某监控对象来说，每个item都由“key”进行标识
4. 触发器（trigger）：一个表达式，用于评估某监控对象的某特定item内所接受到的数据是否在合理范围内，即阈值；接受到的数据量大于阈值时，触发器状态将从“OK”转变为“Problem”，但数据在此回归到合理范围时，其状态将从“Problem”转换回“OK”
5. 事件（event）：即发生的一个值得关注的事情，如触发器的状态转变，新的agent或重新上线的agent的自动注册等
6. 动作（action）:指对于特定事件事先定义的处理方法，通过包含操作（如发送通知）和条件（何时执行操作）
7. 报警升级（escalation）：发送报警或执行远程命令的自定义方案，如每5分钟发送一次警报，共发送5次等
8. 媒介（media）：发送通知的手段或通道，如Email，Jabber或SMS等
9. 通知（notification）：通过选定的媒介向用户发送的有关某事件的信息
10. 远程命令（remote command）：预定义的命令，可在被监控主机处于某特定条件时自动执行
11. 模版（template）:用于快速定义被监控主机的预设条目集合，通常包含了item，trigger，graph，screen，application以及low-level discovery rule；模版可以直接链接至单个主机
12. 应用（application）：一组item的集合
13. web场景（web scennario）：用于检测web站点可用性的一个或多个HTTP请求
14. 前端（frontend）：Zabbix的web接口

# 监控模式

当服务端监控主机过多时候，由于服务端去搜集信息，服务端会出现严重的性能问题，比如：

1. 当监控端到一个量级的时候，web操作界面很卡，容易出现502。
2. 图层断裂。
3. 开启的进程太多，即使item数量减少，以后加一定量的机器也会出现问题。


所以主要往2个优化方面考虑：

1. 添加 proxy 节点或者 node 模式做分布式监控
2. 调整 agentd 为主动模式。

由于第一个方案需要加物理机器，所以尝试第二个方案。

## 被动式

被动式为默认模式，只需修改以下几项配置：

```ini
Server = 服务端IP
ServerActive = 服务端IP
Hostname = 客户端IP
```

## 主动式

主动模式一定要记得设置： `ServerActive=ServerIP`，并取消：`Server=` 选项

主动模式流程：

1. Agent向Server建立一个TCP连接

2. Agent请求需要检测的数据列表

3. Server响应Agent，发送一个Items列表

4. Agent允许响应

5. TCP连接完成本次会话关闭

6. Agent开始周期性地收集数据

---



> 参考文档：
>
> 钉钉告警：https://www.cnblogs.com/yanjieli/p/10848330.html
>
> 钉钉告警：https://blog.51cto.com/m51cto/2051945
>
> 钉钉告警：https://blog.51cto.com/11353391/2537688?source=dra
>
> 钉钉告警：https://www.jb51.net/article/185134.htm
>
> 邮件告警：https://blog.csdn.net/qq_44434664/article/details/87939940
>
>
> 邮件告警：https://blog.51cto.com/andyxu/2145196
