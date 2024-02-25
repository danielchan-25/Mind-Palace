# Apache

## 查看正在使用的配置文件
```bash
apache2ctl -t -D DUMP_INCLUDES
```

这个命令将显示 Apache2 配置中所有被包含的文件，包括正在使用的文件。在输出中，你可以看到哪些配置文件当前正在被 Apache2 服务器加载和使用。