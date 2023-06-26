# Systemctl

# 简要
`CentOS 7` 的服务 `systemctl` 脚本存放在：`/usr/lib/systemd/`

有系统 `（system）` 和用户 `（user）` 之分

像需要开机不登陆就能运行的程序，还是存在系统服务里

即：`/usr/lib/systemd/system` 目录下每一个服务以 `.service` 结尾

一般会分为3部分：`[Unit]`、`[Service]` 和 `[Install]`

# 举例
这里以 `Mongo` 脚本示例，`Mongo` 脚本由于自定义，本人有很多参数没有写，但是以下面示例的参数，足够控制服务了。
```sh
[root@CentOS7 system]# cat /usr/lib/systemd/system/mongod.service 
[Unit]
Description=mongo
After=network.target 
 
[Service]
Type=forking
PIDFile=/usr/local/mongodb/tmp/mongod.pid
ExecStart=/usr/local/mongodb/bin/mongod -f /etc/mongod.conf.bak
ExecReload=/bin/kill -s HUP $MAINPID      #停止与重载写不写无所谓
ExecStop=/bin/kill -s QUIT $MAINPID
PrivateTmp=true
 
[Install]
WantedBy=multi-user.target
```
## [Unit]
`Description`：服务的简单描述
`Documentation`：服务文档
`Before, After`：定义启动顺序，Before=xxx.service，代表本服务在xxx.service启动之前启动。After=xxx.service,代表本服务在xxx之后启动。

## [Service]
`Type`：启动类型simple、forking、oneshot、notify、dbus

	Type=simple：默认值，执行ExecStart指定的命令，启动主进程
	Type=forking：以 fork 方式从父进程创建子进程，创建后父进程会立即退出
	Type=oneshot：一次性进程，Systemd 会等当前服务退出，再继续往下执行
	Type=notify：当前服务启动完毕，会通知Systemd，再继续往下执行

`PIDFile`：pid文件路径, pid文件,没有可以删除这行
`ExecStartPre`：启动前要做什么，比如是测试配置文件
`ExecStart`：启动
`ExecReload`：重载 
`ExecStop`：停止
`Restart`：定义服务何种情况下重启（启动失败，启动超时，进程被终结）。可选选项：no, on-success, on-failure,on-watchdog, on-abort
## [Install]
`Alias`：别名
`Also（可选）`：当目前这个 unit 本身被 enable 时，Also 后面接的 unit 也请 enable 的意思！也就是具有相依性的服务可以写在这里呢！
`WantedBy`：何种情况下，服务被启用。eg：WantedBy=multi-user.target（多用户环境下启用）