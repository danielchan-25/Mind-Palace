# Zabbix

# 介绍

## 基本概念

Zabbix最重要的五个组成部分：

1. Item ——> 监控项 ——> 需要监控的内容
2. Trigger ——> 触发器 ——> 监控的内容满足什么条件时报警
3. Action ——> 动作 ——> 触发器出发时怎么告警
4. Media ——> 报警介质 ——> 告警采用什么方式
5. User ——> 用户 ——> 用户

## 监控功能

## 工作原理

一个监控系统运行的大概的流程是这样的：

Zabbix agent 需要安装到被监控的主机上，它负责定期收集各项数据，并发送到 server 端

Zabbix server 将数据存储到数据库中，zabbix web根据数据在前端进行展现和绘图。



这里agent收集数据分为主动和被动两种模式：

- 主动：agent 请求 server 获取主动的监控项列表，并主动将监控项内需要检测的数据提交给 server/proxy
- 被动：server 向 agent 请求获取监控项的数据，agent 返回数据。

## 组件及进程

Zabbix 由以下几个组件部分构成：

1. Zabbix Server：负责接收agent发送的报告信息的核心组件， 所有配置，统计数据及操作数据均由其组织进行；
2. Database Storage：专用于 存储所有配置信息，以及由zabbix收集的数据；
3. Web interface： zabbix的GUI接口，通常与Server运行在同一台主机上；
4. Proxy：可 选组件，常用于分布监控环境中，代理Server收集部分被监控端的监控数据并统一发往Server端；
5. Agent： 部署在被监控主机上，负责收集本地数据并发往Server端或Proxy端；

## 专有名词

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



1. 客户端配置调整

```ini
# 客户端的anent的模式，0表示关闭被动模式，zabbix-agentd不监控本地端口，所以看不到zabbix_agentd进程。
StartAgents=0

# 如果设置纯被动模式，应该注释掉这行
Server=172.16.100.84

# 主动模式的serverip地址
ServerActive=172.16.100.84

# 客户端的hostname，不配置则使用主机名
Hostname=172.16.100.47

# 被监控端到服务器获取监控项的周期，默认120S
RefreshActiveChecks=120

# 被监控端存储监控信息的空间大小
BufferSize=200

# 超时时间
Timeout=3

# 纯主动监控模式下的zabbix agent
# 只能支持zabbix agent (active)类型的监控项
```

2. 模版调整

克隆一个 `temple os linux` 模版来修改

# 监控项

## 自定义监控

### 监控终端在线人数

需求：限制登陆人数不超过三个，超过三人则发出警告。

1. 查看登陆人数命令

   ```shell
   [root@centos7-server /]# who am i | wc -l
   1
   ```

2. 在客户端创建 唯一key

   ```shell
   UserParameter=<key>,<shell command>
   
   vim zabbix/etc/zabbix_agentd.conf
   UserParameter=login-user,w | grep up | awk '{print $6}'
   ```

3. 重启客户端后，测试此 key 是否可用

   ```shell
   service zabbix_agentd restart
   ./zabbix_get -s 127.0.0.1 -p 10050 -k "login-user"
   1
   ```

4. 在web端进行配置

   1. 新增模板

      1. 模板名称：Login-user、群组：News

      2. 应用集：Server Security（任意）

      3. 监控项

         名称：Number of logged ind users

         键值：login-user

      4. 触发器

         名称：当前在线用户数量大于3个

         表达式：{Login-user:login-user.last()}>=3

      5. 图形名称：Number of logged in users

   2. 在需要监控的主机里，添加这个模板

5. 添加动作

   1. 名称：在线用户大于3个
   2. 条件
      1. 触发器 - 等于 - Login-user
   3. 操作
      1. 操作细节，添加发送用户，发送的信息

### 检测CPU温度

用于检测物理主机的 CPU 温度，需提前安装 **sensors** 该命令。

```shell
UserParameter=get_temperature_cpu,/usr/bin/sensors|grep 'Core 0'|cut -c 16-19|awk 'NR==1'
```

# 触发器

# 动作

动作模板

```ini
脚本参数：
{ALERT.SENDTO}
{ALERT.SUBJECT}
{ALERT.MESSAGE}
```

```ini
操作：
服务器:{HOST.NAME}发生: {TRIGGER.NAME}故障!
{
告警主机:{HOST.NAME}
主机分组:{TRIGGER.HOSTGROUP.NAME}
监控项目:{ITEM.NAME}
监控取值:{EVENT.VALUE}
告警等级:{TRIGGER.SEVERITY}
当前状态:{TRIGGER.STATUS}
告警信息:{TRIGGER.NAME}
告警时间:{EVENT.DATE} {EVENT.TIME}
事件ID:{EVENT.ID}
}

恢复：
服务器:{HOST.NAME}: {TRIGGER.NAME}已恢复!
{
告警主机:{HOST.NAME}
主机分组:{TRIGGER.HOSTGROUP.NAME}
监控项目:{ITEM.NAME}
监控取值:{EVENT.RECOVERY.VALUE}
告警等级:{TRIGGER.SEVERITY}
当前状态:{TRIGGER.STATUS}
告警信息:{TRIGGER.NAME}
告警时间:{EVENT.DATE} {EVENT.TIME}
恢复时间:{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME}
事件ID:{EVENT.ID}
}

更新：
服务器:{HOST.NAME}: 报警确认
{
确认人:{USER.FULLNAME}
时间:{ACK.DATE} {ACK.TIME}
确认信息如下:{ACK.MESSAGE}
问题服务器IP:{HOSTNAME1}
问题ID:{EVENT.ID}
当前的问题是: {TRIGGER.NAME}
}
```

# 告警媒介

## 邮件

具体安装见：

服务端添加邮件信息

   ```ini
   vim /etc/mail.rc
   # 添加以下内容
   set from=qq@qq.com	# 发件人
   set smtp=smtp.qq.com
   set smtp-auth-user=qq@qq.com		# 邮件登录名称
   set smtp-auth-password=qq		# 授权码
   set smtp-auth=login
   ```

测试

   ```shell
   echo "zabbix mail send test" | mail -s 'zabbix' qq@qq.com
   echo "Test" | mail -s "Title" qq@qq.com
   ```

## 钉钉机器人

*Python3环境*

1. 创建钉钉机器人，获取webhook值与secret值

2. 在服务端安装目录下找到配置文件，在配置文件里找出相关信息

   ```shell
   cat zabbix/etc/zabbix_server.conf | grep AlertScriptsPath
   ### Option: AlertScriptsPath
   # AlertScriptsPath=${datadir}/zabbix/alertscripts
   AlertScriptsPath=/data/programs/zabbix/share/zabbix/alertscripts
   
   cd /data/programs/zabbix/share/zabbix/alertscripts
   ```

3. 编写配置文件

   1. `vim dd_info.conf`：用于填写钉钉机器人的webhook值与secret值

      ```ini
      [config]
      log_path=/var/log/zabbix/zabbix_dd.log
      webhook=https://oapi.dingtalk.com/robot/send?access_token=
      secret=
      ```

   2. `vim dd.py`：钉钉告警程序

      ```python
      #!/usr/bin/env python3
      # coding:utf8
      import configparser
      import os
      import time
      import hmac
      import hashlib
      import base64
      import urllib.parse
      import requests
      import json
      import sys
      
      config = configparser.ConfigParser()
      config.read('/data/zabbix/alertscripts/dd_info.conf', encoding='utf-8')
      log_path = config.get('config', 'log_path')
      api_url = config.get('config', 'webhook')
      api_secret = config.get('config', 'secret')
      log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
      
      
      # 钉钉机器人文档说明
      # https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
      def get_timestamp_sign():
          timestamp = str(round(time.time() * 1000))
          secret = api_secret
          secret_enc = secret.encode('utf-8')
          string_to_sign = '{}\n{}'.format(timestamp, secret)
          string_to_sign_enc = string_to_sign.encode('utf-8')
          hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
          sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
          return timestamp, sign
      
      # 获取加签后的链接
      def get_signed_url():
          timestamp, sign = get_timestamp_sign()
          webhook = api_url + "&timestamp=" + timestamp + "&sign=" + sign
          return webhook
      
      # 定义消息模式
      def get_webhook(mode):
          if mode == 0:  # only 关键字
              webhook = api_url
          elif mode == 1 or mode == 2:  # 关键字和加签 或 # 关键字+加签+ip
              webhook = get_signed_url()
          else:
              webhook = ""
              print("error! mode:   ", mode, "  webhook :  ", webhook)
          return webhook
      
      
      def get_message(text, user_info):
          # 和类型相对应，具体可以看文档 ：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
          # 可以设置某个人的手机号，指定对象发送
          message = {
              "msgtype": "text",  # 有text, "markdown"、link、整体跳转ActionCard 、独立跳转ActionCard、FeedCard类型等
              "text": {
                  "content": text  # 消息内容
              },
              "at": {
                  "atMobiles": [
                      user_info,
                  ],
                  "isAtAll": False  # 是否是发送群中全体成员
              }
          }
          return message
      
      
      # 消息发送日志
      def log(info):
          if os.path.exists(log_path):
              log_file = open(log_path, "a+")
          else:
              log_file = open(log_path, "w+")
          log_file.write(info)
      
      
      def send_ding_message(text, user_info):
          # 请求的URL，WebHook地址
          # 主要模式有 0 ： 关键字 1：# 关键字 +加签 3：关键字+加签+IP
          webhook = get_webhook(1)
          # 构建请求头部
          header = {
              "Content-Type": "application/json",
              "Charset": "UTF-8"
          }
          # 构建请求数据
          message = get_message(text, user_info)
          # 对请求的数据进行json封装
          message_json = json.dumps(message)
          # 发送请求
          info = requests.post(url=webhook, data=message_json, headers=header).json()
          code = info["errcode"]
          errmsg = info["errmsg"]
          if code == 0:
              log(log_time + ":消息已发送成功 返回信息:%s %s\n" % (code, errmsg))
          else:
              log(log_time + ":消息发送失败 返回信息:%s %s\n" % (code, errmsg))
              print(log_time + ":消息发送失败 返回信息:%s %s\n" % (code, errmsg))
              exit(3)
      
      
      if __name__ == "__main__":
          text = sys.argv[3]
          user_info = sys.argv[1]
          send_ding_message(text, user_info)
      ```

4. 测试脚本

   ```shell
   ./dd.py (钉钉号) subject test
   ```

5. 测试通过后，在 web 添加钉钉告警即可。

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