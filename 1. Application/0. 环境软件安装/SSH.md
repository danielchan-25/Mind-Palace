# Windows
```powershell
# 安装 OpenSSH.Server，v0.0.1.0
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# 启动并设置服务开机自启
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# 允许防火墙通过 22 端口（默认 SSH 端口）
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

```
