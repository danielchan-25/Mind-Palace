# Cobbler
# 1. 服务端部署

## 1.1 安装环境

```bash
systemctl stop firewalld && systemctl disable firewalld
setenforce 0
sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/sysconfig/selinux
```

## 1.2 开始部署

```bash
yum -y install epel-release
yum -y install cobbler cobbler-web tftp-server dhcp httpd xinetd pykickstart syslinux fence-agents
systemctl start httpd tftp cobblerd rsyncd
systemctl enable httpd tftp cobblerd rsyncd
```

## 1.3 排错

```bash
cobbler check

1 : The 'server' field in /etc/cobbler/settings must be set to something other than localhost, or kickstarting features will not work.  This should be a resolvable hostname or IP for the boot server as reachable by all machines that will use it.
2 : For PXE to be functional, the 'next_server' field in /etc/cobbler/settings must be set to something other than 127.0.0.1, and should match the IP of the boot server on the PXE network.
3 : change 'disable' to 'no' in /etc/xinetd.d/tftp
4 : Some network boot-loaders are missing from /var/lib/cobbler/loaders, you may run 'cobbler get-loaders' to download them, or, if you only want to handle x86/x86_64 netbooting, you may ensure that you have installed a *recent* version of the syslinux package installed and can ignore this message entirely.  Files in this directory, should you want to support all architectures, should include pxelinux.0, menu.c32, elilo.efi, and yaboot. The 'cobbler get-loaders' command is the easiest way to resolve these requirements.
5 : enable and start rsyncd.service with systemctl
6 : debmirror package is not installed, it will be required to manage debian deployments and repositories
7 : ksvalidator was not found, install pykickstart
8 : The default password used by the sample templates for newly installed machines (default_password_crypted in /etc/cobbler/settings) is still set to 'cobbler' and should be changed, try: "openssl passwd -1 -salt 'random-phrase-here' 'your-password-here'" to generate new one
9 : fencing tools were not found, and are required to use the (optional) power management features. install cman or fence-agents to use them

Restart cobblerd and then run 'cobbler sync' to apply changes.
```

针对上面的问题，逐个逐个解决即可。

```bash
1. cobbler setting edit --name=server --value=IP地址
2. cobbler setting edit --name=next_server --value=IP地址
3. sed -ri '/disable/c\disable = no' /etc/xinetd.d/tftp
4. cobbler get-loaders
	yum install -y syslinux
	cp /usr/share/syslinux/pxelinux.0 /var/lib/cobbler/loaders/
	cp /usr/share/syslinux/menu.c32 /var/lib/cobbler/loaders/
	(若cobbler get-loaders遇到网络异常，可开多个终端多次尝试即可解决)
5. systemctl enable xinetd && systemctl restart xinetd
7. yum -y install pykickstart
8. openssl passwd -1 -salt 'random-phrase-here' 'admin'
9. yum install -y fence-agents
```

排到最后只剩这个即可

```bash
cobbler check


The following are potential configuration items that you may want to fix:

1 : debmirror package is not installed, it will be required to manage debian deployments and repositories

Restart cobblerd and then run 'cobbler sync' to apply changes.
```

# 2. 配置文件

```bash
cobbler     									# cobbler程序包
cobbler-web  									# cobbler的web服务包
pykickstart  									# cobbler检查kickstart语法错误
httpd     									  # Apache web服务
 
/etc/cobbler                  # 配置文件目录
/etc/cobbler/settings         # cobbler主配置文件
/etc/cobbler/dhcp.template    # DHCP服务的配置模板
/etc/cobbler/tftpd.template   # tftp服务的配置模板
/etc/cobbler/rsync.template   # rsync服务的配置模板
/etc/cobbler/iso              # iso模板配置文件目录
/etc/cobbler/pxe              # pxe模板文件目录
/etc/cobbler/power            # 电源的配置文件目录
/etc/cobbler/users.conf       # Web服务授权配置文件
/etc/cobbler/users.digest     # web访问的用户名密码配置文件
/etc/cobbler/dnsmasq.template # DNS服务的配置模板
/etc/cobbler/modules.conf     # Cobbler模块配置文件
/var/lib/cobbler              # Cobbler数据目录
/var/lib/cobbler/config       # 配置文件
/var/lib/cobbler/kickstarts   # 默认存放kickstart文件
/var/lib/cobbler/loaders      # 存放的各种引导程序
/var/www/cobbler              # 系统安装镜像目录
/var/www/cobbler/ks_mirror    # 导入的系统镜像列表
/var/www/cobbler/images       # 导入的系统镜像启动文件
/var/www/cobbler/repo_mirror  # yum源存储目录
/var/log/cobbler              # 日志目录
/var/log/cobbler/install.log  # 客户端系统安装日志
/var/log/cobbler/cobbler.log  # cobbler日志
```

需开启的服务：

```bash
systemctl start tftp dhcpd cobblerd rsyncd httpd
```

# 3. DHCP服务器

`/etc/cobbler/settings`

```bash
cobbler setting edit --name=manage_dhcp --value=1

cat /etc/cobbler/settings
manage_dhcp: 1
```

```bash
vim /etc/cobbler/dhcp.template
subnet 192.168.239.0 netmask 255.255.255.0 {
     option routers             192.168.239.2;
     option domain-name-servers 192.168.239.128;
     option subnet-mask         255.255.255.0;
     range dynamic-bootp        192.168.239.100 192.168.239.254;
     default-lease-time         21600;
     max-lease-time             43200;
     next-server                $next_server;
     class "pxeclients" {
          match if substring (option vendor-class-identifier, 0, 9) = "PXEClient";
          if option pxe-system-type = 00:02 {
                  filename "ia64/elilo.efi";
          } else if option pxe-system-type = 00:06 {
                  filename "grub/grub-x86.efi";
          } else if option pxe-system-type = 00:07 {
                  filename "grub/grub-x86_64.efi";
          } else if option pxe-system-type = 00:09 {
                  filename "grub/grub-x86_64.efi";
          } else {
                  filename "pxelinux.0";
          }
     }
}
```

```bash
systemctl restart cobblerd && cobbler sync
dhcpd
cat /etc/dhcp/dhcpd.conf 
(！这步骤一定要做！查看dhcpd.conf配置有没有同步，不然启动报错！)
此时可以开另一台客户端测试，使用网卡启动，看是否能获取到DHCP地址

可能遇到的问题：
客户端在获取DHCP时卡住，然后查看/var/log/message报错：Error code 0: TFTP Aborted
cp /usr/share/syslinux/pxelinux.0 /var/lib/cobbler/loaders/
cp /usr/share/syslinux/menu.c32 /var/lib/cobbler/loaders/
即可
```

# 4.镜像

## 4.1 挂载镜像

```bash
mkdir -p /centos7
mkdir -p /var/www/html/centos7
mount -o loop CentOS-7-x86_64-Minimal-1908.iso /centos7/
cp -fr /centos7/* /var/www/html/centos7
```

查看挂载的镜像

```bash
ls /var/www/html/centos7/
CentOS_BuildTag  EFI  EULA  GPL  images  isolinux  LiveOS  Packages  repodata  RPM-GPG-KEY-CentOS-7  RPM-GPG-KEY-CentOS-Testing-7  TRANS.TBL
```

## 4.2 导入镜像

```bash
cobbler import --path=/var/www/html/centos7 --name=centos7.7 --arch=x86_64
# --path 镜像路径
# --name 为安装源定义一个名字
# --arch 指定安装源是32位、64位、ia64, 目前支持的选项有: x86│x86_64│ia64
# 安装源的唯一标示就是根据name参数来定义，本例导入成功后，安装源的唯一标示就是：centos6.9，如果重复，系统会提示导入失败。
```

查看导入后的信息

```bash
[root@192 html]# cobbler distro report --name=centos7.7-x86_64
Name                           : centos7.7-x86_64
Architecture                   : x86_64
TFTP Boot Files                : {}
Breed                          : redhat
Comment                        : 
Fetchable Files                : {}
Initrd                         : /var/www/cobbler/ks_mirror/centos7.7-x86_64/images/pxeboot/initrd.img
Kernel                         : /var/www/cobbler/ks_mirror/centos7.7-x86_64/images/pxeboot/vmlinuz
Kernel Options                 : {}
Kernel Options (Post Install)  : {}
Kickstart Metadata             : {'tree': 'http://@@http_server@@/cblr/links/centos7.7-x86_64'}
Management Classes             : []
OS Version                     : rhel7
Owners                         : ['admin']
Red Hat Management Key         : <<inherit>>
Red Hat Management Server      : <<inherit>>
Template Files                 : {}
```

查看profile信息

```bash
cobbler profile report --name=centos7.7-x86_64
[root@192 html]# cobbler profile report --name=centos7.7-x86_64
Name                           : centos7.7-x86_64
TFTP Boot Files                : {}
Comment                        : 
DHCP Tag                       : default
Distribution                   : centos7.7-x86_64
Enable gPXE?                   : 0
Enable PXE Menu?               : 1
Fetchable Files                : {}
Kernel Options                 : {}
Kernel Options (Post Install)  : {}
Kickstart                      : /var/lib/cobbler/kickstarts/sample_end.ks
Kickstart Metadata             : {}
Management Classes             : []
Management Parameters          : <<inherit>>
Name Servers                   : []
Name Servers Search Path       : []
Owners                         : ['admin']
Parent Profile                 : 
Internal proxy                 : 
Red Hat Management Key         : <<inherit>>
Red Hat Management Server      : <<inherit>>
Repos                          : []
Server Override                : <<inherit>>
Template Files                 : {}
Virt Auto Boot                 : 1
Virt Bridge                    : xenbr0
Virt CPUs                      : 1
Virt Disk Driver Type          : raw
Virt File Size(GB)             : 5
Virt Path                      : 
Virt RAM (MB)                  : 512
Virt Type                      : kvm
```

# 5. KS文件

## 5.1 初始KS文件

（类似用U盘安装，无自动应答）

```shell
vim /var/lib/cobbler/kickstarts/centos7.ks
#platform=x86, AMD64, or Intel EM64T
#version=DEVEL
# Install OS instead of upgrade
install
# Keyboard layouts
keyboard 'us'
# System language
lang en_US
# System authorization information
auth  --useshadow  --passalgo=sha512
# Use graphical install
graphical
# SELinux configuration
selinux --disabled
# Do not configure the X Window System
skipx


# Firewall configuration
firewall --disabled
# Halt after installation
halt
# System timezone
timezone Africa/Abidjan
# Use network installation
url --url="http://192.168.239.128/centos7/"
# System bootloader configuration
bootloader --location=none
# Partition clearing information
clearpart --all
```

动态编辑指定使用新的kickstart文件

```bash
cobbler profile edit --name=centos7.7-x86_64 --kickstart=/var/lib/cobbler/kickstarts/centos7.ks
```

验证是否成功

```bash
cobbler profile report --name=centos7.7-x86_64 |grep Kickstart
Kickstart: /var/lib/cobbler/kickstarts/centos7.ks

cobbler sync
重启客户端查看DHCP是否能获取
```

## 5.2 自定义KS文件

如不熟悉自定义KS文件，可使用centos7里自带的kickstart工具进行自定义

```bash
# 先安装桌面
yum -y groups install "GNOME Desktop"
# 运行桌面
startx
yum install system-config-kickstart
```

这里写好了一份KS文件，仅供参考

```bash
# platform=x86, AMD64, or Intel EM64T
# version=DEVEL
# Install OS instead of upgrade
install
# Keyboard layouts
keyboard 'us'
# Root password
rootpw --iscrypted $1$7jXKb6BU$n5Hvx51DMbLR.YDg6y5Y21
# System language
lang en_US
# System authorization information
auth  --useshadow  --passalgo=sha512
# Use graphical install
graphical
firstboot --disable
# SELinux configuration
selinux --disabled

text
# Firewall configuration
firewall --disabled
# Network information
network  --bootproto=dhcp --device=ens33
# Halt after installation
halt
# System timezone
timezone Asia/Shanghai
# Use network installation
url --url="http://192.168.239.130/centos7"
# System bootloader configuration
bootloader --location=mbr
# Clear the Master Boot Record
zerombr
# Partition clearing information
clearpart --all --initlabel
# Disk partitioning information
part / --fstype="xfs" --size=5120
part /boot --fstype="xfs" --size=800
part swap --fstype="swap" --size=8192
reboot
%packages --nobase
@core
%end
```





参考文档

> https://www.cnblogs.com/clsn/p/7833333.html#auto-id-7