# Zabbix_自定义监控
## 监控 Windows 主机进程

需求：在 Windows 客户端中，运行了 4 个 Python 进程，需要监控是否在线。

1. 在 Zabbix Server 中新建模板
2. 新建【监控项】：`proc.num[<name>,<user>,<state>,<cmdline>,<zone>]`，键值设置为：`proc.num[python.exe]`
3. 点击【测试】，会显示出 4 个 Python 的进程数量，OK 正常
4. 新建【触发器】：表达式根据实际情况输入，如小于4触发告警，如=0触发告警。


## 监控 MySQL
监控 MySQL 可以使用自带的 `Template DB MySQL by Zabbix agent 2` 模板，前提是客户端也是 `Zabbix agent 2`。

## 监控 Redis
由于 5.0 TLS 版本不支持 Yaml 模板导入，唯有使用自带的 `Template DB Redis` 模板。

1. 新建宏：`{$REDIS_PASS}`，值为密码
2. 修改监控项
   1. `Redis: Get config`，``Redis: Get info`, `Redis: Ping`, `Redis: Slowlog entries per second`
   2. 键值统一添加 `{$REDIS_PASS}`，例如：`["{$REDIS.CONN.URI}","{$REDIS_PASS}"]`
