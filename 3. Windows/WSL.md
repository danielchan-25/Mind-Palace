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



# 其它

## 安装报错
- `WslRegisterDistribution failed with error: 0x800701bc`

更新 WSL2：[https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

- `0x80370102`

使用 PowerShell 管理员执行以下命令后重启：`bcdedit /set hypervisorlaunchtype auto`

## 迁移

```powershell
wsl --export Ubuntu-22.04 D:\wsl\Ubuntu-22.04.tar  # 导出镜像
wsl --unregister Ubuntu-22.04  # 注销现有的发行版
wsl --import Ubuntu-22.04 D:\wsl\Ubuntu-22.04 D:\wsl\Ubuntu-22.04.tar --version 2  # 在新位置导入发行版
wsl -d Ubuntu-22.04  # 启动
```
