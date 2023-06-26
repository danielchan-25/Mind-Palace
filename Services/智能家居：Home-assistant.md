# 智能家居：Home-assistant
![](/media/202303/2023-03-10_145026_8940670.3460440800485811.png)
# 介绍
HomeAssistant，简称 HA，是一款基于 Python 的智能家居开源系统，支持众多品牌的智能家居设备，可以轻松实现设备的语音控制、自动化等。
相比起Homekit、米家、Aqara等，最大的优点是：一统江湖，能集中管理各个品牌的智能家居，你也不想在各种APP中跳转才能使用吧，这样太不智能了。

# 部署
## docker部署
```shell
docker pull homeassistant/home-assista
```
```bash
docker run -d \
  --name homeassistant \
  --privileged \
  --restart=unless-stopped \
  -e TZ="Asia/Shanghai" \
  -v /data/docker-data/home-assistant/config:/config \
  --network=host \
  ghcr.io/home-assistant/home-assistant:stable
```
## docker-compose部署
```yml
version: "3"
services:
  home-assistant:
    image: homeassistant/home-assistant
    restart: unless-stopped
    container_name: home-assistant
    network_mode: bridge
    environment:
      - TZ:Asia/Shanghai
    volumes:
      - "/data/docker-data/home-assistant/config:/config"
    ports:
      - "61238:8123"
```

网页访问 IP:8123 进入后台，根据实际情况填入信息即可。

![](/media/202303/2023-03-10_145105_3828890.19353547074826638.png)

# HACS
## 简介
HACS（Home Assistant Community Store）是HA的第三方应用商店，有很多大佬们写的各种插件，可以连接各大物联网平台的设备，是一个必装的集成。
> 下载地址：https://github.com/hacs/integration/releases/

## 安装说明
我们先下载安装包：**hacs.zip**，并在服务器 Home-asstant 上创建三个目录：

```bash
./config/custom_components
./config/custom_components/hacs
./config/www

# custom_components：存放其它插件的离线安装包
# custom_components/hacs：是存放等会要安装的HACS文件
# www：存放未来HACS安装的各种首页磁贴
```

将安装包放在`./config/custom_components/hacs` 下并解压，得到的内容应该是：

```bash
ls /config/custom_components/hacs
>>>
__init__.py                 const.py                    enums.py                    hacs_frontend_experimental  repositories                update.py
__pycache__                 data_client.py              exceptions.py               iconset.js                  sensor.py                   utils
base.py                     diagnostics.py              frontend.py                 manifest.json               system_health.py            validate
config_flow.py              entity.py                   hacs_frontend               repairs.py                  translations                websocket
```

此时回到网页后台，重启 Home-assistant：『开发者工具』->『重新启动』

重启后：『配置』->『设备与服务』->右下角『添加集成』->搜索 “HACS”

需要绑定 GitHub 账号，相信大家都有就不过多描述了，绑定完成后再次重启，在菜单栏即可找到 HACS，至此安装成功。

## 添加插件

安装成功后，我们就可以安装任意 HACS 插件了，由于网络因素，在线安装经常卡住，这里展示在线安装和离线安装。

### 在线安装

举例：我要添加 小米智能家居

『HACS』->『集成』->右下角『浏览并下载存储库』-> 搜索『Xiaomi』->『Xiaomi Miot Auto』，右下角下载插件。

添加成功后输入小米的账号密码，即可添加你账号下的小米设备，这里就不过多赘述了。

### 离线安装

举例：我要添加 Uptime_Kuma

1. 『HACS』->『集成』->右下角『浏览并下载存储库』-> 搜索『Uptime』
![](/media/202303/2023-03-10_145453_6080640.2848525808359921.png)

2. 点击进入，再点击右上角的 ... 选择存储库（GitHub）

3. 找到 release 下的安装包

4. 上传到服务器/config/custom_components 目录解压

5. 重启服务端

6. 『配置』->『设备与服务』->『添加集成』->『搜索 UptimeKuma』，填入UptimeKuma服务端信息即可。

## 手动添加主题 UI

### 创建 themes 目录

服务器上创建 `themes` 目录，与 `custom_components` `www` 同级

目录结构：
```bash
config
├── configuration.yaml
├── custom_components
├── themes
└── www
```

### 下载插件安装包

『HACS』->『前端』->『浏览添加存储库』，找到喜欢的存储库后，右上角进入 GitHub 地址。

将项目下的 `themes/` `ios-themes.yml` 下载，上传至服务器的 `config/themes/` 目录

> 也可能不叫 `ios-themes.yml`，是 `yml` 结尾的文件

目录结构：
```bash
├── themes
│   └── ios-themes
│       ├── homekit-bg-blue-red.jpg
│       ├── homekit-bg-dark-blue.jpg
│       ├── homekit-bg-dark-green.jpg
│       ├── homekit-bg-light-blue.jpg
│       ├── homekit-bg-light-green.jpg
│       ├── homekit-bg-orange.jpg
│       ├── homekit-bg-red.jpg
│       └── ios-themes.yaml
│   └── ios-themes2
│       ├── homekit-bg-blue-red.jpg
│       └── ios-themes2.yaml
```