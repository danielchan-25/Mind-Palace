---
title: "Kernel"
date: 2019-01-21

---

# 简介

内核是啥？

# 更换内核

## ubuntu

```shell
# 查看已有内核
dpkg -l | grep kernel

# 替换内核
## 先搜索出需要安装的内核版本，两个都要安装
apt-cache search linux | grep linux-image
apt-cache search linux | grep linux-headers
```

安装完后修改配置文件

配置文件：`/etc/default/grub`

- GRUB_DEFAULT：默认启动项
	数字：从0开始（按照开机选择界面的顺序对应）
	saved：默认上次的启动项
- GRUB_HIDDEN_TIMEOUT	是否隐藏菜单
	0：不隐藏，1：隐藏
- GRUB_HIDDEN_TIMEOUT_QUIET	是否显示等待倒计时
	true：不显示，false：显示
- GRUB_TIMEOUT	等候时间
	单位：s，默认10s，-1表示一直等待
- GRUB_GFXMODE	图形界面分辨率
	640x480

一般替换默认启动项即可，完成后执行：`update-grub`

重启生效，若卡住内核版本无法启动，开机时按住 `shift` 选择启动
