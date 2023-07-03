# Windows修改鼠标滚轮方向

## 背景

从 macOS 转到 windows 系统最不适应的就是鼠标的滚轮方向，用久了 MacBook 的触控板和鼠标滚动方向，windows 的 “反向操作” 极度不舒适。

## 解决方法

1. 计算机管理中找到鼠标的：设备实例路径，记录下里面的 **值**

2. 打开注册表编辑器，找到这个路径：

   `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\HID`

3. 在里面找到鼠标的 **值** 的路径，里面有个 `Device Parameter`

4. 双击右侧的 `FlipFlopWheel` ，将 数值数据由 0 改为 1，确定。

5. 重新插拔鼠标 USB。



> 参考文档：https://blog.csdn.net/weixin_42306148/article/details/117526821