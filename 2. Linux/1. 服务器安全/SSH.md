---
title: "SSH"
date: 2018-04-12

---


在 Linux 中，SSH 服务尤为重要，所以有必要对 SSH 登录进行安全加固。

# 修改端口

配置文件：`/etc/ssh/sshd_config`

```shell
#Port 22
Port 23
```

# 开启 SSH 日志

开启 SSH 日志，能方便查看关于 SSH 的各种信息，如登录信息等。

1. 安装rsyslog

```shell
yum install rsyslog -y
```


2. 启动服务

```shell
systemctl start rsyslog && systemctl enable rsyslog
```

3. 修改配置

```shell
# 取消注释
/etc/ssh/sshd_config: SyslogFacility AUTHPRIV

/etc/rsyslog.conf
authpriv.*    /var/log/secure
service sshd retstart && service rsyslog restart

4. 查看日志

```shell
less -N /var/log/secure
```

# 安全配置
## IP黑名单

禁止特定 IP 登录 SSH

```shell
vim /etc/hosts.deny
sshd:192.168.1.1
ALL:192.168.1.1
```

## 登录认证

修改配置文件：`/etc/ssh/sshd_config`

```ini
PermitRootLogin no    # 禁止以root用户身份通过 SSH 登录
LogLevel INFO        # 将LogLevel设置为INFO,记录登录和注销活动
MaxAuthTries 3        # 限制单次登录会话的最大身份验证尝试次数
LoginGraceTime 20    # 缩短单次的登录宽限期，即ssh登录必须完成身份验证的时间 单位是秒
PasswordAuthentication no     # 禁止密码认证
PermitEmptyPasswords no     # 禁止空密码用户登录
```

## 设置连续错误登录后冻结

- 终端窗口登录：`/etc/pam.d/login`

- ssh远程登录：`/etc/pam.d/sshd `

```shell
auth required pam_tally2.so deny=3 unlock_time=5 even_deny_root root_unlock_time=10
# even_deny_root 也限制root用户；
# deny  设置普通用户和root用户连续错误登陆的最大次数，超过最大次数，则锁定该用户；
# unlock_time 设定普通用户锁定后，多少时间后解锁，单位是秒；
# root_unlock_time 设定root用户锁定后，多少时间后解锁，单位是秒；

# 此处使用的是 pam_tally2 模块，如果不支持 pam_tally2 可以使用 pam_tally 模块。另外，不同的pam版本，设置可能有所不同，具体使用方法，可以参照相关模块的使用规则。
```

### 查看用户登录失败次数

```shell
pam_tally2 --user 用户名
例：sudo pam_tally2 --user root
```

### 解除冻结用户

```shell
pam_tally2 --user 用户名 --reset
例：sudo pam_tally2 --user root --reset
```

