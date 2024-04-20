---
title: "相册系统：Immich"
date: 2023-08-11

---

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/Immich-1.png)

Github: [Immich](https://github.com/immich-app/immich)

# 简介
## 特性
1. 上传和查看视频和照片
2. 打开应用程序时自动备份
3. 将照片和视频下载到本地设备
4. 多用户支持
5. 共享相册
6. 支持 RAW（HEIC、HEIF、DNG、Apple ProRaw）
7. 元数据视图（EXIF、地图）
8. 按元数据、对象和图像标签搜索
9. 管理功能（用户管理）
10. 后台备份

## 系统要求
1. 操作系统 ：首选 Ubuntu、Debian、macOS 等
2. RAM ：至少 2GB，首选 4GB
3. 核心 ：至少 2 个核心，首选 4 个核心

## 技术栈
有几个服务组成了 Immich：
1. NestJs - 应用程序的后端
2. SvelteKit - 应用程序的 Web 前端
3. PostgreSQL - 应用程序的主数据库
4. Redis - 用于在 docker 实例和后台任务消息队列之间共享 websocket 实例
5. Nginx - 负载均衡和优化的文件上传
6. TensorFlow - 对象检测 (COCO SSD) 和图像分类 (ImageNet)

# 部署
## docker部署

暂无

## docker-compose部署

```shell
# 获取 yml 文件
wget https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml

# 获取 .env 文件
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env

# 请根据官方文档修改配置文件，也可直接部署
## https://immich.app/docs/install/docker-compose
docker-compose -f docker-compose.yml up -d

# 启动成功后，访问本机的 2283 端口即可。
```


```yml
version: "3.8"

services:
  immich-server:
    container_name: immich_server
    image: altran1502/immich-server:release
    entrypoint: ["/bin/sh", "./start-server.sh"]
    volumes:
      - ${UPLOAD_LOCATION}:/usr/src/app/upload
    env_file:
      - /data/docker-data/immich/.env
    environment:
      - NODE_ENV=production
    depends_on:
      - redis
      - database
    restart: always

  immich-microservices:
    container_name: immich_microservices
    image: altran1502/immich-server:release
    entrypoint: ["/bin/sh", "./start-microservices.sh"]
    volumes:
      - ${UPLOAD_LOCATION}:/usr/src/app/upload
    env_file:
      - /data/docker-data/immich/.env
    environment:
      - NODE_ENV=production
    depends_on:
      - redis
      - database
    restart: always

  immich-machine-learning:
    container_name: immich_machine_learning
    image: altran1502/immich-machine-learning:release
    entrypoint: ["/bin/sh", "./entrypoint.sh"]
    volumes:
      - ${UPLOAD_LOCATION}:/usr/src/app/upload
    env_file:
      - /data/docker-data/immich/.env
    environment:
      - NODE_ENV=production
    depends_on:
      - database
    restart: always

  immich-web:
    container_name: immich_web
    image: altran1502/immich-web:release
    entrypoint: ["/bin/sh", "./entrypoint.sh"]
    env_file:
      - /data/docker-data/immich/.env
    restart: always

    #redis:
    #container_name: immich_redis
    #image: redis:6.2
    #restart: always

  database:
    container_name: immich_postgres
    image: postgres:14
    env_file:
      - /data/docker-data/immich/.env
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_USER: ${DB_USERNAME}
      POSTGRES_DB: ${DB_DATABASE_NAME}
      PG_DATA: /var/lib/postgresql/data
    volumes:
      - pgdata:/var/lib/postgresql/data
    restart: always

  immich-proxy:
    container_name: immich_proxy
    image: altran1502/immich-proxy:release
    environment:
      # Make sure these values get passed through from the env file
      - IMMICH_SERVER_URL
      - IMMICH_WEB_URL
    ports:
      - 62283:8080
    logging:
      driver: none
    depends_on:
      - immich-server
    restart: always

volumes:
  pgdata:
```
