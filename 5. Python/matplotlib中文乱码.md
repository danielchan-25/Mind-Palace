服务器环境：Ubuntu 20.04.5 LTS

当运行以下代码时：
```python
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
mpl.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

x = np.random.randint(0, 100, 100)
y = np.random.randint(0, 100, 100)
plt.figure()
plt.title('示例')
plt.scatter(x, y)
plt.savefig('/root/AutoGPT/coding/scatter2.png')
print('Scatter plot saved to scatter.png')
```
出现报错：

```
findfont: Generic family 'sans-serif' not found because none of the following families were found: SimHei
```

解决办法：

1. 安装中文环境：

   ```shell
   apt update -y
   apt install -y language-pack-zh-hans language-pack-gnome-zh-hans fontconfig ttf-mscorefonts-installer
   
   update-locale LANG=zh_CN.UTF-8
   locale-gen zh_CN.UTF-8
   ```
2. 下载 `SimHei.ttf` 文件
3. 运行以下代码，查看matplotlib库的配置文件所在位置：

   ```python
   import matplotlib
   print(matplotlib.matplotlib_fname())
   
   >>> anaconda3/envs/pytorch2/lib/python3.10/site-packages/matplotlib/mpl-data
   ```

4. 将字体文件放进以上路径的 `fonts`目录里。

5. 修改配置文件：`anaconda3/envs/pytorch2/lib/python3.10/site-packages/matplotlib/mpl-data/matplotlibrc`

   ```ini
   # 取消以下注释
   font.family : sans-serif
   font.sans-serif : SimHei
   axes.unicode_minus : False
   ```

6. 清理 `matplotlib` 缓存：

   ```shell
   rm -f ~/.cache/matplotlib/*
   ```

7. 测试
