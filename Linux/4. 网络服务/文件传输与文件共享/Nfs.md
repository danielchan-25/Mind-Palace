# 服务端安装
```shell
# Ubuntu
apt install nfs-common nfs-kernel-server
# Centos8 ARM
yum install nfs-utils rpcbind
```

```shell
# 创建共享目录
mkdir -p /data/share
chmod a+w /data/share
```

```shell
# 修改配置文件，添加共享目录
vim /etc/exports
/data/share 192.168.123.*(rw,sync,no_root_squash,no_subtree_check)
```

- `/data/share` ：要共享的目录
- `192.168.123.*` ：允许访问的网段，也可以是 IP 地址、主机名
- `(rw,sync,no_root_squash,no_subtree_check)`
    - `rw`：读/写权限
    - `sync`：数据同步写入内存和硬盘
    - `no_root_squash`：服务器允许远程系统以 root 特权存取该目录
    - `no_subtree_check`：关闭子树检查

```shell
# Ubuntu 启动
/etc/init.d/nfs-kernel-server restart

# Centos8 ARM 启动
service nfs-server start
service rpcbind start
```

# 客户端安装
```shell
# Ubuntu 安装
apt install nfs-common
# Centos8 ARM 安装
yum install nfs-utils

# 启动
systemctl start rpcbind
```

```shell
# 挂载
mkdir -p /data/share
mount -t nfs 10.211.55.15:/data/share /data/share
```


