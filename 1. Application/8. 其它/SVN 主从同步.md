# SVN 主从同步

## Windows

实验环境：

1. SVN服务端：VisualSVN Server
2. 主 SVN：192.168.1.43
3. 从 SVN：192.168.1.42

### 服务端配置

1. 确认服务器系统一致，主从 svn 版本号一致。取消 svn 的 https 认证，改为 http（80端口）

2. 主从 svn 都新建一个备份用户，用户名为：backup，用户密码随机复杂即可。

3. 在 **从库** 创建 与 主库相同 的 `Repositories`

4. 在 **每个从库** `Repositories` 的 host 目录 里添加文件：`pre-revprop-change.bat`，内容为空

5. 主svn 服务器上执行以下命令

   ```powershell
   svnsync init http://hostname:port/svn/从库 http://hostname:port/svn/主库 --source-username 主库用户名 --source-password 主库密码 --sync-username 从库用户名 --sync-password 从库密码
   
   svnsync sync http://hostname:port/svn/从库 --source-username 主库用户名 --source-password 主库密码 --sync-username 从库用户名 --sync-password 从库密码
   ```

6. 在 主库每个 `Repositories` 的 `hooks` 目录下创建文件：`post-commit.bat`

   ```powershell
   @echo off
   set SVN_HOME="D:\Program Files\VisualSVN Server"
   %SVN_HOME%\bin\svnsync sync --non-interactive http://hostname:port/svn/从库 --source-username 主库用户名 --source-password 主库密码 --sync-username 从库用户名 --sync-password 从库密码
   ```

### 客户端配置

需要在每台客户端上重新定位 svn 地址，不然无法连接，填上新的 svn 地址即可。