Librespeed 是一个开源的网速测试工具，类似于Speedtest.net。

它可以在Web浏览器上运行并提供有关网络速度和延迟的信息。

## 部署
首先，使用如下的 Docker 命令拉取 Librespeed 的 Docker 镜像：
```shell
docker pull linuxserver/librespeed
```
启动容器
```shell
docker run -d \
-p 80:80 \
--name=librespeed \
linuxserver/librespeed
```


同样也可以使用 docker-compose 脚本部署
```yml
version: "3"
services:
  librespeed:
    image: linuxserver/librespeed
    container_name: librespeed
    ports:
      - 80:80
```
使用以下命令启动容器：
```shell
docker-compose up -d
```
接下来，在您的浏览器中访问服务器的IP地址或域名，即可进入 Librespeed 的主页，进行网速测试。
