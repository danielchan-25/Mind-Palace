---
title: "Jenkins"

date: 2024-04-20

---

官网: [Jenkins](https://www.jenkins.io/download/)

# 部署

## 源码部署

1. 部署 Tomcat
（Ps：Tomcat版本为：9.x.xx，10以上无法使用）

```shell
wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.68/bin/apache-tomcat-9.0.68.tar.gz
tar -xvf apache-tomcat-9.0.68.tar.gz
```

2. 部署 Jenkins

```shell
wget https://get.jenkins.io/war-stable/2.361.2/jenkins.war
mv jenkins.war ./apache-tomcat-9.0.68/webapps/.
```

3. 启动测试

```shell
./apache-tomcat-9.0.68/bin/startup.sh
```

4. Nginx设置反向代理（可选）

```nginx
server {
	listen  80;
	server_name     cc0235.tpddns.cn;

	location / {
		root    html;
		index   index.html index.php;
	}

	location /jenkins {
		proxy_pass      http://127.0.0.1:8080/jenkins;
		proxy_set_header Host $host:$proxy_port;
		proxy_set_header X-Real_IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_max_temp_file_size 0;
		client_max_body_size       10m;
		client_body_buffer_size    128k;

		proxy_connect_timeout      90;
		proxy_send_timeout         90;
		proxy_read_timeout         90;

		proxy_temp_file_write_size 64k;
		proxy_http_version 1.1;
		proxy_request_buffering off;
		proxy_buffering off;
	}
}
```


# 使用
## 连接服务器
### Linux
### Windows
如果我们项目的部署环境在 window 环境上，我们可以选择给服务器安装 openSSH 的方式，然后以脚本的方式进行部署。

**注意：Windows机器上需要有：`Java` `OpenSSH` 环境**

安装 OpenSSH
Github: [OpenSSH](https://github.com/PowerShell/Win32-OpenSSH/releases)

```powershell
# 解压zip包后，使用管理员方式的 cmd，进入到 OpenSSH 目录，执行以下命令：
powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1

# 设置自启动
sc config sshd start= auto
net start sshd
```

连接测试

```cmd
# 在 Windows 的终端中输入：
ssh administrator@127.0.0.1
```

配置完成后，即可在 Jenkins 服务端中添加该客户端。

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Jenkins-1.png)
![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Jenkins-2.png)

依次填写信息即可，保存后查看日志是否正常。


## 其它
### 安装中文插件

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Jenkins-3.png)
![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Jenkins-4.png)


---
# 参考文档
> [修改端口](https://www.cnblogs.com/heartxkl/p/12943904.html)