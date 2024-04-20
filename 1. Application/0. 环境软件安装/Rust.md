---
title: "Rust"
date: 2024-04-19
---

# 源码包安装

环境：`Ubuntu 18.04` 

1. 下载源码包

   ```shell
   wget 
   tar -xvf 
   cd 
   ```

2. 编辑配置文件

   ```toml
   [install]
   # Instead of installing to /usr/local, install to this path instead.
   prefix = "~/rust"
   ```

3. 构建安装

   ```shell
   ./x.py build
   ./x.py install
   ```


---

>  参考文档
>
> Github: [rust](https://github.com/rust-lang/rust)
>
> [从源码安装 Rust](https://www.jianshu.com/p/63ce92182dbf)
