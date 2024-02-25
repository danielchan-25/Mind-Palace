# Pcre

> 官网地址：https://www.pcre.org/

## 简介

PCRE（Perl Compatible Regular Expressions）是一个正则表达式库，提供了与Perl语言兼容的正则表达式功能。它由Philip Hazel开发，最初是作为邮件服务器软件Exim的一部分而创建的。PCRE库支持广泛的正则表达式语法，并提供了强大的模式匹配和处理能力。

PCRE库可以在许多编程语言中使用，包括C、C++、Python、PHP等。它提供了一套API函数和正则表达式的语法规则，允许开发人员使用正则表达式模式来进行文本搜索、匹配、替换等操作。

PCRE的特点包括：

1. 支持Perl兼容的正则表达式语法：PCRE库支持Perl的正则表达式语法，包括元字符、字符类、重复限定符、分组和捕获、反向引用等。这使得使用熟悉Perl的开发人员可以无缝地在其他编程语言中使用PCRE进行模式匹配。

2. 强大的模式匹配功能：PCRE库提供了丰富的模式匹配功能，包括正向匹配、反向匹配、全局匹配、多行匹配等。它支持各种匹配选项和模式修饰符，可以灵活地进行高级的模式匹配操作。

3. Unicode支持：PCRE库对Unicode字符集的支持相当完善，可以处理各种Unicode字符属性、编码和字符集范围。

4. 高效性能：PCRE库经过优化，提供了高效的模式匹配性能。它使用了自动机和编译器等技术，能够在大规模的文本数据上快速进行模式匹配。

由于PCRE具有强大的正则表达式功能和广泛的语言支持，它在文本处理、字符串匹配、数据验证等方面得到了广泛的应用。无论是在编写脚本还是开发复杂的应用程序，PCRE都提供了一种灵活且功能丰富的工具来处理文本和模式匹配的需求。

## 安装

源码安装
```shell
wget https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.40/pcre2-10.40.tar.gz
tar -xvf pcre2-10.40.tar.gz
cd pcre2-10.40
./configure --prefix=/usr/local/pcre-10.4
make && make install
```
apt 安装

```shell
apt install build-essential
apt install libtool
apt install libpcre3-dev
apt install libpcre3
```