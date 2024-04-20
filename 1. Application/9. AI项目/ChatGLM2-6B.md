---
title: "ChatGLM2-6B"

---

> [Github](https://github.com/THUDM/ChatGLM2-6B)

只需 6B 显存，即可运行。

# 部署

```shell
# 推荐 Python 版本：3.9.6
conda create -n ChatGLM2-6B python==3.9.6

git clone https://github.com/THUDM/ChatGLM2-6B
cd ChatGLM2-6B
```

> 启动 web_demo.py 时可能会报错，要使用 gradio==3.39.0



# API 使用

```shell
python openai_api.py
```

> https://github.com/THUDM/ChatGLM2-6B/issues/483
>
> 如果报错：`TypeError: dumps_kwargs keyword arguments are no longer supported.`
>
> ```shell
> # 检查 `openai_api.py` 文件，修改以下内容：
> 
> chunk.json(exclude_unset=True, ensure_ascii=False)
> # 替换为
> chunk.model_dump_json(exclude_unset=True,exclude_none=True)
> ```

