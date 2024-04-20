---
title: "ProxmoxVE"

---

# 概念
Qemu代理

Qemu 代理即 qemu-guest-agent，是一个运行在虚拟机里面的程序 qemu-guest-agent是一个帮助程序，守护程序，它安装在虚拟机中。 它用于在主机和虚拟机之间交换信息，以及在虚拟机中执行命令。

在Proxmox VE中，qemu代理主要用于两件事：

1、正确关闭虚拟机，而不是依赖ACPI命令或Windows策略

2、在进行备份时冻结来宾文件系统（在Windows上，使用卷影复制服务VSS）。

# 磁盘配置
扩容系统盘空间，在控制台中执行以下命令即可。
```shell
lvremove /dev/pve/data
lvextend -l +100%FREE -r /dev/pve/root
```

> 显卡直通：https://www.bilibili.com/read/cv26863115/?jump_opus=1