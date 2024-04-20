# Windows系统修改远程桌面端口

Windows系统的远程桌面端口默认是用的是 **3389** 端口，但是由于系统安全的考虑，经常我们安装好系统后一般都会把原来的 3389 端口更改为另外的端口。
将原来的远程桌面服务 3389 端口改为 **51001** 端口为例，具体操作过程如下

1. 打开注册表：`regedit`

2. 找到路径：`[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\Wds\rdpwd\Tds\tcp]`

   1. 双击右边 `PortNumber`
   2. 点击十进制
   3. 将值改为：51001
   4. 确定

   <img src="https://github.com/danielchan-25/danielchan-25.github.io/blob/master/images/posts/windows_rdp_port1.jpg" alt="show" />

3. 找到路径：`[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp]`

   1. 双击右边 `PortNumber`
   2. 点击十进制
   3. 将值改为：51001
   4. 确定

   <img src="https://github.com/danielchan-25/danielchan-25.github.io/blob/master/images/posts/windows_rdp_port2.jpg" alt="show" />

4. 重启电脑即可，记得先在防火墙放行，不然重启完后进不去