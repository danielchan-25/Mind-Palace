> Jenkins 需要 JAVA 环境：
>
> Jenkins 下载地址：[https://www.jenkins.io/download/](https://www.jenkins.io/download/)
>
> Java 下载地址：[https://repo.huaweicloud.com/java/jdk/](https://repo.huaweicloud.com/java/jdk/)


## Linux

1. 部署 Tomcat
（Ps：Tomcat版本为：9.x.xx，10以上无法使用）

```sh
wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.68/bin/apache-tomcat-9.0.68.tar.gz
tar -xvf apache-tomcat-9.0.68.tar.gz
```

2. 部署 Jenkins

```sh
wget https://get.jenkins.io/war-stable/2.361.2/jenkins.war
mv jenkins.war ./apache-tomcat-9.0.68/webapps/.
```

3. 启动测试

```sh
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

## Windows
直接使用 `.msi` 文件安装即可