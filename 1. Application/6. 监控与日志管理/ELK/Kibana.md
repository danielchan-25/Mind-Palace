# Kibana

## 1. 部署

```shell
wget https://artifacts.elastic.co/downloads/kibana/kibana-8.17.0-linux-x86_64.tar.gz
tar -xvf kibana-8.17.0-linux-x86_64.tar.gz
```

修改配置文件：`config/kibana.yml`

```yml
server.port: 5601
server.host: "0.0.0.0"
server.name: "kibana"
elasticsearch.hosts: ["http://10.17.174.99:9200"]
i18n.locale: "zh-CN"
elasticsearch.ssl.verificationMode: none

elasticsearch.username: "kibana_system"
elasticsearch.password: "your-kibana-system-password"
# 注意：kibana_system 不能直接登录 kibana
```

尝试启动，并访问后台：`http://localhost:5601/`，使用 `elastic` 用户登录

```shell
# 不支持使用root用户启动
su elk ./bin/kibana
nohup su elk ./bin/kibana &	# 后台启动
```



