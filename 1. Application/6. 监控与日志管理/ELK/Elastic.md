# Elastic

## 1. 部署

```shell
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.17.0-linux-x86_64.tar.gz
tar -xvf elasticsearch-8.17.0-linux-x86_64.tar.gz
chown -R elk.elk elasticsearch-8.17.0/
```

修改配置文件：`config/elasticsearch.yml`

```yml
path.data: ./data # 数据目录位置
path.logs: ./logs # 日志目录位置
network.host: 0.0.0.0
http.port: 9200

# 初始化节点名称
cluster.name: elasticsearch
node.name: es-node0
cluster.initial_master_nodes: ["es-node0"]

xpack.security.enabled: false	# 关闭SSL认证，如不关闭需要改为https访问
```

尝试启动，并访问后台：`http://localhost:9200/`

```shell
# 不支持使用root用户启动
su elk ./bin/elasticsearch
nohup su elk ./bin/elasticsearch &	# 后台启动

# 访问后台出现以下内容，证明成功
{
  "name": "es-node0",
  "cluster_name": "elasticsearch",
  "cluster_uuid": "8A3JFU0GTyqVFLGmTvBNjA",
  "version": {
    "number": "8.17.0",
    "build_flavor": "default",
    "build_type": "tar",
    "build_hash": "2b6a7fed44faa321997703718f07ee0420804b41",
    "build_date": "2024-12-11T12:08:05.663969764Z",
    "build_snapshot": false,
    "lucene_version": "9.12.0",
    "minimum_wire_compatibility_version": "7.17.0",
    "minimum_index_compatibility_version": "7.0.0"
  },
  "tagline": "You Know, for Search"
}
```







```shell
# 重置密码
# 当无法重置密码时，需要修改配置文件，将 xpack.security.enabled: 改回 true

./bin/elasticsearch-reset-password -u elastic
```

