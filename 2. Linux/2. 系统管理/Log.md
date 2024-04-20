---
title: "Log"

date: 2024-04-20

---

# journal

要清理 `systemd journal` 日志文件，您可以使用 `journalctl` 工具来执行此操作。您可以选择删除旧的日志文件或限制存储空间的大小以确保日志文件不会无限增长。

下面是一些常见的操作：

1. **删除旧的日志文件：**

   删除旧的日志文件可以帮助释放磁盘空间。您可以使用以下命令来删除某个日期之前的日志文件（例如，删除 30 天前的日志）：

   ```shell
   sudo journalctl --vacuum-time=30d
   ```

   这将删除 30 天前的日志文件。

2. **限制日志文件的大小：**

   您可以配置 systemd journal 以限制单个日志文件的大小和总体磁盘空间的使用。编辑 `/etc/systemd/journald.conf` 配置文件（需要管理员权限）：

   ```shell
   sudo nano /etc/systemd/journald.conf
   ```

   找到以下行，根据需要进行配置（示例值）：

   ```shell
   SystemMaxUse=100M   # 总体磁盘空间使用不超过 100MB
   SystemKeepFree=50M  # 留下至少 50MB 的磁盘空间
   SystemMaxFileSize=10M  # 单个日志文件最大为 10MB
   ```

   保存文件并退出编辑器。然后重新启动 journal 服务以应用更改：

   ```shell
   sudo systemctl restart systemd-journald
   ```

   这将限制 journal 日志文件的大小和总体磁盘空间的使用。

3. **清除所有日志：**

   如果您希望完全清除所有 journal 日志，可以运行以下命令：

   ```shell
   sudo journalctl --rotate        # 旋转并归档日志
   sudo journalctl --vacuum-time=0 # 删除所有旧日志
   ```

   这将清除所有 journal 日志。

请注意，在进行 journal 日志清理或配置更改时，请确保不会影响您的系统监控、故障排除或审计需求。 journal 日志对于系统管理和故障排除非常重要，因此在清理时要谨慎处理。