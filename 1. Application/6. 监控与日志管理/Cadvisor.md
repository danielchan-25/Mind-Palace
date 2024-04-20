---
title: "cadvisor"

---

# 简介
为了解决 `docker stats` 的问题(存储、展示)，谷歌开源的 `cadvisor` 诞生了。

`cadvisor` 不仅可以搜集一台机器上所有运行的容器信息，还提供基础查询界面和 http 接口，方便其他组件如 `Prometheus` 进行数据抓取，或者 `cadvisor + influxdb + grafna` 搭配使用。

`cAdvisor` 可以对节点机器上的资源及容器进行实时监控和性能数据采集，包括 CPU 使用情况、内存使用情况、网络吞吐量及文件系统使用情况

`Cadvisor` 使用Go语言开发，利用 Linux 的 `cgroups` 获取容器的资源使用信息，在K8S中集成在Kubelet里作为默认启动项，官方标配。


> Github: [Cadvisor](https://github.com/google/cadvisor)

# 部署

由于在国内因不可控因素，建议使用二进制文件部署。

## 二进制文件部署

下载二进制文件，直接可用。

> Github:[Cadvisor](https://github.com/google/cadvisor/releases)

```shell
./cadvisor -port=8080 >> cadvisor.log
```

## docker 部署

```shell
docker pull google/cadvisor:latest
```
```shell
docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
```

# 配合其它工具使用

可使用以下URL，配合 `Prometheus`

> http://localhost:8080/metrics

在 `Prometheus.yml` 下新增：
```yml
scrape_configs:
  - job_name: "cadvisor"
    static_configs:
      - targets: ["10.17.174.252:8080"]
```
