# V2Ray

> 下载地址：https://github.com/v2ray/dist

## 部署
以 `Ubuntu20.04-server` 版本为例。
```sh
# 目录结构
/data/v2ray/
├── config.json
├── config.json.bak
├── geoip.dat
├── geoip-only-cn-private.dat
├── geosite.dat
├── systemd
│   └── system
│       ├── v2ray.service
│       └── v2ray@.service
├── v2ray
├── v2ray-linux-64.zip
├── Vaccess.log
├── Verror.log
├── vpoint_socks_vmess.json
└── vpoint_vmess_freedom.json
```
可以从 Windows 客户端中，导出已有的配置文件，然后导入

![](/media/202305/2023-05-24_175339_1961160.46400390987039086.png)

```sh
# 启动，可以通过 -c 指定配置文件
./v2ray run -c config.json