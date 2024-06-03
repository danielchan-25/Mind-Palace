---
date: 2024-06-03

---

`WSL` 是 `Windows` 平台上的工具，这里不过多介绍，直接进入安装教程。

# 安装

控制面板 -> 程序 -> 启用或关闭 Windows 功能，将这三个功能打开：`Hyper-V`, 适用于Linux的Windows子系统，虚拟机平台。

重启生效，同时也要启动CPU虚拟化。

# 使用说明

官方说明：[https://learn.microsoft.com/en-us/windows/wsl/](https://learn.microsoft.com/en-us/windows/wsl/)

常用命令：

```powershell
wsl.exe --help
wsl.exe -l -v  # 查看现有的子系统
wsl.exe --install -d Ubuntu-22.04  # 安装 Ubuntu22.04
```
