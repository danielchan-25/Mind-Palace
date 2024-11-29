# 背景
## 为什么要部署 HTTPS
说到底，就是 HTTPS 更安全。
甚至为了安全，一个专业可靠的网站， HTTPS 是必须的。 
Firefox 和 Chrome 都计划将没有配置 SSL 加密的 HTTP 网站标记为不安全（貌似 Firefox 50 已经这么干了），目前它们也正在联合其他相关的基金会与公司推动整个互联网 HTTPS 化，现在大家访问的一些主要的网站。
如 Google 多年前就已经全部启用 HTTPS ，国内的淘宝、搜狗、知乎、百度等等也全面 HTTPS 了。
甚至 Google 的搜索结果也正在给予 HTTPS 的网站更高的排名和优先收录权。

## 怎么部署 HTTPS
你只需要有一张被信任的 CA （ Certificate Authority ）也就是证书授权中心颁发的 SSL 安全证书，并且将它部署到你的网站服务器上。
一旦部署成功后，当用户访问你的网站时，浏览器会在显示的网址前加一把小绿锁，表明这个网站是安全的，当然同时你也会看到网址前的前缀变成了 HTTPS ，不再是 HTTP 了。

## 怎么获得 SSL 安全证书
理论上，我们自己也可以签发 SSL 安全证书，但是我们自己签发的安全证书不会被主流的浏览器信任，所以我们需要被信任的证书授权中心（ CA ）签发的安全证书。
而一般的 SSL 安全证书签发服务都比较贵，比如 Godaddy 、 GlobalSign 等机构签发的证书一般都需要 20 美金一年甚至更贵。
所以我们可以使用开源项目： `acme.sh`

> https://github.com/acmesh-official/acme.sh

# 部署
按照 Wiki 中的步骤进行部署，最好使用 root 用户。

# 使用
以服务器上部署有 `Nginx` 为例：

```shell
./acme.sh --register-account -m 1@1.com  # 添加邮箱
./acme.sh --issue -d baidu.com -d www.baidu.com --webroot /usr/share/nginx/html/  # 后面是你的web项目路径
./acme.sh --set-default-ca --server letsencrypt

./acme.sh --issue -d baidu.com --nginx
./acme.sh --install-cert -d baidu.com \
--key-file /etc/nginx/cert/baidu.com.key \
--fullchain-file /etc/nginx/cert/baidu.com.pem

nginx -s reload
```
