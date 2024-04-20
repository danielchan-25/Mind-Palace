---
title: "Conda"

---

# 简介
试想一下，我有很多个 Python 项目都在同一台服务器下，但每个 Python 版本都不一样的，那要怎么管理呢？

`Conda` 就是为此而生。


# 安装

> 官网: [Anaconda](https://www.anaconda.com/)

> 官网: [MiniConda](https://docs.anaconda.com/free/miniconda/index.html)

其实没啥区别，只是软件的大小，我喜欢装 `MiniConda`

```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```


# 使用
安装完成后，可以使用

## 新建环境

```shell
conda create -n CONDA_TEST python==3.10
```

此时就会创建一个名称为 CONDA_TEST 的 Python3.10 环境。

## 配置文件

查看配置文件

```shell
conda config –show
```

配置文件都在用户的家目录下，文件名为：`.condarc`（隐藏文件）
- Windows路径：`C:\users\username\`
- Linux路径：`~/.condarc`

## 常用操作

- 移动虚拟环境的位置
	```shell
	# 修改配置文件
	pkgs_dirs:
	  - E:\conda_files\pkgs
	envs_dirs:
	  - E:\conda_files\envs
	```

- 删除虚拟环境
	```shell
	conda env remove --name xxx
	```
