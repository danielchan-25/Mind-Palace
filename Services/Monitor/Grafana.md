# Grafana
## 部署

**CentOS**

下载安装包，安装

```sh
wget https://dl.grafana.com/oss/release/grafana-5.4.3-1.x86_64.rpm
yum localinstall grafana-5.4.3-1.x86_64.rpm
systemctl enable --now grafana-server
```

```shell
# 可选
## 修改默认端口
/etc/grafana/grafana.ini
http_port = 13000

## 安装饼状图插件
grafana-cli plugins install grafana-piechart-panel

## 启动默认账号密码：admin
```
**Ubuntu**

```shell
# Ubuntu
sudo apt-get install -y adduser libfontconfig1
wget https://dl.grafana.com/enterprise/release/grafana-enterprise_9.0.7_amd64.deb
sudo dpkg -i grafana-enterprise_9.0.7_amd64.deb

# 启动
systemctl start grafana-server
```