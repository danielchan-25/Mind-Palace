---
title: "Python库"
date: 2024-04-30

---

# TA-Lib

Github: [TA-Lib](https://github.com/TA-Lib/ta-lib-python)

系统：`Ubuntu 20.04.4 LTS`

1. 环境安装
```shell
apt update
apt install build-essential
apt install libtool autotools-dev automake pkg-config
```

2. 下载 ta-lib 包
```shell
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib

./configure --prefix=/usr
make -j4
make install -j4

ldconfig
```

3. 下载 TA-Lib Python 包
```shell
wget https://files.pythonhosted.org/packages/44/74/eddbc580f1486d55a831a04c2bd7e2e774a665e404f56d8ff30655f5cca6/TA-Lib-0.4.28.tar.gz
tar -xvf TA-Lib-0.4.28.tar.gz
cd TA-Lib-0.4.28
python setup.py install
```

4. 测试
重新开一个终端，执行
```shell
(py310) root@LJJServer:~# python
Python 3.10.0 (default, Mar  3 2022, 09:58:08) [GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import talib
>>> 
```
