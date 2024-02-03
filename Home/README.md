# Home

## 服务器

| 名称       | 系统             | 配置                                                         | 说明         |
| ---------- | ---------------- | ------------------------------------------------------------ | ------------ |
| cc-Windows | Windos 11        | Intel(R) Core(TM) i5-8500 CPU @ 3.00GHz/GTX 1060 6G<br />32Gb<br />256G SSD + 500G HDD  + 2Tb SSD | 主力电脑     |
| cc-J1900   | Ubuntu 20.04 LTS | Intel(R) Celeron(R) CPU  J1900  @ 1.99GHz<br />DDR3 4GB 1666MHz<br />64G HDD | 低功耗小主机 |
| cc-NAS     | QNAP             | 512Mb<br />1Tb HDD *2（RAID 1）                              | 存储服务器   |

## 软件架构

- cc-Windows
  - 模型
    - Stable Diffusions WebUI
    - ChatGLM2-6B

- cc-J1900
  - docker
    - UptimeKuma：监控
    - Bitwarden：密码托管
    - Memos：树洞
    - Gitea：代码托管
    - MrDoc：文档服务
  - MySQL：数据库
  - Nginx：HTTP 服务
  - OpenVPN

- cc-NAS

  - NFS&SMB&FTP：文件共享服务

  - 相册、视频、音乐服务
