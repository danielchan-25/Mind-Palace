---
title: "GitLab"

---

# 安装

在 `/etc/yum.repos.d/` 下新建 `gitlab-ce.repo`，写入如下内容：
```ini
[gitlab-ce]
name=gitlab-ce
baseurl=https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/
gpgcheck=0
enabled=1
```

```shell
yum clean all && yum makecache
yum install gitlab-ce
```

配置后台地址：修改 `/etc/gitlab/gitlab.rb` 的 `external_url`

重载配置文件：`gitlab-ctl reconfigure`

查看 GitLab 状态：`gitlab-ctl status`

查看 Root 初始密码：`cat /etc/gitlab/initial_root_password`

修改默认端口
```shell
vim /var/opt/gitlab/gitlab-rails/etc/gitlab.yml

gitlab:
	## Web server settings (note: host is the FQDN, do not include http://)
	host: 10.17.174.90
	port: 8081
	https: false
```
```shell
vim /var/opt/gitlab/nginx/conf/gitlab-http.conf

server {
  #listen *:80;
  listen *: 8081;
```
```shell
# 这个可有可无
vim /var/opt/gitlab/gitlab-rails/etc/unicorn.rb
#listen "127.0.0.1:8080", :tcp_nopush => true
listen "127.0.0.1:端口号2,如9080", :tcp_nopush => true
```
```shell
vim /var/opt/gitlab/gitlab-shell/config.yml
#gitlab_url: "http://127.0.0.1:8080"
gitlab_url: "http://127.0.0.1:8081"
```

```shell
重启：gitlab-ctl restart
# 注意，不可以运行 gitlab-ctl reconfigure
```

# 目录说明
```shell
gitlab组件日志路径：/var/log/gitlab
gitlab配置路径：/etc/gitlab/  # 路径下有gitlab.rb配置文件
应用代码和组件依赖程序：/opt/gitlab
各个组件存储路径： /var/opt/gitlab/
仓库默认存储路径   /var/opt/gitlab/git-data/repositories
版本文件备份路径：/var/opt/gitlab/backups/
nginx安装路径：/var/opt/gitlab/nginx/
redis安装路径：/var/opt/gitlab/redis
```

# 常用命令
```shell
#查看服务状态
gitlab-ctl status
使用控制台实时查看日志
# 查看所有的logs; 按 Ctrl-C 退出
gitlab-ctl tail
# 拉取/var/log/gitlab下子目录的日志
gitlab-ctl tail gitlab-rails
# 拉取某个指定的日志文件
gitlab-ctl tail nginx/gitlab_error.log
#启动关闭gitlab	
gitlab-ctl start      
gitlab-ctl stop                                #停止            
gitlab-ctl status                              #查看状态
gitlab-ctl restart                             #重启
gitlab-ctl reconfigure			   #更新配置文件
gitlab-ctl help                                #帮助
gitlab-rake gitlab:check SANITIZE=true --trace	检查gitlab
#gitlab 默认的日志文件存放在/var/log/gitlab 目录下
gitlab-ctl tail                                #查看所有日志
#禁止 Gitlab 开机自启动
systemctl disable gitlab-runsvdir.service 
#启用 Gitlab 开机自启动
systemctl enable gitlab-runsvdir.service
```


---

参考文档
> https://blog.csdn.net/weixin_56270746/article/details/125427722
