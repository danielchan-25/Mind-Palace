> 官网: [Gitea](https://docs.gitea.cn/)

# 部署

```yml
version: "3"

services:
  gitea:
    image: gitea/gitea
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
    network_mode: bridge
    volumes:
      - /data/docker-data/gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "222:22"
```

# CI/CD
和其他CI/CD解决方案一样，Gitea不会自己运行Job，而是将Job委托给Runner。 

Gitea Actions的Runner被称为act runner，它是一个独立的程序，也是用Go语言编写的。

> 下载地址：https://gitea.com/gitea/act_runner/releases

添加工作流：

1. 在存储库下新建 `.gitea/workflows/` 目录，然后新建工作流文件，以 `.yaml` 结尾
