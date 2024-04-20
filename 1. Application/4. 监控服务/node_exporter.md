# node_exporter

## 简介

`node_exporter` 是 `Prometheus` 的指标数据收集组件。

它负责从目标 Jobs 收集数据，并把收集到的数据转换为Prometheus支持的时序数据格式。

和传统的指标数据收集组件不同的是，他只负责收集，并不向Server端发送数据，而是等待 Prometheus Server 主动抓取

`node_exporter` 默认的抓取url地址：`http://ip:9100/metrics` 

`node_exporter` 用于采集 node 的运行指标，包括 node 的 **cpu、load、filesystem、meminfo、network** 等基础监控指标，类似于 `zabbix` 监控系统的的 `zabbix-agent`

> 下载地址：https://github.com/prometheus/node_exporter/releases

## 部署

1. 下载 `node_exporter` 到本机

```sh
wget https://github.com/prometheus/node_exporter/releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
tar -xvf node_exporter-0.17.0.linux-amd64.tar.gz
cd node_exporter-0.17.0.linux-amd64
```

2. 运行并测试

```sh
# 运行监控采集服务，端口为：9100
./node_exporter
curl -I 127.0.0.1:9100

# 后台运行
nohup ./node_exporter > /dev/null &
```

3. 修改 `prometheus.yml` 添加配置文件，重启生效

```sh
# 在 prometheus 添加 node 节点
scrape_configs:
 - job_name: 'node'
static_configs:
 - targets: ['192.168.1.22:9090']
```

4. 其它

```sh
# 修改默认端口
./node_exporter --web.listen-address=":9600"
# 修改metris路径，默认为 /metrics
./node_exporter --web.telemetry-path="/test_metrics"
# 最大并行请求数，默认为40，0为不限制
./node_exporter --web.max-requests=40
# 日志等级: [debug, info, warn, error, fatal]
./node_exporter --log.level="info"
# 置日志打印target和格式: [logfmt, json]
./node_exporter --log.format=logfmt
# 各个metric对应的参数
./node_exporter --collector.{metric-name} 
```

监控 Docker 容器时操作步骤一致。

## 功能

其中最重要的参数就是 `--collector.<name>`

通过该参数可以启用我们收集的功能模块，`node_exporter` 会默认采集一些模块，要禁用这些默认启用的收集器可以通过 `--no-collector.<name>` 标志来禁用

如果只启用某些特定的收集器，基于先使用 `--collector.disable-defaults` 标志禁用所有默认的，然后在通过指定具体的收集器 `--collector.<name>` 来进行启用。

下图列出了默认启用的收集器：