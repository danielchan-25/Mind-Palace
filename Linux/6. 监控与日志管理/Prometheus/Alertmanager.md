# AlertManager

`Prometheus` 包含一个报警模块，就是 `AlertManager`，`Alertmanager` 主要用于接收 `Prometheus` 发送的告警信息，它支持丰富的告警通知渠道，而且很容易做到告警信息进行去重，降噪，分组等，是一款前卫的告警通知系统，Alertmanager支持Email, Slack，等告警方式, 也可以通过webhook接入钉钉等国内IM工具。

## 安装

```shell
tar -xvf alertmanager-0.25.0-rc.2.linux-amd64.tar.gz
cd alertmanager-0.25.0-rc.2.linux-amd64/
./alertmanager	# 启动，可以访问 http://IP:9093 查看页面

# 常用启动参数
--config.file="alertmanager.yml"
--web.listen-address=:9093
```

## 配置

配置文件为：`alertmanager.yml`

```yml

```



## 邮件告警

待完善。

## 钉钉机器人告警

1. 安装钉钉机器人模块：`prometheus-webhook-dingtalk`

   ```shell
   tar -xvf prometheus-webhook-dingtalk-2.1.0.linux-amd64.tar.gz
   cd prometheus-webhook-dingtalk-2.1.0.linux-amd64
   ./prometheus-webhook-dingtalk 	# 启动
   ```

2. 配置钉钉机器人，编辑 `prometheus-webhook-dingtalk.yml` 文件：

   ```yml
   timeout: 5s
   templates:
     - ./dingtalk_template.tmpl	# 等下需要建立这个模版
   targets:
     webhook1:
       url: https://oapi.dingtalk.com/robot/send?access_token=	# 钉钉机器人信息
       secret: SEC71359c23757222339912ea4	# 钉钉机器人信息
   ```

3. 新建钉钉告警的模版：`dingtalk_template.tmpl`

   ```tmpl
   {{ define "__subject" }}
   [{{ .Status | toUpper }}{{ if eq .Status "firing" }}:{{ .Alerts.Firing | len }}{{ end }}]
   {{ end }}
   
   
   {{ define "__alert_list" }}{{ range . }}
   ---
   {{ if .Labels.owner }}@{{ .Labels.owner }}{{ end }}
   
   **告警主题**: {{ .Annotations.summary }}
   
   **告警类型**: {{ .Labels.alertname }}
   
   **告警级别**: {{ .Labels.severity }}
   
   **告警主机**: {{ .Labels.instance }}
   
   **告警信息**: {{ index .Annotations "description" }}
   
   **告警时间**: {{ dateInZone "2006.01.02 15:04:05" (.StartsAt) "Asia/Shanghai" }}
   {{ end }}{{ end }}
   
   {{ define "__resolved_list" }}{{ range . }}
   ---
   {{ if .Labels.owner }}@{{ .Labels.owner }}{{ end }}
   
   **告警主题**: {{ .Annotations.summary }}
   
   **告警类型**: {{ .Labels.alertname }}
   
   **告警级别**: {{ .Labels.severity }}
   
   **告警主机**: {{ .Labels.instance }}
   
   **告警信息**: {{ index .Annotations "description" }}
   
   **告警时间**: {{ dateInZone "2006.01.02 15:04:05" (.StartsAt) "Asia/Shanghai" }}
   
   **恢复时间**: {{ dateInZone "2006.01.02 15:04:05" (.EndsAt) "Asia/Shanghai" }}
   {{ end }}{{ end }}
   
   
   {{ define "default.title" }}
   {{ template "__subject" . }}
   {{ end }}
   
   {{ define "default.content" }}
   {{ if gt (len .Alerts.Firing) 0 }}
   **====侦测到{{ .Alerts.Firing | len  }}个故障====**
   {{ template "__alert_list" .Alerts.Firing }}
   ---
   {{ end }}
   
   {{ if gt (len .Alerts.Resolved) 0 }}
   **====恢复{{ .Alerts.Resolved | len  }}个故障====**
   {{ template "__resolved_list" .Alerts.Resolved }}
   {{ end }}
   {{ end }}
   
   
   {{ define "ding.link.title" }}{{ template "default.title" . }}{{ end }}
   {{ define "ding.link.content" }}{{ template "default.content" . }}{{ end }}
   {{ template "default.title" . }}
   {{ template "default.content" . }}
   ```

4. 启动 prometheus-webhook-dingtalk

   ```shell
   ./prometheus-webhook-dingtalk --config.file=prometheus-webhook-dingtalk.yml
   ```

5. 配置 `alertmanager.yml` ：

   ```yml
   route:
     group_by: ['dingtalk']
     group_wait: 30s
     group_interval: 5m
     repeat_interval: 1h
     receiver: 'dingtalk.webhook1'
     routes:
       - receiver: 'dingtalk.webhook1'
         match_re:
           alertname: ".*"
   
   receivers:
     - name: 'dingtalk.webhook1'
       webhook_configs:
         - url: 'http://192.168.2.11:8060/dingtalk/webhook1/send'
           send_resolved: true
   ```

6. 测试，将其中一个告警规则生效即可看到。


---
> 参考文档
>
> https://www.cnblogs.com/colin88/p/17108936.html
