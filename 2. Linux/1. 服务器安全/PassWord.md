---
title: "PassWord"
date: 2018-01-12

---

# 使用

为用户新建、修改密码，都使用以下命令：

```shell
passwd root		# 输入密码，密码不可见
```



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
