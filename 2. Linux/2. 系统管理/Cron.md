---
title: "Cron"
date: 2024-04-20

---

> 官网: [Cron](https://crontab.guru/)

# 时间说明
```shell
# .---------------- minute (0 - 59) 
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ... 
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)  OR
#sun,mon,tue,wed,thu,fri,sat 
# |  |  |  |  |
# *  *  *  *  *  command to be executed
```

# 语法

- 星号（*）：代表所有可能的值，例如month字段如果是星号，则表示在满足其它字段的制约条件后每月都执行该命令操作。

- 逗号（,）：可以用逗号隔开的值指定一个列表范围，例如，“1,2,5,7,8,9”。

- 中杠（-）：可以用整数之间的中杠表示一个整数范围，例如“2-6”表示“2,3,4,5,6”。

- 正斜线（/）：可以用正斜线指定时间的间隔频率，例如“0-23/2”表示每两小时执行一次。同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。

使用命令时，**务必所有命令均使用绝对路径**，因环境变量不同

# 使用

开启 `Cron` 日志功能：

编辑`/etc/rsyslog.d/50-default.conf`，将 `#cron` 取消注释，重启 `rsyslog` & `cron` 服务。

在定时任务中，百分号（%）和括号（()）等字符都被视为特殊字符，它们在crontab语法中具有特殊的含义。为了避免这个问题，你可以使用反斜杠（\）进行字符转义，或者将整个命令包含在引号中。

每条 JOB 执行完毕之后，系统会自动将输出发送邮件给当前系统用户。日积月累，非常的多，甚至会撑爆整个系统。所以每条 JOB 命令后面进行重定向处理是非常必要的： >/dev/null 2>&1 。前提是对 Job 中的命令需要正常输出已经作了一定的处理, 比如追加到某个特定日志文件.

如：
```shell
54 23 * * * cat /etc/rc.local > rc.local_`date "+%F"`
# 改成：
54 23 * * * cat /etc/rc.local > rc.local_`date "+\%F"`
```


新创建的cron job，不会马上执行，至少要过2分钟才执行。如果重启 cron 则马上执行。

```shell
systemctl restart crond
```


# 环境变量
文件路径：`/etc/crontab`

```ini
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
```

解释：前四行是用来配置crond任务运行的环境变量

- 第一行SHELL变量指定了系统要使用哪个shell，这里是bash；

- 第二行PATH变量指定了系统执行命令的路径；

- 第三行MAILTO变量指定了crond的任务执行信息将通过电子邮件发送给root用户，如果MAILTO变量的值为空，则表示不发送任务执行信息给用户；

- 第四行的HOME变量指定了在执行命令或者脚本时使用的主目录。

## 转义
在定时任务中，百分号（%）和括号（()）等字符都被视为特殊字符，它们在crontab语法中具有特殊的含义。为了避免这个问题，你可以使用反斜杠（\）进行字符转义，或者将整个命令包含在引号中。

```shell
54 23 * * * cat /etc/rc.local > rc.local_`date "+%F"`
# 改成：
54 23 * * * cat /etc/rc.local > rc.local_`date "+\%F"`
```



# 实例
```shell
30 21 * * * /usr/local/etc/rc.d/lighttpd restart   # 每晚的21:30重启apache。
45 4 1,10,22 * * /usr/local/etc/rc.d/lighttpd restart  # 每月1、10、22日的4 : 45重启apache。
10 1 * * 6,0 /usr/local/etc/rc.d/lighttpd restart  # 每周六、周日的1 : 10重启apache。
0,30 18-23 * * * /usr/local/etc/rc.d/lighttpd restart   # 每天18 : 00至23 : 00之间每隔30分钟重启apache。
0 23 * * 6 /usr/local/etc/rc.d/lighttpd restart   # 每星期六的11 : 00 pm重启apache。
* */1 * * * /usr/local/etc/rc.d/lighttpd restart   # 每一小时重启apache
* 23-7/1 * * * /usr/local/etc/rc.d/lighttpd restart    # 晚上11点到早上7点之间，每隔一小时重启apache
0 11 4 * mon-wed /usr/local/etc/rc.d/lighttpd restart    # 每月的4号与每周一到周三的11点重启apache
0 4 1 jan * /usr/local/etc/rc.d/lighttpd restart     # 一月一号的4点重启apache
*/30 * * * * /usr/sbin/ntpdate 210.72.145.44     # 每半小时同步一下时间

50 23 * * * docker exec -i liangjunjie bash -c "/root/auto_push.sh"		# 每天23:50启动容器里的 /root/auto_push.sh 脚本
```

---

参考文档
> https://zhuanlan.zhihu.com/p/58719487
