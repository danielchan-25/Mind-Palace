---
title: "Java"

---

> 官网地址：https://repo.huaweicloud.com/java/jdk/11.0.1+13/

apt 安装
```shell
apt install openjdk-17-jre

vim /etc/profile
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH

source /etc/profile
```