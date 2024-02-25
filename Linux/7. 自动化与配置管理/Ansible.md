# Ansible

命令执行过程

1. 加载自己的配置文件，默认`/etc/ansible/ansible.cfg`；
2. 查找对应的主机配置文件，找到要执行的主机或者组；
3. 加载自己对应的模块文件，如 command；
4. 通过ansible将模块或命令生成对应的临时py文件(python脚本)， 并将该文件传输至远程服务器；
5. 对应执行用户的家目录的`.ansible/tmp/XXX/XXX.PY`文件；
6. 给文件 +x 执行权限；
7. 执行并返回结果；
8. 删除临时py文件，`sleep 0`退出；

## 配置详解

### 程序结构

（yum安装）

配置文件目录：`/etc/ansible/`

执行文件目录：`/usr/bin/`

Lib库依赖目录：`/usr/lib/pythonX.X/site-packages/ansible/`

Help文档目录：`/usr/share/doc/ansible-X.X.X/`

Man文档目录：`/usr/share/man/man1/`

### 配置文件查找顺序

ansible与我们其他的服务在这一点上有很大不同，这里的配置文件查找是从多个地方找的，顺序如下：

1. 检查环境变量`ANSIBLE_CONFIG`指向的路径文件(export ANSIBLE_CONFIG=/etc/ansible.cfg)；
2. `~/.ansible.cfg`，检查当前目录下的ansible.cfg配置文件；
3. `/etc/ansible.cfg`检查etc目录的配置文件。

### ansible配置文件

ansible 配置文件：/etc/ansible/ansible.cfg

```sh
这是一些常见的参数
[defaults]
inventory = /etc/ansible/hosts		#这个参数表示资源清单inventory文件的位置
library = /usr/share/ansible		#指向存放Ansible模块的目录，支持多个目录方式，只要用冒号（：）隔开就可以
forks = 5		#并发连接数，默认为5
sudo_user = root		#设置默认执行命令的用户
remote_port = 22		#指定连接被管节点的管理端口，默认为22端口，建议修改，能够更加安全
host_key_checking = False		#设置是否检查SSH主机的密钥，值为True/False。关闭后第一次连接不会提示配置实例
timeout = 60		#设置SSH连接的超时时间，单位为秒
log_path = /var/log/ansible.log		#指定一个存储ansible日志的文件（默认不记录日志）
```

### 主机清单

在配置文件中，我们提到了资源清单，这个清单就是我们的主机清单，里面保存的是一些 ansible 需要连接管理的主机列表。我们可以来看看他的定义方式：

配置文件：`/etc/ansible/hosts`

```sh
1、 直接指明主机地址或主机名：
## green.example.com#
# blue.example.com#
# 192.168.100.1
# 192.168.100.10
2、 定义一个主机组[组名]把地址或主机名加进去
[client]
192.168.239.240
192.168.239.241
```

需要注意的是，这里的组成员可以使用通配符来匹配，这样对于一些标准化的管理来说就很轻松方便了。
　　我们可以根据实际情况来配置我们的主机列表，具体操作如下：

```sh
vim /etc/ansible/hosts
[client]
192.168.239.240
192.168.239.241
```

## 命令集

### 命令集

`/usr/bin/ansible`　　Ansibe AD-Hoc 临时命令执行工具，常用于临时命令的执行

`/usr/bin/ansible-doc` 　Ansible 模块功能查看工具

`/usr/bin/ansible-galaxy`　　下载/上传优秀代码或Roles模块 的官网平台，基于网络的

`/usr/bin/ansible-playbook`　　Ansible 定制自动化的任务集编排工具

`/usr/bin/ansible-pull`　　Ansible远程执行命令的工具，拉取配置而非推送配置（使用较少，海量机器时使用，对运维的架构能力要求较高）

`/usr/bin/ansible-vault`　　Ansible 文件加密工具

`/usr/bin/ansible-console`　　Ansible基于Linux Consoble界面可与用户交互的命令执行工具

其中，我们比较常用的是`/usr/bin/ansible`和`/usr/bin/ansible-playbook`。

### ansible-doc

ansible-doc 命令常用于获取模块信息及其使用帮助，一般用法如下：

```sh
ansible-doc -l				#获取全部模块的信息
ansible-doc -s MOD_NAME		#获取指定模块的使用帮助
ansible-doc copy			#查看copy模块使用方法
ansible-doc shell			#查看shell模块使用方法
```

## 语法

具体格式：

```sh
ansible <host-pattern> [-f forks] [-m module_name] [-a args]
```

```sh
-a MODULE_ARGS　　　#模块的参数，如果执行默认COMMAND的模块，即是命令参数，如： “date”，“pwd”等等
-k，--ask-pass #ask for SSH password。登录密码，提示输入SSH密码而不是假设基于密钥的验证
--ask-su-pass #ask for su password。su切换密码
-K，--ask-sudo-pass #ask for sudo password。提示密码使用sudo，sudo表示提权操作
--ask-vault-pass #ask for vault password。假设我们设定了加密的密码，则用该选项进行访问
-B SECONDS #后台运行超时时间
-C #模拟运行环境并进行预运行，可以进行查错测试
-c CONNECTION #连接类型使用
-f FORKS #并行任务数，默认为5
-i INVENTORY #指定主机清单的路径，默认为/etc/ansible/hosts
--list-hosts #查看有哪些主机组
-m MODULE_NAME #执行模块的名字，默认使用 command 模块，所以如果是只执行单一命令可以不用 -m参数
-o #压缩输出，尝试将所有结果在一行输出，一般针对收集工具使用
-S #用 su 命令
-R SU_USER #指定 su 的用户，默认为 root 用户
-s #用 sudo 命令
-U SUDO_USER #指定 sudo 到哪个用户，默认为 root 用户
-T TIMEOUT #指定 ssh 默认超时时间，默认为10s，也可在配置文件中修改
-u REMOTE_USER #远程用户，默认为 root 用户
-v #查看详细信息，同时支持-vvv，-vvvv可查看更详细信息
```

## 配置公私钥

```sh
yum -y install openssh-clientsansible
#1.生成私钥
ssh-keygen 
#2.向主机分发私钥
ssh-copy-id root@192.168.239.240
ssh-copy-id root@192.168.239.241
```

这样的话，就可以实现无密码登录，我们的实验过程也会顺畅很多

## 常用模块

### 命令模块

ping

```sh
ansible client -m ping
```

这样就说明我们的主机是连通状态的。接下来的操作才可以正常进行。

command

这个模块可以直接在远程主机上执行命令，并将结果返回本主机。

```sh
ansible client -m command -a 'free -h'
ansible client -m command -a 'df -h'
ansible client -m command -a 'whoami'
```

命令模块接受命令名称，后面是空格分隔的列表参数。

给定的命令将在所有选定的节点上执行。

它不会通过shell进行处理

比如 `$HOME` 和操作如 `"<"，">"，"|"，";"，"&"` 工作（需要使用（shell）模块实现这些功能）。

注意，该命令不支持`| `管道命令。

```sh
chdir：#在执行命令之前，先切换到该目录
#先切换到/data/ 目录，再执行“ls”命令
ansible client -m command -a 'chdir=/root ls' 

creates：#一个文件名，当这个文件存在，则该命令不执行，可以用来做判断
#如果/data/1.jpg存在，则不执行“s /root”命令，反之不存在，所以执行
ansible client -m command -a 'creates=/data/1.jpg ls /root' 

removes：#一个文件名，这个文件不存在，则该命令不执行
#如果/home/1.txt存在，则执行“yum install -y tree”命令
ansible client -m command -a 'removes=/home/1.txt yum install -y tree'
```

shell

shell模块可以在远程主机上调用shell解释器运行命令，支持shell的各种功能，例如管道等。

```sh
ansible client -m shell -a 'cat /etc/passwd | grep root'
ansible client -m shell -a '/home/hello.sh'
```

### 文件模块

copy

这个模块用于将文件复制到远程主机，同时支持给定内容生成文件和修改权限等。

```bash
src：#被复制到远程主机的本地文件。可以是绝对路径，也可以是相对路径。
#如果路径是一个目录，则会递归复制，用法类似于"rsync"
content：#用于替换"src"，可以直接指定文件的值
dest：#必选项，将源文件复制到的远程主机的绝对路径
backup：#当文件内容发生改变后，在覆盖之前把源文件备份，备份文件包含时间信息
directory_mode：#递归设定目录的权限，默认为系统默认权限
force：#当目标主机包含该文件，但内容不同时，设为"yes"，表示强制覆盖；
#设为"no"，表示目标主机的目标位置不存在该文件才复制。默认为"yes"
others：#所有的 file 模块中的选项可以在这里使用
```

举例

```bash
复制文件：
ansible client -m copy -a 'src=/root/centos7.sh dest=/home mode=0755'

给定内容生成文件，并制定权限：
ansible client -m copy -a 'content="I am keer" dest=/data/name mode=666'

覆盖文件
ansible client -m copy -a 'content="I am keery" backup=yes dest=/data/name mode=666'
```

fetch

从远程主机拉取文件到管理主机（和copy的功能相反），但是只能拉取单个文件（多个文件的话可以打包拉取）

`dest`：用来存放文件的目录
`src`：在远程拉取的文件，并且必须是一个**file**，不能是**目录**

```bash
ansible client -m fetch -a 'src=/home/1.txt dest=/home'
```

file

该模块主要用于设置文件的属性，比如创建文件、创建链接文件、删除文件等。

```bash
force：#需要在两种情况下强制创建软链接，一种是源文件不存在，但之后会建立的情况下；另一种是目标软链接已存在，需要先取消之前的软链，然后创建新的软链，有两个选项：yes|no
group：#定义文件/目录的属组。后面可以加上`mode`：定义文件/目录的权限
owner：#定义文件/目录的属主。后面必须跟上`path`：定义文件/目录的路径
recurse：#递归设置文件的属性，只对目录有效，后面跟上`src`：被链接的源文件路径，只应用于`state=link`的情况
dest：#被链接到的路径，只应用于`state=link`的情况

state：#状态，有以下选项：
    directory：#如果目录不存在，就创建目录
    file：#即使文件不存在，也不会被创建
    link：#创建软链接
    hard：#创建硬链接
    touch：#如果文件不存在，则会创建一个新的文件，如果文件或目录已存在，则更新其最后修改时间
    absent：#删除目录、文件或者取消链接文件

创建目录：
ansible client -m file -a 'path=/data/app state=directory'

创建链接文件：
ansible client -m file -a 'path=/data/bbb.jpg src=aaa.jpg state=link'

删除文件：
ansible web -m file -a 'path=/data/a state=absent'
```

### 其它常用

yum

yum软件包管理器安装，升级，降级，删除和列出软件包和组

```bash
name：#安装包的名称
state：#present(安装)/latest(安装最新的)/absent(卸载)
update_cache：#强制更新yum的缓存
conf_file：#指定远程yum安装时所依赖的配置文件

ansible client -m yum -a 'name=wget state=latest'
ansible client -m yum -a 'name=wget state=removed'
```

cron

该模块适用于管理`cron`计划任务的。
其使用的语法跟我们的`crontab`文件中的语法一致，同时，可以指定以下选项：

```bash
day：#日应该运行的工作( 1-31, *, */2, )
hour：#小时 ( 0-23, *, */2, )
minute：#分钟( 0-59, *, */2, )
month：#月( 1-12, *, /2, )
weekday：#周 ( 0-6 for Sunday-Saturday,, )
job：#指明运行的命令是什么
name：#定时任务描述
reboot：#任务在重启时运行，不建议使用，建议使用special_time
special_time：#特殊的时间范围，参数：reboot（重启时），annually（每年），monthly（每月），weekly（每周），daily（每天），hourly（每小时）
state：#指定状态，present表示添加定时任务，也是默认设置，absent表示删除定时任务
use：#以哪个用户的身份执行

添加计划任务：
ansible client -m cron -a 'name="ntp update every 5 min" minute=*/5 job="/sbin/ntpdate 172.17.0.1 &> /dev/null"'

删除计划任务:
ansible client -m cron -a 'name="df everyday" hour=15 job="df -lh >> /tmp/disk_total &> /dev/null" state=absent'
```

service

该模块用于服务程序的管理

```bash
name: #服务名
state: #started、stopped、restarted、reloaded
enabled: #yes、no

ansible client -m service -a 'name=nginx state=started enabled=true' 
```

---


参考文档

> https://www.cnblogs.com/keerya/p/7987886.html
> Windows客户端：https://zhuanlan.zhihu.com/p/572901058