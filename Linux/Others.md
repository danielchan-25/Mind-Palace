# Others

## 桌面环境

Ubuntu 自带了 Gnome桌面，但如想在其它电脑上进行远程，无法实现，所以需安装 Xrdp
```bash
# 安装 xrdp
apt install xrdp
systemctl start xrdp && systemctl enable xrdp

# 添加用户进 xrdp 组：/etc/ssl/private/ssl-cert-snakeoil.key
adduser cc ssl-cert

# 查看 xrdp 端口
netstat -tnlp | grep 3389

# 配置环境变量
echo "gnome-session" > /home/cc/.xsession
```

## 更改系统语言

系统：`Ubuntu 22.04.1 LTS` ，以中文设置为英文为例，有两种方法：

1. 使用 `dpkg-reconfigure` 命令

   ```sh
   dpkg-reconfigure locales
   
   # 选择 en_US.UTF-8
   ```

2. 修改配置文件：`/etc/locale.gen`

   1. 将 `zh_CN.UTF-8` 注释
   2. 执行：`locale-gen`
   3. 重启系统
