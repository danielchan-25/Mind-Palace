---
title: "Time Zone"
date: 2024-04-20

---

# 时区

## 查看时区

使用 `date` 命令可以查看当前服务器的时区：

```shell
root@server:/# timedatectl
               Local time: Thu 2023-12-07 01:34:55 UTC
           Universal time: Thu 2023-12-07 01:34:55 UTC
                 RTC time: Thu 2023-12-07 01:34:56    
                Time zone: Etc/UTC (UTC, +0000)       
System clock synchronized: yes                        
              NTP service: n/a                        
          RTC in local TZ: no
```

## 修改时区

```shell
root@server:/# timedatectl set-timezone Asia/Shanghai

# 再次验证时区是否修改成功
root@server:/# timedatectl
               Local time: Thu 2023-12-07 09:37:11 CST
           Universal time: Thu 2023-12-07 01:37:11 UTC
                 RTC time: Thu 2023-12-07 01:37:12    
                Time zone: Asia/Shanghai (CST, +0800) 
System clock synchronized: yes                        
              NTP service: n/a                        
          RTC in local TZ: no
```

# 时间

同步服务器本地时间，可以使用 `NTP`（Network Time Protocol） 命令。

## 安装
```shell
yum install -y ntp
apt install -y ntp
```

## 使用

1. 编辑 `/etc/ntp.conf` 文件

2. 在配置文件中，找到 server 部分，注释掉默认的 NTP 服务器，并添加您要使用的 NTP 服务器。例如，添加以下行来使用中国的 NTP 服务器

```shell
server ntp.aliyun.com
```

3. 开启 ntp： `systemctl restart ntpd` `systemctl enable ntpd`

4. 同步时间：`ntpq -p`

## 常用的NTP服务器

### 阿里云

- ntp.aliyun.com
- ntp1.aliyun.com
- ntp2.aliyun.com
- ntp3.aliyun.com
- ntp4.aliyun.com
- ntp5.aliyun.com
- ntp6.aliyun.com
- ntp7.aliyun.com


### 腾讯

- time1.cloud.tencent.com
- time2.cloud.tencent.com
- time3.cloud.tencent.com
- time4.cloud.tencent.com
- time5.cloud.tencent.com

### 清华
- ntp.tuna.tsinghua.edu.cn