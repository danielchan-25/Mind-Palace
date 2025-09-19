# WindowsTerminal

主要是修改："profiles":"list" 下的配置

示例：
```json
{
    "profiles": 
    {
        "defaults": 
        {
            "colorScheme": "One Half Dark"
        },
        "list": 
        [
            {
                "commandline": "%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                "hidden": false,
                "name": "Windows PowerShell"
            },
            {
                "commandline": "%SystemRoot%\\System32\\cmd.exe",
                "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
                "hidden": false,
                "name": "\u547d\u4ee4\u63d0\u793a\u7b26"
            },
            {
                # 功能：进入 D:\\frpc 目录，执行 D:\\frpc\\frpc.exe -c D:\\frpc\\frpc.ini
                "colorScheme": "Campbell Powershell",
                "commandline": "D:\\frpc\\frpc.exe -c D:\\frpc\\frpc.ini",
                "guid": "{6e0f135d-8309-458a-9d59-2dcd59764215}",
                "hidden": false,
                "name": "Frpc",
                "startingDirectory": "D:\\frpc"
            },
            {
                "commandline": "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python310\\python.exe get_account_details.py",
                "guid": "{daaccf8f-733c-4d12-9ee5-d6d4f14d14ed}",
                "hidden": false,
                "name": "TB_Logger",
                "startingDirectory": "C:\\Users\\admin\\Desktop\\tb"
            },
            {
                "commandline": "C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python310\\python.exe D:\\NXLData.py",
                "guid": "{71343f94-8184-444a-8788-0e0b70ed7166}",
                "hidden": false,
                "name": "TX_NXLData"
            },
            {
                "colorScheme": "Vintage",
                "commandline": "D:\\ib\\.venv\\Scripts\\python.exe D:\\ib\\spider_data.py",
                "guid": "{5f727adb-31e7-4d8c-9b53-d6d16317a4ce}",
                "hidden": false,
                "name": "IB_SpiderDATA",
                "startingDirectory": "D:\\ib"
            }
        ]
    },
}
```
