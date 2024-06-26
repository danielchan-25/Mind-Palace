---

title: "密码管理器：Bitwarden"

date: 2024-04-17

---

# 服务端部署

## Docker 部署

```shell
docker run -d --name bitwarden \
-v ~/bitwarden/:/data/ \
-p 8080:80 bitwardenrs/server
```

## Docker-Compose 部署

```yml
version: '3.0'
services:
  bitwardens:
    image: bitwardenrs/server
    container_name: bitwarden
    network_mode: bridge
    restart: always
    environment:
      - ADMIN_TOKEN=XXXXXXXXX
    volumes:
      - "~/bitwarden/:/data/"
    ports:
      - "8080:80"
```

```yml
version: '3.0'
services:
  bitwardens:
    image: docker.io/vaultwarden/server:latest
    container_name: vaultwarden
    network_mode: bridge
    restart: always
    environment:
      - ADMIN_TOKEN=XXXXXXXXX
    volumes:
      - "~/valutwarden/:/data/"
    ports:
      - "8080:80"
```


启动容器

```shell
docker-compose -f bitwarden.yml up -d
```

访问：`http://localhost:8080` 

后台管理页面：`http://localhost:8080/admin`

# 配置

进入后台管理页面后，可参考以下网页进行配置：

[Vaultwarden Wiki 中文版](https://rs.ppgg.in)

[Bitwarden 部署和使用](https://host.ppgg.in)

# 反向代理

因 `Bitwarden` 安全需要，必须使用SSL方式访问。

以下是 `Nginx` 的配置文件：

```nginx
http {
        ssl_certificate cert/domain.com.pem;  # 证书文件
        ssl_certificate_key cert/domain.com.key;  # 证书文件
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout 5m;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
        ssl_protocols TLSv1.1 TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;

        server {
                listen 443 ssl;
                listen [::]:443 ssl;

                server_name domain.com;

                location / {
                        proxy_pass      http://127.0.0.1:8080;
                        proxy_http_version 1.1;
                        proxy_set_header Upgrade $http_upgrade;
                        proxy_set_header Connection "upgrade";
                        proxy_set_header Host $host;
                        proxy_set_header X-Real-IP $remote_addr;
                        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                        proxy_set_header X-Forwarded-Proto $scheme;
                }
        }
}
```


# 生成受信任的SSL证书

先简单说下我的情况：

- 自建 `Bitwarden` 服务器，且不是云服务器，服务器在家里。

- 有公网 IP，用上了 DDNS，但没有 80,443 端口权限。

- 没有免费的 SSL 证书。

如果您也是以上的情况，可以使用 `mkcert` 生成受信任的本地SSL证书。

> Github: [mkcert](https://github.com/FiloSottile/mkcert)

## 服务端安装

在服务端执行以下操作：

```shell
wget https://github.com/FiloSottile/mkcert/releases/download/v1.4.4/mkcert-v1.4.4-linux-amd64
chmod +x mkcert-v1.4.4-linux-amd64
./mkcert-v1.4.4-linux-amd64 --cert-file bitwarden.pem --key-file bitwardenkey.pem 192.168.2.11
./mkcert-v1.4.4-linux-amd64 -install
```

执行完毕后，在当前目录可以看到有两个文件（服务端使用）：

- bitwarden.pem
- bitwardenkey.pem

在 `/root/.local/share/mkcert/` 下也有两个文件（客户端使用）：

- rootCA.pem
- rootCA-key.pem

至此服务端已完成操作，接下来便是客户端的操作。

## 客户端安装

### iPhone

1. 安装证书
   1. 在 Files 中打开 rootCA.pem 文件，显示什么不用管，直接下一步。
   2. 打开 Settings，有个提醒：Profile Downloaded，点击。
   3. 此时会显示你的证书，点击右上角的 Install，并输入锁屏密钥，再次 Install，然后 Done。
   4. 这是已经跳转到 VPN & Device Management 界面，表示已经安装成功，点击证书即可看到证书的详细细节。
   5. 来到 General -> About -> Certificate Trust Settings
   6. 查看你的证书，点击右方的按钮启用，Continue，完成。
2. 登录
   1. 打开 `Bitwarden` 软件
   2. 由于是自建服务器，所以需要在 Logging in on 中选择：Self-hosted
      1. Server URL 填写服务端的信息，如：`https://localhost:8443`，点击 Save 保存。
      2. 输入 Email address，点击 Continue，输入密码，点击 Log in
      3. 成功。

### MacOS

1. 安装证书
   1. 打开：`keychain Access.app` 
   2. 选择 `login` ，将证书添加至 `Certificates` 
   3. 点击证书，选择 `Get Info` 
   4. 将 `Trust` 中的所有选项调整为：`Always Trust`
   5. 保存退出。
2. 登录
   1. 与 `iPhone` 的登录步骤一致。
