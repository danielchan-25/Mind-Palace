---
title: "Firewall"
date: 2019-01-12

---
# 介绍

Firewalld 是 CentOS 及其衍生发行版（如RHEL）中默认的动态防火墙管理工具。它提供了一种简化的方式来管理网络防火墙规则，并具有动态更新和配置更改的能力。Firewalld使用D-Bus系统总线来与网络管理器和其他系统组件进行通信。

# 常用命令

```shell
sudo systemctl start firewalld   # 启动Firewalld服务
sudo systemctl stop firewalld    # 停止Firewalld服务
sudo systemctl restart firewalld # 重启Firewalld服务

sudo systemctl status firewalld	 # 检查Firewalld服务状态
sudo systemctl enable firewalld	 # 设置开机启动
```

# 基本语法

```shell
sudo firewall-cmd --zone=public --add-service=http     # 添加HTTP服务规则到public区域
sudo firewall-cmd --zone=public --remove-service=http  # 从public区域删除HTTP服务规则

sudo firewall-cmd --zone=public --add-service=http --permanent  # 添加永久性HTTP服务规则到public区域
sudo firewall-cmd --reload  # 重载规则，使永久性设置生效


sudo firewall-cmd --list-all  # 显示所有区域和规则的详细信息
sudo firewall-cmd --zone=public --list-services  # 显示特定区域中启用的服务
```

