# KMS
## 简介
KMS的意思是：知识管理系统。全称是：Key Management Service

这个功能是在Windows Vista之后的产品中的一种新型产品激活机制，目的是为了Microsoft更好的遏制非法软件授权行为(盗版)。

计算机必须保持与KMS服务器的定期连接，以便KMS激活服务的自动检查实现激活的自动续期，这样就实现了限制于公司域内的激活范围，避免了对于外界计算机的非法授权。

可以在内网部署KMS服务，以达到计算机保持与KMS服务器的定期连接。

## 部署
使用 `docker-compose` 部署：
```yml
version: '2.9.0'
services:
  kms:
    image: teddysun/kms
    container_name: kms
    network_mode: bridge
    restart: always
    ports:
      - "1688:1688"
```
使用命令：`docker-compose up -d` 启动即可。


## 使用方法

以激活 Windows 为例：

在需要激活的电脑上打开命令行（以管理员权限打开）

输入：`slmgr /skms 10.17.174.54`

继续输入：`slmgr /ato`
