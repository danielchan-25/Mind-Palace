---
title: "ClashForWindows使用技巧"
date: 2024-04-19
---

如何防止更新订阅后，覆盖自定义规则？

> 参考文档：
>
> [Clash添加自定义规则并防止更新覆盖](https://yang-zi.com/ctjzdygzbfzgxfg/)
>
> [Clash 教程](https://www.codein.icu/clashtutorial/)
>
> [Clash 如何防止更新订阅后覆盖自定义规则？以及注意事项](https://blog.fengsweb.top/archives/clash22)
>
> [利用Clash for Windows Parsers配置文件预处理防止更新订阅覆盖自定义规则Rules](https://xin.im/2022.html)

1. 进入：Settings -> Profiles -> Parsers，编辑

2. 配置文件如下：

   ```yml
   parsers: # array
    - url: # 订阅地址
      yaml:
        prepend-rules:
          - DOMAIN-SUFFIX,icanhazip.com,DIRECT
          - DOMAIN-SUFFIX,chat.openai.com,美國费利蒙
          - DOMAIN-SUFFIX,cdn.oaistatic.com,美國费利蒙
          - DOMAIN-SUFFIX,gravatar.com,美國费利蒙
          - DOMAIN-SUFFIX,anthropic.com,美國费利蒙
          - DOMAIN-SUFFIX,reddit.com,美國费利蒙
   ```

3. 编辑完成后，进入 `Profiles` 更新订阅，然后在订阅中的 `Rules` 即可看到刚刚写入的规则了。



