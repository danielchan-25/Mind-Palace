# NVIDIA环境

> 驱动下载地址：https://www.nvidia.cn/Download/index.aspx?lang=cn

```shell
sh ./NVIDIA-Linux-x86_64-525.116.04.run
```
注意：执行 `nvidia-smi` 命令时报错：
```shell
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
```
错误原因：是内核版本更新的问题，导致新版本内核和原来显卡驱动不匹配
解决办法：检查 `nvcc` 以及驱动
```shell
nvcc -V

ls /usr/src | grep nvidia
nvidia-450.57

apt install dkms
dkms install -m nvidia -v 450.57

nvidia-smi
```

## Cuda
> 下载地址：
> https://developer.nvidia.com/cuda-downloads
> https://developer.nvidia.com/cuda-11-8-0-download-archive

源码安装
```shell
chmod +x cuda_12.0.0_525.60.13_linux.run
sh ./cuda_12.0.0_525.60.13_linux.run
################################################
Do you accept the above EULA? (accept/decline/quit):
accept
################################################
 CUDA Installer                                                               x
x - [ ] Driver                                                                 x
x      [ ] 525.60.13                                                           x
x + [X] CUDA Toolkit 12.0                                                      x
x   [X] CUDA Demo Suite 12.0                                                   x
x   [X] CUDA Documentation 12.0                                                x
x - [ ] Kernel Objects                                                         x
x      [ ] nvidia-fs                                                           x
x   Options                                                                    x
x   Install
################################################
```

## cuDNN
> 下载地址：https://developer.nvidia.com/rdp/cudnn-archive

>安装说明：https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#prerequisites

建议使用 `TAR` 的方式安装，只需将 `include` `lib` 里的东西拷贝进 `cuda` 对应的目录，然后写入环境变量即可，如：
```shell
cd cudnn-linux-x86_64-8.6.0.163_cuda11-archive/

cp cudnn*.h /usr/local/cuda/include
cp -P libcudnn* /usr/local/cuda/lib64/
chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.8/lib64:/usr/local/cuda/extras/CUPTI/lib64
```

## tensorflow

> 兼容性：https://tensorflow.google.cn/install/source?hl=en


在使用 `tensorflow` 调用 GPU 时，注意 `CUDA` `cuDNN` 的版本兼容性。

![](/media/202306/2023-06-02_140817_2992010.4506267745364454.png)

测试是否支持 GPU
```shell
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```


> https://blog.csdn.net/wjinjie/article/details/108997692

> https://blog.csdn.net/xiaojinger_123/article/details/121161446