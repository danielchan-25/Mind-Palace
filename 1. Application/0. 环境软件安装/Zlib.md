---
title: "Zlib"

---

> 官网地址: [Zlib](http://www.zlib.net/)

# 简介

Zlib是一个开源的数据压缩库，由Jean-loup Gailly和Mark Adler创建。它提供了一组用于压缩和解压缩数据的函数，以及一种通用的压缩文件格式（zlib格式）。

Zlib库使用DEFLATE算法来实现数据的无损压缩。DEFLATE算法是一种通用的压缩算法，结合了LZ77（一种字典压缩算法）和哈夫曼编码（一种编码技术）。DEFLATE算法广泛应用于许多应用程序和文件格式中，例如HTTP协议中的gzip压缩、PNG图像文件、ZIP压缩文件等。

Zlib库提供了简单易用的API函数，使开发人员可以轻松地在自己的应用程序中使用数据压缩和解压缩功能。它可以用于处理文件、网络传输的数据、内存中的数据等。Zlib还支持多种压缩级别，可以根据需求进行不同程度的压缩。

除了基本的数据压缩和解压缩功能，Zlib还提供了一些辅助函数，用于校验和计算、数据流处理、内存管理等。

由于其高效性、广泛的应用和良好的兼容性，Zlib已成为许多编程语言和操作系统中常用的数据压缩库。它被广泛应用于网络通信、文件压缩、数据存储等领域，提供了高效的数据压缩和解压缩解决方案。

# 部署

源码安装
```shell
wget http://www.zlib.net/zlib-1.2.13.tar.gz
tar -xvf zlib-1.2.13.tar.gz
cd zlib-1.2.13
./configure --prefix=/usr/local/zlib-1.2.13
make && make install
```