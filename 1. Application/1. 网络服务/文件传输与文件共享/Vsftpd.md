---
title: "Vsftpd"

---

# 1. 前言

`Vsftpd` 是 `“very secure TTP daemon”` 的缩写，是一个完全免费的、开放源代码的 `FTP` 服务器软件。

是一款在 `Linux` 发行版中最受推崇的 `FTP` 服务器程序，小巧轻快，安全易用，支持虚拟用户，支持带宽限制等功能。

# 2. FTP传输模式

> 文件传输协议（FTP），基于该协议FTP客户端与服务端可以实现共享文件、上传文件、下载文件。
>
> FTP客户端与服务端有两种传输模式，**FTP主动模式、FTP被动模式**。（主被动模式是以服务器为参照）

- **FTP主动模式**：客户端从一个任意的端口N（N>1024）连接到FTP服务器的port 21命令端口，客户端开始监听N+1端口，并发送FTP命令“ port N+1” 到服务器，FTP服务器以数据端口（20）连接到客户端指定的数据端口（N+1）。
- **FTP被动模式**：客户端从一个任意的端口N（N>1024）连接到FTP服务器的port 21命令端口，客户端开始监听N+1端口，客户端提交PASV命令，服务器会开始一个任意端口（P>1024），并发送“port p”命令给客户端。客户端发起从本地端口N+1到服务器的端口P的连接用来传送数据。
- 在企业实际环境中，如果FTP客户端与服务端均开放防火墙，FTP需以主动模式工作，这样只需要在FTP服务端防火墙规则中，开放20、21端口即可。

# 3. 安装

```shell
yum list | grep vsftpd					# 在yum列表中查询vsftpd
yum install vsftpd -y					# 使用yum安装vsftpd
service vsftpd start/stop/restart		# vsftpd的常用命令
systemctl start/stop/restart vsftpd		# vsftpd的常用命令
systemctl enable/disable vsftpd			# vsftpd的常用命令
ps -aux | grep vsftpd					# 查看vsftpd是否在运行
```

# 4. 配置

> [VsFTPd](https://pkgs.org/download/vsftpd)

`/etc/vsftpd/vsftpd.conf`

vsftpd的核心配置文件，请先备份再操作

```shell
# 是否允许匿名登录FTP服务器，默认设置为YES允许
# 用户可使用用户名ftp或anonymous进行ftp登录，口令为用户的E-mail地址。
# 如不允许匿名访问则设置为NO
anonymous_enable=YES

# 是否允许本地用户(即linux系统中的用户帐号)登录FTP服务器，默认设置为YES允许
# 本地用户登录后会进入用户主目录，而匿名用户登录后进入匿名用户的下载目录/var/ftp/pub
# 若只允许匿名用户访问，前面加上#注释掉即可阻止本地用户访问FTP服务器
local_enable=YES

# 是否允许本地用户对FTP服务器文件具有写权限，默认设置为YES允许
write_enable=YES

# 掩码，本地用户默认掩码为077
# 你可以设置本地用户的文件掩码为缺省022，也可根据个人喜好将其设置为其他值
local_umask=022

# 是否允许匿名用户上传文件，须将全局的write_enable=YES。默认为YES
anon_upload_enable=YES

# 是否允许匿名用户创建新文件夹
anon_mkdir_write_enable=YES 

# 是否激活目录欢迎信息功能
# 当用户用CMD模式首次访问服务器上某个目录时，FTP服务器将显示欢迎信息
# 默认情况下，欢迎信息是通过该目录下的.message文件获得的
# 此文件保存自定义的欢迎信息，由用户自己建立
dirmessage_enable=YES

# 是否让系统自动维护上传和下载的日志文件
# 默认情况该日志文件为/var/log/vsftpd.log,也可以通过下面的xferlog_file选项对其进行设定
# 默认值为NO
xferlog_enable=YES

# Make sure PORT transfer connections originate from port 20 (ftp-data).
# 是否设定FTP服务器将启用FTP数据端口的连接请求
# ftp-data数据传输，21为连接控制端口
connect_from_port_20=YES

# 设定是否允许改变上传文件的属主，与下面一个设定项配合使用
# 注意，不推荐使用root用户上传文件
chown_uploads=YES

# 设置想要改变的上传文件的属主，如果需要，则输入一个系统用户名
# 可以把上传的文件都改成root属主。whoever：任何人
chown_username=whoever

# 设定系统维护记录FTP服务器上传和下载情况的日志文件
# /var/log/vsftpd.log是默认的，也可以另设其它
xferlog_file=/var/log/vsftpd.log

# 是否以标准xferlog的格式书写传输日志文件
# 默认为/var/log/xferlog，也可以通过xferlog_file选项对其进行设定
# 默认值为NO
xferlog_std_format=YES

# 以下是附加配置，添加相应的选项将启用相应的设置
# 是否生成两个相似的日志文件
# 默认在/var/log/xferlog和/var/log/vsftpd.log目录下
# 前者是wu_ftpd类型的传输日志，可以利用标准日志工具对其进行分析；后者是vsftpd类型的日志
dual_log_enable

# 是否将原本输出到/var/log/vsftpd.log中的日志，输出到系统日志
syslog_enable

# 设置数据传输中断间隔时间，此语句表示空闲的用户会话中断时间为600秒
# 即当数据传输结束后，用户连接FTP服务器的时间不应超过600秒。可以根据实际情况对该值进行修改
idle_session_timeout=600

# 设置数据连接超时时间，该语句表示数据连接超时时间为120秒，可根据实际情况对其个修改
data_connection_timeout=120

# 运行vsftpd需要的非特权系统用户，缺省是nobody
nopriv_user=ftpsecure

# 是否识别异步ABOR请求。
# 如果FTP client会下达“async ABOR”这个指令时，这个设定才需要启用
# 而一般此设定并不安全，所以通常将其取消
async_abor_enable=YES

# 是否以ASCII方式传输数据。默认情况下，服务器会忽略ASCII方式的请求。
# 启用此选项将允许服务器以ASCII方式传输数据
# 不过，这样可能会导致由"SIZE /big/file"方式引起的DoS攻击
ascii_upload_enable=YES
ascii_download_enable=YES

# 登录FTP服务器时显示的欢迎信息
# 如有需要，可在更改目录欢迎信息的目录下创建名为.message的文件，并写入欢迎信息保存后
ftpd_banner=Welcome to blah FTP service.

# 黑名单设置。如果很讨厌某些email address，就可以使用此设定来取消他的登录权限
# 可以将某些特殊的email address抵挡住。
deny_email_enable=YES

# 当上面的deny_email_enable=YES时，可以利用这个设定项来规定哪些邮件地址不可登录vsftpd服务器
# 此文件需用户自己创建，一行一个email address即可
banned_email_file=/etc/vsftpd/banned_emails

# 用户登录FTP服务器后是否具有访问自己目录以外的其他文件的权限
# 设置为YES时，用户被锁定在自己的home目录中，vsftpd将在下面chroot_list_file选项值的位置寻找chroot_list文件
# 必须与下面的设置项配合
chroot_list_enable=YES

# 被列入此文件的用户，在登录后将不能切换到自己目录以外的其他目录
# 从而有利于FTP服务器的安全管理和隐私保护。此文件需自己建立
chroot_list_file=/etc/vsftpd/chroot_list

# 是否允许递归查询。默认为关闭，以防止远程用户造成过量的I/O
ls_recurse_enable=YES

# 是否允许监听。
# 如果设置为YES，则vsftpd将以独立模式运行，由vsftpd自己监听和处理IPv4端口的连接请求
listen=YES

# 设定是否支持IPV6。如要同时监听IPv4和IPv6端口，
# 则必须运行两套vsftpd，采用两套配置文件
# 同时确保其中有一个监听选项是被注释掉的
listen_ipv6=YES

# 设置PAM外挂模块提供的认证服务所使用的配置文件名，即/etc/pam.d/vsftpd文件
# 此文件中file=/etc/vsftpd/ftpusers字段，说明了PAM模块能抵挡的帐号内容来自文件/etc/vsftpd/ftpusers中
pam_service_name=vsftpd

# 是否允许ftpusers文件中的用户登录FTP服务器，默认为NO
# 若此项设为YES，则user_list文件中的用户允许登录FTP服务器
# 而如果同时设置了userlist_deny=YES，则user_list文件中的用户将不允许登录FTP服务器，甚至连输入密码提示信息都没有
userlist_enable=YES/NO

# 设置是否阻扯user_list文件中的用户登录FTP服务器，默认为YES
userlist_deny=YES/NO

# 是否使用tcp_wrappers作为主机访问控制方式。
# tcp_wrappers可以实现linux系统中网络服务的基于主机地址的访问控制
# 在/etc目录中的hosts.allow和hosts.deny两个文件用于设置tcp_wrappers的访问控制
# 前者设置允许访问记录，后者设置拒绝访问记录。
# 如想限制某些主机对FTP服务器192.168.57.2的匿名访问，编缉/etc/hosts.allow文件，如在下面增加两行命令：
# vsftpd:192.168.57.1:DENY 和vsftpd:192.168.57.9:DENY
# 表明限制IP为192.168.57.1/192.168.57.9主机访问IP为192.168.57.2的FTP服务器
# 此时FTP服务器虽可以PING通，但无法连接
tcp_wrappers=YES
```

`/etc/vsftpd/ftpusers`

这个文件是禁止使用vsftpd的用户列表文件。

记录不允许访问FTP服务器的用户名单，可以把一些对系统安全有威胁的用户账号记录在此文件中，以免用户以FTP登录后获得大于上传下载操作的权力，对系统造成损坏。

`/etc/vsftpd/user_list`

这个文件禁止或允许使用vsftpd的用户列表文件。

这个文件中指定的用户缺省情况（即在/etc/vsftpd/vsftpd.conf 中，设置userlist_deny=YES）下也不能访问FTP服务器，在设置了userlist_deny=NO 时，仅允许user_list 中指定的用户访问FTP服务器。

# 5. 传输模式配置

## 5.1 被动模式

```shell
connect_from_port_20=NO(默认为YES) #设置是否允许主动模式
pasv_enable=YES(默认为YES) #设置是否允许被动模式
pasv_min_port=50000(default:0(use any port))
pasv_max_port=60000(default:0(use any port))
```

## 5.2 主动模式

```shell
connect_from_port_20=YES
pasv_enable=NO
```

上边配置只是开启所需模式要求，其他配置看实际情况。

# 6. 用户访问模式

vsftpd服务访问模式有三种：**匿名用户模式、系统用户模式、虚拟用户模式**

## 6.1 匿名用户模式

vsftpd默认以匿名用户访问，匿名用户默认访问的FTP服务器路径：/var/ftp/pub

匿名用户只有查看权限，无法创建、删除、修改。

这种模式下，**不需改动配置文件**，直接启动服务即可。

如果要允许匿名用户能上传、下载、删除文件，需修改配置文件中：

```shell
anon_upload_enable=YES               #允许匿名用户上传文件；
anon_mkdir_write_enable=YES          #允许匿名用户创建目录；
anon_other_write_enable=YES          #允许匿名用户其他写入权限。
```

另外默认vsftpd匿名用户有两个：anonymous、ftp

所以匿名用户如果需要上传文件、删除以及修改等权限，需要ftp用户对 /var/ftp/pub/ 目录有写入权限。

## 6.2 系统用户模式

匿名模式可以让任何人使用FTP服务，比较公开，多适用于共享文件。

如果想要特定用户使用，需要使用系统用户登录访问，需要新建linux不同用户，然后修改配置文件

```shell
[root@server /]# useradd chengxiang
[root@server /]# passwd chengxiang

anonymous_enable=NO   #禁止匿名用户登录
chown_uploads=NO      #设定禁止上传文件更改宿主
nopriv_user=ftptest   #设定支撑Vsftpd服务的宿主用户为新建用户
ascii_upload_enable=YES
ascii_download_enable=YES #设定支持ASCII模式的上传和下载功能。
userlist_enable=YES
userlist_deny=NO
```

最后打开 **/etc/vsftpd/user_list/** 文件，将新建的用户添加到最后一行（一个用户一行）

这种模式下，登录访问的目录就是 /home/user/

## 6.3 虚拟用户模式

系统用户模式虽然可以控制访问，但是如果用户过多会影响服务器系统的管理，对服务器安全造成威胁。

那么就需要设置虚拟用户进行登录，这种更安全，**推荐！**

**虚拟用户就是没有实际的真实系统用户，而是通过映射到其中一个真实用户以及设置相应的权限来实现访问验证**，虚拟用户不能登录Linux系统。

首先要创建一个宿主用户，也就是要映射的真实用户，然后设置该用户不允许登陆系统

```shell
useradd virtualhost -s /sbin/nologin

# 设定不允许匿名访问
anonymous_enable=NO
# 设定本地用户可以访问，注意：主要是为虚拟宿主用户，如果该项目设定为NO那么所有虚拟用户将无法访问。
local_enable=YES
# 设定可以进行写操作
write_enable=YES
# 设定上传后文件的权限掩码
local_umask=022
# 禁止匿名用户上传
anon_upload_enable=NO
# 止匿名用户建立目录
anon_mkdir_write_enable=NO
# 定开启目录标语功能
dirmessage_enable=YES
# 定开启日志记录功能。
xferlog_enable=YES
# 定端口20进行数据连接。(主动模式)
connect_from_port_20=YES
# 定禁止上传文件更改宿主。
chown_uploads=NO
#chown_username=whoever
# 定Vsftpd的服务日志保存路径。注意，该文件默认不存在。必须要手动touch出来，并且由于这里更改了Vsftpd的服务宿主用户为手动建立的Vsftpd。必须注意给与该用户对日志的写入权限，否则服务将启动失败。
xferlog_file=/var/log/xferlog
# 设定日志使用标准的记录格式
xferlog_std_format=YES
# 设定空闲连接超时时间，单位为秒，这里默认
#idle_session_timeout=600
# 设定空闲连接超时时间，单位为秒，这里默认
#data_connection_timeout=120
#nopriv_user=ftptest
# 设定支持异步传输功能。
async_abor_enable=YES
ascii_upload_enable=YES
# 设定支持ASCII模式的上传和下载功能
ascii_download_enable=YES
# 设定Vsftpd的登陆标语。
ftpd_banner=Welcome to blah FTP service.
#deny_email_enable=YES
# (default follows)
#banned_email_file=/etc/vsftpd/banned_emails
# 禁止用户登出自己的FTP主目录。
chroot_list_enable=NO
# (default follows)
#chroot_list_file=/etc/vsftpd/chroot_list
# 禁止用户登陆FTP后使用"ls -R"的命令。该命令会对服务器性能造成巨大开销。如果该项被允许，那么挡多用户同时使用该命令时将会对该服务器造成威胁
ls_recurse_enable=NO
# 设定该Vsftpd服务工作在StandAlone模式下
listen=YES
#listen_ipv6=YES
# 设定userlist_file中的用户将不得使用FTP。
userlist_enable=YES
#userlist_deny=NO
# 设定支持TCP Wrappers
tcp_wrappers=YES
```

下边是关于虚拟用户的重要配置

```bash
guest_enable=YES #设定启用虚拟用户功能
guest_username=virtualhost #指定虚拟用户的宿主用户
virtual_use_local_privs=YES #设定虚拟用户的权限符合他们的宿主用户
pam_service_name=vsftpd #设定PAM服务下Vsftpd的验证配置文件名。因此，PAM验证将参考/etc/pam.d/下的vsftpd文件配置
user_config_dir=/etc/vsftpd/virtualconf #设定虚拟用户个人Vsftp的配置文件存放路径。也就是说，这个被指定的目录里，将存放每个Vsftp虚拟用户个性的配置文件，一个需要注意的地方就是这些配置文件名必须和虚拟用户名相同。
```

注意：

1. vsftpd的日志文件不存在，建立vsftpd的日志文件，并更改宿主为vsftpd的服务宿主用户。

   ```shell
   touch /var/log/vsftpd.log
   chown virtualhost.virtualhost /var/log/vsftpd.log
   ```

2. 建立虚拟用户配置文件存在路径

   ```shell
   # 这里是跟配置文件中的 user_config_dir 这一项是对应的
   mkdir /etc/vsftpd/virtualconf
   ```

3. 接着制作虚拟用户数据库文件

   ```shell
   # 安装环境：db4包，用来支持文件数据库
   yum install db4 -y
   # 建立虚拟用户名单文件
   touch /etc/vsftpd/virtusers
   # 建立了一个虚拟用户名单文件，这个文件用来记录vsftpd虚拟用户的用户名和口令的数据文件。
   # 我命名为 virtusers。为了避免文件混乱，我把这个名单文件放进 /etc/vsftpd/中
   # 继续编辑这个文件，将虚拟用户信息写入这个文件
   vim /etc/vsftpd/virtusers
   virtual1
   123456
   virtual2
   123456
   # 接着生成虚拟用户数据文件
   db_load -T -t hash -f /etc/vsftpd/virtusers /etc/vsftpd/virtusers.db
   ```

4. 设定PAM验证文件，并指定虚拟用户数据库文件进行读取

   ```shell
   # 安装环境
   yum install pam -y
   # vsftpd的PAM验证配置文件：/etc/pam.d/vsftpd/
   # 这里对应的就是核心配置文件中 pam_service_name
   # 它会去找 /etc/pam.d/vsftpd/ 这个文件
   # 编辑文件，先备份
   cp /etc/pam.d/vsftpd /etc/pam.d/vsftpd.bak
   vim /etc/pam.d/vsftpd
   #%PAM-1.0
   auth    sufficient      /lib/security/pam_userdb.so     db=/etc/vsftpd/virtusers
   account sufficient      /lib/security/pam_userdb.so     db=/etc/vsftpd/virtusers
   以上两条是手动添加，内容是对虚拟用户的安全和账户权限进行验证：
   auth：指对用户的用户名口令进行验证。
   accout：指对用户的账户有哪些权限 哪些限制进行验证。
   sufficient：表示充分条件，也就是说：一旦在这里通过验证，那么也就不用经过下面剩下的验证步骤了。
   /lib/security/pam_userdb.so/：表示该条审核将调用 pam_userdb.so 这个库函数进行。
   db=/etc/vsftpd/virtusers：指定了验证库函数将到这个指定的数据库中调用数据进行验证。
   ```

   注意：如果为 x64，则需要修改

   ```shell
   /lib64/security/pam_userdb.so
   ```

5. 配置虚拟用户

   ```shell
   # 规划好虚拟用户的主路径
   mkdir /opt/vsftpd/
   # 建立测试用户的FTP用户目录
   mkdir /opt/vsftpd/virtual1 /opt/vfstpd/virtual2
   # 建立虚拟用户配置文件模板
   cp /etc/vsftpd/vsftpd.conf.bak /etc/vsftpd/virtualconf/vconf.tmp
   # 定制虚拟用户模板配置文件
   vim /etc/vsftpd/virtualconf/vconf.tmp
   # 指定虚拟用户的具体主路径。
   local_root=/opt/vsftp/virtuser
   # 设定不允许匿名用户访问。
   anonymous_enable=NO
   # 设定允许写操作。
   write_enable=YES
   # 设定上传文件权限掩码。
   local_umask=022
   # 设定不允许匿名用户上传。
   anon_upload_enable=NO
   # 设定不允许匿名用户建立目录。
   anon_mkdir_write_enable=NO
   # 设定空闲连接超时时间。
   idle_session_timeout=600
   # 设定单次连续传输最大时间。
   data_connection_timeout=120
   # 设定并发客户端访问个数。
   max_clients=10
   # 设定单个客户端的最大线程数，这个配置主要来照顾Flashget、迅雷等多线程下载软件。
   max_per_ip=5
   # 设定该用户的最大传输速率，单位b/s。
   local_max_rate=50000
   ```

   这里将原vsftpd.conf 配置文件经过简化后保存作为虚拟用户配置文件的模板。

   并不需要指定太多配置内容，主要框架和限制由vsftpd.conf 来定义，即虚拟用户配置文件当中没有提到的配置项目将参考著主配置文件中的设定。

   而在这里作为虚拟用户的配置文件模板只需要留一些和用户流量控制，访问方式控制的配置项目就可以了。

   这里关键为 **local_root**，用来指定这个虚拟用户的FTP主路径。

   ```shell
   # 更改虚拟用户的主目录的属主为虚拟宿主用户
   chown -R virtualhost.virtualhost /opt/vsftpd
   # 配置虚拟用户，从虚拟用户模板配置文件复制
   cp /etc/vsftpd/virtualconf/vconf.tmp /etc/vsftpd/virtualconf/virtual1
   # 针对具体用户进行定制
   vim /etc/vsftpd/virtualconf/virtual1
   local_root=/opt/vsftp/virtual1
   anonymous_enable=NO
   write_enable=YES
   local_umask=022
   anon_upload_enable=NO
   anon_mkdir_write_enable=NO
   idle_session_timeout=300
   data_connection_timeout=90
   max_clients=1
   max_per_ip=1
   local_max_rate=25000
   ```

6. 测试

   1. 可以先在 /opt/vsftpd/virtual1/ 创建一个空文件
   2. 在windows - cmd - ftp ip
   3. 用户：virtual1 密码：123456
   4. 测试上传，put
   5. 测试建立目录，mkdir
   6. 测试下载，get，windows默认下载目录为 C:\Users\xxxx

7. 常见问题

   连接FTP后显示：Passive mode refused

   原因：FTP服务器为主动模式，客户端为被动模式了，导致不能正常访问

   解决办法：强制使用主动模式访问服务器即可

   `ftp>passive / passive off`

