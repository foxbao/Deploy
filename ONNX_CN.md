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

# 运行代码
参考https://blog.csdn.net/weixin_43603658/article/details/129113148
生成lenet.onnx
```
python LeNet.py
```



# Deploy