# Openssl
> 官网地址：https://www.openssl.org/source/

## 简介

OpenSSL是一个开源的软件库，提供了用于安全通信的密码学功能和相关的工具。它由Eric A. Young和Tim Hudson创建，并以BSD风格的许可证发布。

OpenSSL库提供了各种密码学算法和协议的实现，包括对称加密、非对称加密、散列函数、数字签名、证书管理等。它支持的加密算法包括AES、RSA、DSA、Diffie-Hellman、ECC等，以及常用的协议如SSL（Secure Sockets Layer）和TLS（Transport Layer Security）。

OpenSSL提供了一组API函数，使开发人员可以在自己的应用程序中使用密码学功能来实现安全通信和数据保护。它可以用于创建安全的网络连接、加密和解密数据、生成和验证数字证书、处理密码学密钥等。

除了密码学功能，OpenSSL还提供了一些与安全相关的实用工具，如命令行工具`openssl`，用于生成证书、管理密钥、执行加密操作等。`openssl`命令行工具还可以用于测试和调试安全连接，执行各种密码学操作，并提供与SSL/TLS协议相关的功能。

由于其广泛的应用和可靠性，OpenSSL已成为许多操作系统和应用程序的标准安全库。它被用于保护网络通信、加密敏感数据、创建数字证书、实现安全协议等各种安全应用场景。

## 安装

源码安装

```shell
wget https://www.openssl.org/source/openssl-3.0.7.tar.gz
tar -xvf openssl-3.0.7.tar.gz
cd openssl-3.0.7
./config --prefix=/usr/local/openssl
make && make install
```