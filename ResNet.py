from mmcls.apis import init_model
import torch

resnet18 = init_model('configs/resnet/resnet18_8xb32_in1k.py',
											   checkpoint='resnet18_8xb32_in1k_20210831-fbbb1da6.pth',
											   device='cuda:0')
# 由于模型在训练过程中有drop_out，而且模型中BN层的参数会随着输入的变化而变化，推理的时候要消除这些影响，因此需要打开evaluation模式，起到使参数固定的作用
resnet18.eval()
x = torch.rand((1,3,224,224),device='cuda:0')
# 单张输入
torch.onnx.export(resnet18, 
									  (x,False), 
									  'resnet18.onnx', 
									  input_names=['input'], 
									  output_names=['output'], 
									  opset_version=11)