# KVM

# KVM优势

- KVM不需要桌面图形环境支持，能够在 Linux Server 版本下运行。
- KVM的各种操作（创建、修改、起停、状态查看、删除、克隆等等）都在命令行下进行，不需要依赖GUI，因此很方便集成到自己的应用中去（比如，你可以实现一个自动化的VPS售卖平台）。
- 网络更稳定。KVM是基于Linux内核的虚拟机（Kernel-based Virtual Machine，因此简称KVM），网络稳定性应该更好（目前使用过程还没有遇到类似的网络不稳定的问题）。

# 系统版本

```shell
root@abc:~# uname -a
Linux abc 5.15.0-56-generic #62-Ubuntu SMP Tue Nov 22 19:54:14 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

root@abc:~# lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.1 LTS
Release:	22.04
Codename:	jammy
```

# 检测是否支持

在进一步行动之前，首先需要检查你的 CPU 是否支持 KVM 虚拟化，确保你系统中有 VT-x（ vmx）英特尔处理器或 AMD-V（svm）处理器。

你可以通过运行如下命令，如果输出值大于 0，那么虚拟化被启用。否则，虚拟化被禁用，你需要启用它：

```shell
egrep -c '(vmx|svm)' /proc/cpuinfo
```

根据上方命令输出，你可以推断出虚拟化功能已经启用，因为输出结果大于 0。如果虚拟化功能没有启用，请确保在系统的 BIOS 设置中启用虚拟化功能。

另外，你可以通过如下命令判断 KVM 虚拟化是否已经在运行：

```shell
# 安装检查工具
apt install cpu-checker

# 使用命令检查是否支持kvm 
kvm-ok
# 出现如下信息则表示支持kvm虚拟化技术
INFO: /dev/kvm exists
KVM acceleration can be used
```

# 安装软件

```shell
# 安装必要的kvm软件
apt install -y \
qemu-kvm virt-manager libvirt-daemon-system virtinst libvirt-clients bridge-utils
```

- `qemu-kvm` – 一个提供硬件仿真的开源仿真器和虚拟化包
- `virt-manager` – 一款通过 libvirt 守护进程，基于 QT 的图形界面的虚拟机管理工具
- `libvirt-daemon-system` – 为运行 libvirt 进程提供必要配置文件的工具
- `virtinst` – 一套为置备和修改虚拟机提供的命令行工具
- `libvirt-clients` – 一组客户端的库和API，用于从命令行管理和控制虚拟机和管理程序
- `bridge-utils` – 一套用于创建和管理桥接设备的工具

启动软件

在所有软件包安装完毕之后，通过如下命令启用并启动 libvirt 守护进程：

```shell
systemctl enable --now libvirtd
systemctl start libvirtd

# 你可以通过如下命令验证该虚拟化守护进程是否已经运行：
systemctl status libvirtd
```

另外，请将当前登录用户加入 `kvm` 和 `libvirt` 用户组，以便能够创建和管理虚拟机。

```shell
# $USER 环境变量引用的即为当前登录的用户名。你需要重新登录才能使得配置生效。
usermod -aG kvm $USER
usermod -aG libvirt $USER
```

---

> 参考文档：
>
> http://bqzzd.cn/242.html