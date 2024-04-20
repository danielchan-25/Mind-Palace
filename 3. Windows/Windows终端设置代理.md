# Windows终端设置代理

用 `ShadowSocksR` 为例

先确保 **允许来自局域网的连接** 开启

![](https://github.com/danielchan-25/Mind-Palace/blob/main/Windows/img/windows_proxy.png)

系统代理模式为：**PAC**

## CMD

1. 打开 CMD，查看当前的IP地址
```cmd
C:\Users\admin>curl cip.cc
IP      : xxx.xxx.xxx
地址    : 中国  广东  广州
运营商  : 电信
数据二  : 广东省揭阳市 | 电信
数据三  : 中国广东省揭阳市 | 电信
URL     : http://www.cip.cc/xxx.xxx.xxx
```

2. 输入：
```cmd
set http_proxy=http://127.0.0.1:1080
set https_proxy=http://127.0.0.1:1080
```

3. 测试
```cmd
C:\Users\admin>curl cip.cc
IP      : xxx.xxx.xxx
地址    : 中国  中国
数据二  : 中国 | 阿里云
数据三  : 日本东京都东京 | 阿里云
URL     : http://www.cip.cc/xxx.xxx.xxx
```

## Powershell
```powershell
$env:http_proxy="http://127.0.0.1:1080"
$env:https_proxy="http://127.0.0.1:1080"
```

如果在测试的期间出现以下报错，请检查本机的IE浏览器设置，一般是没使用过 Edge，开启正常流程后即可。

```powershell
curl : 无法分析响应内容，因为 Internet Explorer 引擎不可用，或者 Internet Explorer 的首次启动配置不完整。请指定 UseBasi
cParsing 参数，然后再试一次。
所在位置 行:1 字符: 1
+ curl cip.cc
+ ~~~~~~~~~~~
    + CategoryInfo          : NotImplemented: (:) [Invoke-WebRequest], NotSupportedException
    + FullyQualifiedErrorId : WebCmdletIEDomNotSupportedException,Microsoft.PowerShell.Commands.InvokeWebRequestComman
   d
```


---

参考文档：
> https://github.com/shadowsocks/shadowsocks-windows/issues/1489
> https://gist.github.com/dreamlu/cf7cbc0b8329ac145fa44342d6a1c01d