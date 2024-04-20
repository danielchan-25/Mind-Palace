---
title: "Limits"

date: 2024-01-21

---

# 前言

在 Linux 系统中，目录、字符设备、块设备、套接字、打印机等都被抽象成了文件，即通常所说的 “一切皆文件”。

`open files` 参数如果过小的话，会导致进程不能打开过多的文件。

不过这里的 files 不单是文件的意思，也包括打开的通讯链接(比如socket套接字)，正在监听的端口等等，所以有时候也可以叫做句柄(handle)。

此时应用程序就会报 `java.net.SocketException: Too many open files` 类似的错误，引起的原因就是进程在某个时刻打开了超过系统限制的文件数量以及通讯链接数。

# 为什么要限制打开文件数量？

因为操作系统需要内存来管理每个文件，所以可以打开的文件数可能会受到限制。由于程序也可以关闭文件处理程序，它可以创建任意大小的文件，直到所有可用磁盘空间都已满为止。在这种情况下，安全性的一个方面是通过施加限制来防止资源耗尽。

# 怎么查看打开文件数量？

可以使用 ` ulimit -a` 查看系统的 open files 参数值。

```shell
root@abc:~# ulimit -a
real-time non-blocking time  (microseconds, -R) unlimited
core file size              (blocks, -c) 0
data seg size               (kbytes, -d) unlimited
scheduling priority                 (-e) 0
file size                   (blocks, -f) unlimited
pending signals                     (-i) 31219
max locked memory           (kbytes, -l) 1013224
max memory size             (kbytes, -m) unlimited
open files                          (-n) 1024
pipe size                (512 bytes, -p) 8
POSIX message queues         (bytes, -q) 819200
real-time priority                  (-r) 0
stack size                  (kbytes, -s) 8192
cpu time                   (seconds, -t) unlimited
max user processes                  (-u) 31219
virtual memory              (kbytes, -v) unlimited
file locks                          (-x) unlimited
```

或者直接点，使用 `ulimit -n` 

```shell
root@abc:~# ulimit -n
1024
```

# 怎么修改打开文件数量限制？

涉及到 `open files` 一共是两个参数：

- ulimt 参数(这是对每个用户的限制)
- file-max 参数(这是Linuxt系统的总限制)

## ulimit

### ulimit -n 命令修改

**（只能对root用户生效）**

`ulimit` 命令可用来增加在 shell 中打开文件的数量。

这个命令是系统内置命令，因此它只影响bash和从它启动的程序。

`ulimit` 语法如下：

```shell
ulimit [选项] [限制数值]
```

下面选项决定了什么是有限的：

- `-a` 显示当前所有限制的报告
- `-f` (文件限制)限制shell能创建文件的大小
- `-n` 限制打开的文件描述符的数量。
- `-H`和`-S` 它们分别被设置为硬限制和软限制。硬限制可能不会随之增加，但软限制可能会增加。如果没有提供任何选项，ulimit将同时设置硬限制和软限制。

修改最大文件数量限制：

```shell
ulimit -n 65535
```

### 修改 limits.conf 文件

**（只能对root用户生效）**

可以对 `/etc/security/limits.conf` 文件进行修改，加入以下参数。

> `*` ：代表所有用户
>
> `-` ：超过文件句柄数时，什么都不干
>
> `soft` ：超过文件句柄数时，仅提示
>
> `hard` ：超过文件句柄数时，直接限制

```shell
* soft nofile 65535
* hard nofile 65535
* soft nproc 65535
* hard nproc 65535
```

修改完后再查看

```shell
root@abc:~# ulimit -n
65535
```

### 写入环境变量

由于退出该终端或重启后都会失效，所以需写入环境变量文件

```shell
vim /etc/profile
ulimit -n 65535
```

修改完后重启生效。

## sysctl.conf

配置文件：`/etc/sysctl.conf`

在文件末尾添加：

```shell
fs.nr_open = 6553560
fs.file-max = 6553560
```

> fs.nr_open：进程级别
>
> fs.file-max：系统级别
>
> fs.nr_open 默认设置的上限是 1048576，所以用户的 openfiles 不可能超过这个上限。
>
> fs.nr_open 总是应该小于等于 fs.file-max



---

> 参考文档：
>
> https://www.cnblogs.com/sxdcgaq8080/p/10690141.html
>
> https://www.jianshu.com/p/8b7e17b8c4ab
>
> https://zhuanlan.zhihu.com/p/414556142
>
> https://blog.csdn.net/y_zilong/article/details/121992311
