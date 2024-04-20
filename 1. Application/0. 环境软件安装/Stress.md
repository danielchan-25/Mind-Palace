---
title: "Stress"
date: 2024-04-20

---

`stress` 是 `Linux` 的一个压力测试工具，可以对 CPU、Memory、IO、磁盘进行压力测试。

# 安装

```shell
yum install stress
```

# 使用

```shell
stress [OPTION [ARG]]
```
- `-c，--cpu N`：产生N个进程，每个进程都循环调用sqrt函数产生CPU压力。

- `-i, --io N`：产生N个进程，每个进程循环调用sync将内存缓冲区内容写到磁盘上，产生IO压力。

- `-m, --vm N`：产生N个进程，每个进程循环调用malloc/free函数分配和释放内存。

- `-d, --hdd N`：产生N个不断执行write和unlink函数的进程(创建文件，写入内容，删除文件)

- `-t, --timeout N`：在N秒后结束程序

- `--backoff N`：等待N微秒后开始运行

- `-q, --quiet`：程序在运行的过程中不输出信息

```shell
# 开启 2 个cpu进行压力测试，持续 60 秒
stress --cpu 2 --timeout 60s

# 开启 2 个IO进程，持续 60 秒
stress --io 2 --timeout 60s

# 开启 2 个进程分配内存，每次分配 1GB，保持 100 秒，然后 120 秒后停止
## --vm-hang N：指示每个消耗内存的进程在分配到内存后转入睡眠状态N秒，然后释放内存，一直重复执行这个过程
stress --vm 2 --vm-bytes 1G --vm-hang 100 --timeout 120s
```