---
title: "System Backup"
date: 2023-10-12

---

# 系统备份
由于 Linux 系统所有都是文件，只需要将系统打包即可。一般用以下两种办法：
- 系统压缩：一种为直接将所有文件进行压缩而后在新装的系统中对其进行解压，解压后替换原有文件
- `systemback` 工具：可直接进行安装

## 备份前准备
对系统中的临时文件、日志文件以及一些不需要的文件进行删除，以减少不必要的文件被备份了，并且会导致备份文件太大。

## 开始备份
### 系统压缩
系统压缩思路比较简单，即在根目录下进行所有文件的压缩。在新装好的系统中解压文件，注意如果不在同一电脑/同一硬盘需要更改硬盘号。
可以直接通过 `tar` 对整个文件系统 「/」进行备份，有以下几点要注意：
不能备份以下几个文件/目录
1. 当前压缩文件
2. `/proc`
3. `/lost+found`
4. `/mnt`
5. `/sys`
6. `/media`

所以命令为：
```shell
# -p 代表当前权限
tar -zcvfp backup.tar.gz --exclude=/proc --exclude=/lost+found --exclude=/backup.tar.gz --exclude=/mnt --exclude=/sys --exclude=/media /
```

在备份命令结束时你可能会看到这样一个提示：`tar: Error exit delayed from previous errors`，多数情况下你可以忽略它。

# 系统还原
## 在本机还原
Linux可以再正在远行的系统中还原系统，如果当前启动无法启动，可以通过live cd来启动并执行恢复操作
```shell
tar xvpfz backup.tar.gz -C /
```
需要额外创建目录（正在运行的系统不需要）
`proc` `lost+found` `mnt` `sys`

## 在其它机器上还原
如果备份系统想要恢复到其他机器上，确保系统版本及内核版本一致时可以使用以下命令，增加排除`/dev`、`/etc/fstab`、`/boot`这三个路径，命令如下
```shell
# 备份
tar cvpzf backup.tar.gz --exclude=/proc --exclude=/lost+found --exclude=/dev --exclude=/etc/fstab --exclude=/boot  --exclude=/backup.tar.gz --exclude=/mnt --exclude=/sys --exclude=/media /

# 还原
tar xvpfz backup.tar.gz -C /
```


参考文档：

> https://www.cnblogs.com/chenjiye/p/11332387.html
