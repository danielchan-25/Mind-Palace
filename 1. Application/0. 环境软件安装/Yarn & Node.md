# Yarn & Node

```shell
# 添加 Node.js apt 仓库
# 首先，使用 curl 命令从 NodeSource 的 PGP keys 服务器上下载 Node.js 的签名密钥：
curl -sL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -

# 然后，添加 Node.js 12.x 的 apt 仓库：
sudo add-apt-repository "deb https://deb.nodesource.com/node_12.x $(lsb_release -s -c) main"
升级 Node.js

sudo apt-get update
sudo apt-get install yarn nodejs
```