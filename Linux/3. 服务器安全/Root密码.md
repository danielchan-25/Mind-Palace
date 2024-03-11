# 忘记Root密码
> https://www.feiqueyun.cn/zixun/fuwuqi/97424.html

1. 启动时按 `e`

2. 找到 `linux16` 这行，在最后添加：`rd.break`

3. 按 Ctrl+X 保存，以单用户模式启动

4. 输入：
	```shell
	mount -o remount,rw /sysroot
	chroot /sysroot
	passwd root
	---
	exit 
	reboot
	```
