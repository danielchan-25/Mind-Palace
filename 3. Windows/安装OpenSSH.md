OpenSSH 下载地址：[https://github.com/PowerShell/Win32-OpenSSH/releases](https://github.com/PowerShell/Win32-OpenSSH/releases)

1. 下载后存放在：`C:\Program Files\OpenSSH`（必须存在这里）

2. 使用管理员打开 `cmd`
   ```powershell
   cd C:\Program Files\OpenSSH
   powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1  # 安装
   netsh advfirewall firewall add rule name=sshd dir=in action=allow protocol=TCP localport=22  # 添加入站规则
   sc config sshd start= auto  # 开机自启
   net start sshd  # 启动sshd服务
   ```
3. 测试：
   ```powershell
   ssh
   ssh administrator@127.0.0.1
   # 如果能输入密码登录，那就正常了
   ```
   
