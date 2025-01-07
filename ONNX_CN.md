[TOC] 
# 创建conda环境
```
conda create -n Deploy python=3.8 -y
conda activate Deploy
```

# 安装 Pytroch 1.10.0
切记，这里面的cudatoolkit=11.3，一定要和上面安装的CUDA版本一致
```
pip install torch==1.10.0+cu113 torchvision==0.11.0+cu113 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

```

# 部署LeNet，Pytorch模型转ONNX模型
参考https://blog.csdn.net/weixin_43603658/article/details/129113148
生成lenet.onnx
```
python LeNet.py
```
# onnx可视化
安装netron
```
pip install netron
netron lenet.onnx
```

# 部署ResNet
参考https://blog.csdn.net/weixin_43603658/article/details/129113148


# 安装 mmcv v2.0.0

```
pip install mmcv-full==1.4.2 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.10.0/index.html
```

# 安装mmcls
```
pip install mmcls
```

# 下载mmpretrain源码
```
git clone https://github.com/open-mmlab/mmpretrain.git
cd mmpretrain
pip install -v e .
```
# 下载模型与权重
从以下网页
https://github.com/open-mmlab/mmpretrain/tree/master/configs/resnet
下载相应的权重文件
resnet18_8xb32_in1k_20210831-fbbb1da6.pth

# 运行代码
将ResNet.py代码放入mmpretrain文件夹下，并运行

