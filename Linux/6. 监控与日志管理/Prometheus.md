# Prometheus
# 1. 介绍
`prometheus` 是一种时间序列的数据库，适合应用于监控以及告警，但是不适合100%的准确计费，因为采集的数据不一定很准确，主要是作为监控以及收集内存、CPU、硬盘的数据。

> 下载地址：https://prometheus.io/download/
>
> 下载地址：https://github.com/prometheus/prometheus/releases/download/

## 1.1 主要特征
- 多维数据模型（时序数据由 metric名和一组 key/value组成）
- 在多维度上灵活的查询语言(PromQI)
- 不依赖分布式存储，单主节点工作
- 通过基于HTTP的pull方式采集时序数据
- 也通过中间网关进行时序数据推送（pushing）
- 通过服务发现或静态配置，来发现目标服务对象
- 多种可视化和仪表盘支持，如grafana

## 1.2 相关组件
`Prometheus` 生态系统由多个组件组成，其中许多是可选的：
- Prometheus Server：：负责对监控数据的获取，存储以及查询
- Client Library: 客户端库，负责检测应用程序代码
- Push Gateway：正常情况下Prometheus Server能够直接与Exporter进行通信，然后pull数据；当网络需求无法满足时就可以使用PushGateway作为中转站了
- Exporter：监控数据采集器，将数据通过Http的方式暴露给Prometheus Server；
- AlertManager：：Prometheus支持通过PromQL来创建告警规则，满足规则时创建一条告警，后续的告警流程就交给AlertManager，其提供了多种告警方式包括email，webhook等方式；
- Web UI：简单的web控制台

## 1.3 与 zabbix 相比
- Zabbix 使用的是 C 和 PHP, Prometheus 使用 Golang, 整体而言 Prometheus 运行速度更快一点。
- Zabbix 属于传统主机监控，主要用于物理主机，交换机，网络等监控，Prometheus 不仅适用主机监控，还适用于 Cloud, SaaS, Openstack，Container 监控。
- Zabbix 在传统主机监控方面，有更丰富的插件
- Zabbix 可以在 WebGui 中操作配置，Prometheus 需要手动修改文件配置。


- Prometheus 属于一站式监控告警平台，依赖少，功能齐全
- Prometheus 支持对云或容器的监控，其他系统主要对主机监控
- Prometheus 数据查询语句表现力更强大，内置更强大的统计函数
- Prometheus 在数据存储扩展性以及持久性上没有 InfluxDB，OpenTSDB，Sensu 好




# 2. 监控

## 2.1 CPU

对于节点，我们首先能想到的就是要先对 CPU 进行监控，因为 CPU 是处理任务的核心，根据 CPU 的状态可以分析出当前系统的健康状态。

要对节点进行 CPU 监控，需要用到 `node_cpu_seconds_total` 这个监控指标，在 metrics 接口中该指标内容如下所示：

```yml
# HELP node_cpu_seconds_total Seconds the CPUs spent in each mode.
# TYPE node_cpu_seconds_total counter
node_cpu_seconds_total{cpu="0",mode="idle"} 2.48603354e+06
node_cpu_seconds_total{cpu="0",mode="iowait"} 4926.57
node_cpu_seconds_total{cpu="0",mode="irq"} 0
node_cpu_seconds_total{cpu="0",mode="nice"} 284.08
node_cpu_seconds_total{cpu="0",mode="softirq"} 798
node_cpu_seconds_total{cpu="0",mode="steal"} 0
node_cpu_seconds_total{cpu="0",mode="system"} 40778.19
node_cpu_seconds_total{cpu="0",mode="user"} 166498.14
node_cpu_seconds_total{cpu="1",mode="idle"} 2.49278614e+06
node_cpu_seconds_total{cpu="1",mode="iowait"} 4915.94
node_cpu_seconds_total{cpu="1",mode="irq"} 0
node_cpu_seconds_total{cpu="1",mode="nice"} 178.46
node_cpu_seconds_total{cpu="1",mode="softirq"} 8468.66
node_cpu_seconds_total{cpu="1",mode="steal"} 0
node_cpu_seconds_total{cpu="1",mode="system"} 36884.83
node_cpu_seconds_total{cpu="1",mode="user"} 150982.5
node_cpu_seconds_total{cpu="2",mode="idle"} 2.50505604e+06
node_cpu_seconds_total{cpu="2",mode="iowait"} 4557.23
node_cpu_seconds_total{cpu="2",mode="irq"} 0
node_cpu_seconds_total{cpu="2",mode="nice"} 380.11
node_cpu_seconds_total{cpu="2",mode="softirq"} 787.13
node_cpu_seconds_total{cpu="2",mode="steal"} 0
node_cpu_seconds_total{cpu="2",mode="system"} 37014.57
node_cpu_seconds_total{cpu="2",mode="user"} 154322.88
node_cpu_seconds_total{cpu="3",mode="idle"} 2.51322785e+06
node_cpu_seconds_total{cpu="3",mode="iowait"} 3555.05
node_cpu_seconds_total{cpu="3",mode="irq"} 0
node_cpu_seconds_total{cpu="3",mode="nice"} 679.2
node_cpu_seconds_total{cpu="3",mode="softirq"} 550.78
node_cpu_seconds_total{cpu="3",mode="steal"} 0
node_cpu_seconds_total{cpu="3",mode="system"} 35097.04
node_cpu_seconds_total{cpu="3",mode="user"} 152608.38
```

从接口中描述可以看出该指标是用来统计 CPU 每种模式下所花费的时间，是一个 Counter 类型的指标，也就是会一直增长，这个数值其实是 CPU 时间片的一个累积值，意思就是从操作系统启动起来 CPU 开始工作，就开始记录自己总共使用的时间，然后保存下来，而且这里的累积的 CPU 使用时间还会分成几个不同的模式，比如用户态使用时间、空闲时间、中断时间、内核态使用时间等等，也就是平时我们使用 top 命令查看的 CPU 的相关信息，而我们这里的这个指标会分别对这些模式进行记录。

接下来我们来对节点的 CPU 进行监控，我们也知道一个一直增长的 CPU 时间对我们意义不大，一般我们更希望监控的是节点的 CPU 使用率，也就是我们使用 top 命令看到的百分比。

要计算 CPU 的使用率，那么就需要搞清楚这个使用率的含义：

cpu.idle 指的是：CPU处于空闲状态时间比例，从时间的角度衡量CPU的空闲程度。

**CPU 使用率是 CPU 除空闲（idle）状态之外，其他所有 CPU 状态的时间总和除以总的 CPU 时间**得到的结果，理解了这个概念后就可以写出正确的 promql 查询语句了。

1. 要计算除空闲状态之外的 CPU 时间总和，更好的方式是直接计算空闲状态的 CPU 时间使用率，然后用 1 减掉就是我们想要的结果了，所以首先我们先过滤 `idle` 模式的指标，在 `Prometheus` 中输入 `node_cpu_seconds_total{mode="idle"}` 进行过滤
2. 要计算使用率，肯定就需要知道 `idle` 模式的 CPU 用了多长时间，然后和总的进行对比，由于这是 Counter 指标，我们可以用 `increase` 函数来获取变化，使用查询语句 `increase(node_cpu_seconds_total{mode="idle"}[1m])`，因为 `increase` 函数要求输入一个区间向量，所以这里我们取 1 分钟内的数据
3. 我们可以看到查询结果中有很多不同 cpu 序号的数据，我们当然需要计算所有 CPU 的时间，所以我们将它们聚合起来，我们要查询的是不同节点的 CPU 使用率，所以就需要根据 `instance` 标签进行聚合，使用查询语句 `sum(increase(node_cpu_seconds_total{mode="idle"}[1m])) by (instance)`
4. 这样我们就分别拿到不同节点 1 分钟内的空闲 CPU 使用时间了，然后和总的 CPU （这个时候不需要过滤状态模式）时间进行比较即可，使用查询语句 `sum(increase(node_cpu_seconds_total{mode="idle"}[1m])) by (instance) / sum(increase(node_cpu_seconds_total[1m])) by (instance)`
5. 然后计算 CPU 使用率就非常简单了，使用 1 减去乘以 100 即可：`(1 - sum(increase(node_cpu_seconds_total{mode="idle"}[1m])) by (instance) / sum(increase(node_cpu_seconds_total[1m])) by (instance) ) * 100`。这就是能够想到的最直接的 CPU 使用率查询方式了，当然前面我们学习的 promql 语法中提到过更多的时候我们会去使用 `rate` 函数，而不是用 `increase` 函数进行计算，所以最终的 CPU 使用率的查询语句为：`(1 - sum(increase(node_cpu_seconds_total{mode="idle"}[1m])) by (instance) / sum(increase(node_cpu_seconds_total[1m])) by (instance) ) * 100`

## 2.2 内存

除了 CPU 监控之外，我们可能最关心的就是节点内存的监控了，平时我们查看节点的内存使用情况基本上都是使用 free 命令来查看

`free` 命令的输出会显示系统内存的使用情况，包括物理内存、交换内存(swap)和内核缓冲区内存等，所以要对内存进行监控我们需要先了解这些概念，我们先了解下 `free` 命令的输出内容：

- `Mem 行`(第二行)是内存的使用情况
- `Swap 行`(第三行)是交换空间的使用情况
- `total` 列显示系统总的可用物理内存和交换空间大小
- `used` 列显示已经被使用的物理内存和交换空间
- `free` 列显示还有多少物理内存和交换空间可用使用
- `shared` 列显示被共享使用的物理内存大小
- `buff/cache` 列显示被 buffer 和 cache 使用的物理内存大小
- `available` 列显示还可以被应用程序使用的物理内存大小

其中我们需要重点关注的 `free` 和 `available` 两列。free 是真正尚未被使用的物理内存数量，而 available 是从应用程序的角度看到的可用内存，Linux 内核为了提升磁盘操作的性能，会消耗一部分内存去缓存磁盘数据，就是 buffer 和 cache，所以对于内核来说，buffer 和 cache 都属于已经被使用的内存，只是应用程序需要内存时，如果没有足够的 free 内存可以用，内核就会从 buffer 和 cache 中回收内存来满足应用程序的请求。所以从应用程序的角度来说 `available = free + buffer + cache`，不过需要注意这只是一个理想的计算方式，实际中的数据有较大的误差。

如果要在 Prometheus 中来查询内存使用，则可以用 `node_memory_*` 相关指标，同样的要计算使用的，我们可以计算可使用的内存，使用 promql 查询语句 `node_memory_Buffers_bytes + node_memory_Cached_bytes + node_memory_MemFree_bytes`。

然后计算可用内存的使用率，和总的内存相除，然后同样用 1 减去即可，语句为 `(1- (node_memory_Buffers_bytes + node_memory_Cached_bytes + node_memory_MemFree_bytes) / node_memory_MemTotal_bytes) * 100`，这样计算出来的就是节点内存使用率。

当然如果想要查看各项内存使用直接使用对应的监控指标即可，比如要查看节点总内存，直接使用 `node_memory_MemTotal_bytes` 指标即可获取。

## 2.3 磁盘

接下来是比较中的磁盘监控，对于磁盘监控我们不仅对磁盘使用情况感兴趣，一般来说对于磁盘 IO 的监控也是非常有必要的。

### 2.3.1 容量监控

要监控磁盘容量，需要用到 `node_filesystem_*` 相关的指标，比如要查询节点磁盘空间使用率，则可以同样用总的减去可用的来进行计算，磁盘可用空间使用 `node_filesystem_avail_bytes` 指标，但是由于会有一些我们不关心的磁盘信息，所以我们可以使用 `fstype` 标签过滤关心的磁盘信息，比如 `ext4` 或者 `xfs` 格式的磁盘

要查询磁盘空间使用率，则使用查询语句 `(1 - node_filesystem_avail_bytes{fstype=~"ext4|xfs"} / node_filesystem_size_bytes{fstype=~"ext4|xfs"}) * 100` 即可：

### 2.3.2 IO 监控

要监控磁盘 IO，就要区分是读的 IO，还是写的 IO，读 IO 使用 `node_disk_reads_completed` 指标，写 IO 使用 `node_disk_writes_completed_total` 指标。
磁盘读 IO 使用 `sum by (instance) (rate(node_disk_reads_completed_total[5m]))` 查询语句即可

当然如果你想根据 `device` 进行聚合也是可以的，我们这里是全部聚合在一起了。
磁盘写 IO 使用 `sum by (instance) (rate(node_disk_writes_completed_total[5m]))` 查询语句即可

## 2.4 网络

上行带宽需要用到的指标是 `node_network_receive_bytes`，由于我们对网络带宽的瞬时变化比较关注，所以一般我们会使用 `irate` 函数来计算网络 IO，比如计算上行带宽用查询语句 `sum by(instance) (irate(node_network_receive_bytes_total{device!~"bond.*?|lo"}[5m]))` 即可

下行带宽用到的指标为 `node_network_transmit_bytes`，同样的方式查询语句为 `sum by(instance) (irate(node_network_transmit_bytes{device!~"bond.*?|lo"}[5m]))`

# 3. 函数

## rate()
rate函数，rate用来计算两个 间隔时间内发生的变化率（一段时间内平均每秒的增量）
专门用来搭配`Counters`类型的数据，`rate(指标名{筛选条件}[时间间隔])`

```sh
# 比如 查看1分钟内非idle的cpu使用率
rate(node_cpu_seconds_total{mode!="idle"}[1m])
```
## irate()
rate 与 irate 的区别：
irate 和 rate 都会用于计算某个指标在一定时间间隔内的变化速率。

但是它们的计算方法有所不同：irate 取的是在指定时间范围内的最近两个数据点来算速率，而 rate 会取指定时间范围内所有数据点，算出一组速率，然后取平均值作为结果。

**irate 适合快速变化的计数器（counter），而 rate 适合缓慢变化的计数器（counter）**

根据以上算法我们也可以理解，对于快速变化的计数器，如果使用 rate，因为使用了平均值，很容易把峰值削平。除非我们把时间间隔设置得足够小，就能够减弱这种效应。

# 7. 告警

告警规则主要依赖于采集指标（metric），通过对指标进行分析设置阀值来达到告警的目的

告警状态有三种状态

- Inactive：非活动状态，表示正在监控，但是还未有任何警报触发。
- Pending：表示这个警报必须被触发。由于警报可以被分组、压抑/抑制或静默/静音，所以等待验证，一旦所有的验证都通过，则将转到 Firing 状态。
- Firing：将警报发送到 AlertManager，它将按照配置将警报的发送给所有接收者。一旦警报解除，则将状态转到 Inactive，如此循环。



1. 配置告警目录，创建 `rules` 目录，用于统一存放告警规则：`mkdir -p ./rules`

2. 编辑 `prometheus.yml` 文件，配置 `rule_files` 路径

   ```yml
   rule_files:
     - rules/*.yml
   ```

3. 编写告警规则

   ```yml
   #  对于 Prometheus 监控的服务器，都有一个 up 指标，可以知道该服务是否在线。
   #  up == 0/1 服务下/上线了
   
   # "for" 指定达到告警阈值后，一致要持续多长时间才发送告警数据
   # "labels" 可以指定自定义的标签，如定义的标签已存在，则会被覆盖
   # "annotations" 中，$labels 表示告警数据的标签，{{$value}}表示时间序列的值
   
   groups:
   - name: 主机存活告警  # 组的名字，在这个文件必须唯一
     rules:
     - alert: 主机存活告警  # 告警的名字，在组中必须唯一
       expr: up == 0  # 表达式，执行结果为true，表示需要告警
       for: 60s  # 当 up == 0 持续多久才会告警
       labels:   
         severity: warning  # 自定义告警标签
       annotations:  # 告警内容注释，根据需要制定
         summary: "{{ $labels.instance }} 宕机超过1分钟！"  
   ```

   ```yaml
   groups:
   - name: 主机内存使用率告警
     rules:
     - alert: 主机内存使用率告警
       expr: (1 - (node_memory_MemAvailable_bytes / (node_memory_MemTotal_bytes))) * 100 > 80
       for: 15m
       labels:
         severity: warning
       annotations:
         summary: "内存利用率大于80%, 实例: {{ $labels.instance }}，当前值：{{ $value }}%"
   ```

   ```yaml
   groups:
   - name: 主机CPU使用率告警
     rules:
     - alert: 主机CPU使用率告警
       expr: 100 - (avg by (instance)(irate(node_cpu_seconds_total{mode="idle"}[1m]) )) * 100 > 80
       for: 15m
       labels:
         severity: warning
       annotations:
         summary: "CPU近15分钟使用率大于80%, 实例: {{ $labels.instance }}，当前值：{{ $value }}%"
   ```

   ```yml
   # 磁盘利用>80%
   groups:
   - name: 主机磁盘使用率告警
     rules:
     - alert: 主机磁盘使用率告警
       expr: 100 - node_filesystem_free_bytes{fstype=~"xfs|ext4"} / node_filesystem_size_bytes{fstype=~"xfs|ext4"} * 100 > 80 
       for: 15m
       labels:
         severity: warning
       annotations:
         summary: "磁盘使用率大于80%, 实例: {{ $labels.instance }}，当前值：{{ $value }}%"
   ```

4. 检测配置文件是否编写正确：`./promtool check config prometheus.yml`

5. 重启 `prometheus` 生效规则





---



> 参考文档：
> 配合Grafana：https://blog.csdn.net/qq_37128049/article/details/108143110
>
> 简介：https://blog.csdn.net/shenyuanhaojie/article/details/121775976
>
> 函数介绍：https://www.cnblogs.com/ztxd/articles/16480285.html
>
> 告警规则：https://blog.csdn.net/manwufeilong/article/details/126159641
>
> 告警规则：https://blog.csdn.net/xiaoxiangzi520/article/details/115005765
>
> 告警规则：https://blog.csdn.net/u013958257/article/details/107437533
>
> 告警规则：https://blog.csdn.net/fu_huo_1993/article/details/114547201
>
> CPU/内存/磁盘/网络监控：https://zhuanlan.zhihu.com/p/494641308