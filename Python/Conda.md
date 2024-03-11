# Conda
```bash
conda config –show
```

## 配置文件

配置文件都在用户的家目录下，文件名为：`.condarc`（隐藏文件）
- Windows路径：`C:\users\username\`
- Linux路径：`~/.condarc`

### 虚拟环境

- 移动虚拟环境的位置
	```bash
	# 修改配置文件
	pkgs_dirs:
	  - E:\conda_files\pkgs
	envs_dirs:
	  - E:\conda_files\envs
	```

- 删除虚拟环境
	```bash
	conda env remove --name xxx
	```
