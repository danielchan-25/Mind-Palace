# 服务器生成密钥访问

基于服务器安全，建议服务器关闭密码登录，基于ssh密钥进行连接登录。

## 服务端

1. 输入命令：`ssh-keygen -t rsa` ，如果不需要设置密钥密码就进行三次回车键生成密钥对文件。
2. 进入：`/root/.ssh/`  目录，该目录下会生成四个文件
   1. `id_rsa`：私钥
   2. `id_rsa.pub`：公钥
   3. `authorized_keys`：
   4. `known_hosts`：
3. 将公钥的内容输入到 `authorized_keys`  中，即可使用该公钥访问该服务器。
4. 赋予  `authorized_keys`  **660**  权限。
