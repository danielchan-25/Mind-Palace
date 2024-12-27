# HeartBeat

## 1. 部署

```shell
# 二进制文件部署
# Centos7版本
curl -L -O https://artifacts.elastic.co/downloads/beats/heartbeat/heartbeat-8.17.0-x86_64.rpm
sudo rpm -vi heartbeat-8.17.0-x86_64.rpm
```

修改配置文件：`/etc/heartbeat/heartbeat.yml`

```yml
output.elasticsearch:
  hosts: ["https://localhost:9200"]
  ssl.verification_mode: none
  preset: balanced
  username: "elastic"
  password: "LiaXoLvkZm4tklG6Md5J"

setup.kibana:
  host: "localhost:5601"
  
heartbeat.monitors:
- type: http
  urls: ["<http://localhost:9200>"]
  schedule: "@every 10s"
```

启动：

```shell
heartbeat setup
service heartbeat-elastic start
```



