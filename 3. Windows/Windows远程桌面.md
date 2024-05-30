## 远程桌面提示："由于没有远程桌面授权服务器可以提供许可证..."

### 临时解决方案

可以使用以下命令，强制进远程桌面

```powershell
mstsc /admin /v:IP地址
```

### 永久解决方案

删除 `GracePeriod` 注册表键

全路径：`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\RCM\GracePeriod`

1. 将 `GracePeriod` 给 `administrator` 授予 **完全控制权限** 后，删除里面的 `L$RTMTIMEBOMB...`

2. 在 **服务** 中找到 `Remote Desktop Services` ，重新启动后，成功。
