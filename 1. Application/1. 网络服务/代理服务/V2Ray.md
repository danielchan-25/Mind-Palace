---
title: "V2Ray"

---

> [Github](https://github.com/v2ray/dist)

# 部署
以 `Ubuntu20.04-server` 版本为例。

```shell
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

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Services/Network/img/V2Ray-1.png)

```shell
# 启动，可以通过 -c 指定配置文件
./v2ray run -c config.json
```