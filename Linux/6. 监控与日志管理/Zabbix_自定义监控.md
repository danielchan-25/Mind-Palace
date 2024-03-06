# Zabbix_自定义监控
## 监控Windows主机进程

需求：在 Windows 客户端中，运行了 4 个 Python 进程，需要监控是否在线。

1. 在 Zabbix Server 中新建模板
2. 新建【监控项】：`proc.num[<name>,<user>,<state>,<cmdline>,<zone>]`，键值设置为：`proc.num[python.exe]`
3. 点击【测试】，会显示出 4 个 Python 的进程数量，OK 正常
4. 新建【触发器】：表达式根据实际情况输入，如小于4触发告警，如=0触发告警。
