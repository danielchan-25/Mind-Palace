# 连接 Gitlab 服务器

步骤：
1. Gitlab操作
   1. 在仓库中添加访问令牌
2. Jenkins操作
   1. 安装 Gitlab插件
   2. 添加 Gitlab API 密钥（访问令牌），添加 Gitlab 账号密码
   3. 添加 Gitlab 地址等信息




# 连接客户端
### Linux
### Windows
如果我们项目的部署环境在 window 环境上，我们可以选择给服务器安装 openSSH 的方式，然后以脚本的方式进行部署。

**注意：Windows机器上需要有：`Java` `OpenSSH` 环境**

安装 OpenSSH 方法见：[https://github.com/danielchan-25/Mind-Palace/blob/main/3.%20Windows/%E5%AE%89%E8%A3%85OpenSSH.md](https://github.com/danielchan-25/Mind-Palace/blob/main/3.%20Windows/%E5%AE%89%E8%A3%85OpenSSH.md)
配置完成后，即可在 Jenkins 服务端中添加该客户端。

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Jenkins-1.png)
![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Jenkins-2.png)

- Remote root directory：填写 Windows 上的 Jenkins 目录，例如：E:\jenkins
- Labels：标签，可以填入 windows，方便指定某个流水线单独调用
- Usage：选 Only build jobs with label expressions matching this node
- Launch method：Launch agents via SSH，随后在下方填入 Windows 服务器的账号密码

依次填写信息即可，保存后，返回 Status 页面，提供了节点连接服务器的方式，在 Windows 上输入命令即可。


# 其它
## 安装中文插件

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Jenkins-3.png)
![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Jenkins-4.png)
