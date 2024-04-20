---
title: "V2Ray"
date: 2024-04-20

---

> Github: [V2ray](https://github.com/v2ray/dist)

# 客户端

以 `Ubuntu20.04-server` 版本为例。

```shell
# 目录结构
./v2ray/
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

![](https://github.com/danielchan-25/Mind-Palace/blob/main/1.%20Application/99.%20img/V2Ray-1.png)

```shell
# 启动，可以通过 -c 指定配置文件
./v2ray run -c config.json
```