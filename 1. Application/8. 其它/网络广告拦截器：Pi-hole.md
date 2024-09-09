## 简介
Pi-hole是一个免费的、开源的软件，旨在通过网络级别阻止广告和互联网跟踪器。它作为一个DNS服务器运行，过滤掉对已知广告服务域的请求，使得广告不会在网站和应用程序中加载。这可以提高网络性能和安全性，为用户提供更简洁的浏览体验。Pi-hole可以安装在树莓派或其他兼容的硬件上，并可以配置为阻止广泛的广告和跟踪域名。

## 部署
### docker部署

以下是使用 Docker 命令部署 Pi-hole 的步骤：

1. 在命令行中运行以下命令来拉取 Pi-hole 镜像：
```bash
docker pull pihole/pihole:latest
```

2. 创建一个名为 pihole 的容器，并将以下命令复制到命令行中：
```bash
docker run -d \
>     --name pihole \
>     --network pihole_net \
>     -e TZ="Asia/Shanghai" \
>     -e WEBPASSWORD="your_password_here" \
>     -v "$(pwd)/etc-pihole/:/etc/pihole/" \
>     -v "$(pwd)/etc-dnsmasq.d/:/etc/dnsmasq.d/" \
>     -p 53:53/tcp \
>     -p 53:53/udp \
>     -p 80:80 \
>     --restart=unless-stopped \
>     pihole/pihole:latest
其中，your_password_here 部分应替换为您想要设置的 Pi-hole 管理员密码。
```

### docker-compose部署

1. 创建一个名为 `docker-compose.yml` 的文件，并将以下内容复制到文件中：

```yml
version: "3"

services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "67:67/udp"
      - "80:80/tcp"
    environment:
      TZ: 'Asia/Shanghai'
      WEBPASSWORD: 'your_password_here'
    volumes:
      - './etc-pihole/:/etc/pihole/'
      - './etc-dnsmasq.d/:/etc/dnsmasq.d/'
    dns:
      - 127.0.0.1
      - 1.1.1.1
    cap_add:
      - NET_ADMIN
    restart: unless-stopped
```
*其中，`your_password_here` 部分应替换为您想要设置的 Pi-hole 管理员密码。*

2. 在同一目录下创建两个文件夹，分别命名为 `etc-pihole` 和 `etc-dnsmasq.d`。

3. 运行以下命令启动 Pi-hole 容器：
```bash
docker-compose up -d
```

等待 Pi-hole 启动完成，然后可以通过浏览器访问 `http://localhost/admin` 来访问 Pi-hole 的管理界面。

现在，您已经成功地使用 Docker 命令部署了 Pi-hole。

### 使用说明

实际上，Pi-hole使用的是hosts方式对广告进行过滤（类似AdAway），默认的规则对于国内环境不太友好，下面就附上适用于国内环境的一些 hosts：


- yhosts：可以说是国内比较不错的hosts，定期有更新。
- neoHosts：比较小众的hosts，看介绍貌似是不满于上面那位而弄出来的。

> https://github.com/vokins/yhosts
> https://github.com/neoFelhz/neohosts


光设置好Pi-hole是没用的，我们要过滤的是整个局域网的广告，所以要在路由器上进行配置，只需要将路由器的DNS改为我们这台服务器的IP地址即可。
