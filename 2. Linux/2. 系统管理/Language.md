---
title: "Language"
date: 2024-01-21

---

# 查看语言

# 修改语言

系统：`Ubuntu 22.04.1 LTS` ，以中文设置为英文为例，有两种方法：

1. 使用 `dpkg-reconfigure` 命令

   ```shell
   dpkg-reconfigure locales
   
   # 选择 en_US.UTF-8
   ```

2. 修改配置文件：`/etc/locale.gen`

   1. 将 `zh_CN.UTF-8` 注释
   2. 执行：`locale-gen`
   3. 重启系统