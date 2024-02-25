# Ansible

## 服务端

### 源码包部署

> 源码包：https://releases.ansible.com/ansible/ansible-2.9.9.tar.gz

```shell
tar -xvf ansible-2.9.9.tar.gz
cd ansible-2.9.9/
pip install -r requirements.txt
```

### pip安装

```shell
yum install -y python-pip
pip install ansible

# pip 安装后需要手动创建目录以及配置文件
mkdir -p /etc/ansible
touch /etc/ansible/ansible.cfg
# 将 https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg 配置文件复制进去即可
ansible --version # 检测一下配置文件
```

### yum安装

```shell
yum install http://mirrors.163.com/centos/7.4.1708/extras/x86_64/Packages/epel-release-7-9.noarch.rpm
yum install ansible –y
```
## 客户端
#### Windows
服务器下载并安装Microsoft .NET Framework 4.5和powershell5.1
```powershell
#可以用命令确定一版本不合格请先升级安装。
PS C:\Windows\system32> get-host
Name             : ConsoleHost
Version          : 5.1.17763.2931
InstanceId       : fe8b1f38-bb62-477a-aafe-4fbc99e87c08
UI               : System.Management.Automation.Internal.Host.InternalHostUserInterface
CurrentCulture   : zh-CN
CurrentUICulture : zh-CN
PrivateData      : Microsoft.PowerShell.ConsoleHost+ConsoleColorProxy
DebuggerEnabled  : True
IsRunspacePushed : False
Runspace         : System.Management.Automation.Runspaces.LocalRunspace
```
更改powershell执行策略为remotesigned
```powershell
PS C:\Windows\system32> set-executionpolicy remotesigned
执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): y
```
按照下面命令开启WinRM 远程管理，如果是下面报错请所有网络为专用模式后重试。
```powershell
PS C:\Windows\system32> winrm quickconfig
已在此计算机上运行 WinRM 服务。
WSManFault
    Message
        ProviderFault
            WSManFault
                Message = 由于此计算机上的网络连接类型之一设置为公用，因此 WinRM 防火墙例外将不运行。 
将网络连接类型更改为域或专用，然后再次尝试。

错误编号: -2144108183 0x80338169
由于此计算机上的网络连接类型之一设置为公用，因此 WinRM 防火墙例外将不运行。 将网络连接类型更改为域或专用，
然后再次尝试
```
请确认防火墙已放行 **5985/tcp** 端口

查看winrm service listener启动监听状态
```powershell
PS C:\Windows\system32> winrm enumerate winrm/config/listener
Listener
    Address = *
    Transport = HTTP
    Port = 5985
    Hostname
    Enabled = true
    URLPrefix = wsman
    CertificateThumbprint
    ListeningOn = 127.0.0.1, 169.254.21.153, 169.254.29.178, 169.254.73.237, 169.254.211.164, 192.168.76.177, 192.168.123.6, ::1, fe80::490:f6a2:47a9:49ed%7, fe80::1da2:7c3:84eb:8a46%22, fe80::5de7:82fa:489:1db2%13, fe80::61cd:d854:52ec:9f2c%15, fe80::c45b:2708:c937:d3a4%8, fe80::e5e6:ea99:681c:1599%19
```
为winrm service 启用远程连接认证，注意最后几个引号别错了:

```powershell
PS C:\Windows\system32> winrm set winrm/config/service/auth '@{Basic="true"}'
Auth
    Basic = true
    Kerberos = true
    Negotiate = true
    Certificate = false
    CredSSP = false
    CbtHardeningLevel = Relaxed
```
为winrm service 配置允许非加密,这里如果有其他公用网络也会报错：
```powershell
PS C:\Windows\system32> winrm set winrm/config/service '@{AllowUnencrypted="true"}'
Service
    RootSDDL = O:NSG:BAD:P(A;;GA;;;BA)(A;;GR;;;IU)S:P(AU;FA;GA;;;WD)(AU;SA;GXGW;;;WD)
    MaxConcurrentOperations = 4294967295
    MaxConcurrentOperationsPerUser = 1500
    EnumerationTimeoutms = 240000
    MaxConnections = 300
    MaxPacketRetrievalTimeSeconds = 120
    AllowUnencrypted = true
    Auth
        Basic = true
        Kerberos = true
        Negotiate = true
        Certificate = false
        CredSSP = false
        CbtHardeningLevel = Relaxed
    DefaultPorts
        HTTP = 5985
        HTTPS = 5986
    IPv4Filter = *
    IPv6Filter = *
    EnableCompatibilityHttpListener = false
    EnableCompatibilityHttpsListener = false
    CertificateThumbprint
    AllowRemoteAccess = true
```

到此，Windows 客户端已经完成设置了，接下来要设置服务端

```shell
pip install pywinrm
```

测试连接：`vim wintest.py`

```python
import winrm

session = winrm.Session('http://IP地址:5985/wsman', auth=('测试账户', '测试密码'))

res = session.run_cmd('ipconfig')
print(res.status_code)
print(res.std_out.decode('gbk'))
```