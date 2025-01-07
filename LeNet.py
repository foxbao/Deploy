import torch
from torch import nn

class LeNet(nn.Module):
	def __init__(self):
		super(LeNet, self).__init__()
		self.net = nn.Sequential(
			nn.Conv2d(1, 6, kernel_size=5),
			nn.Sigmoid(),
			nn.AvgPool2d(kernel_size=2, stride=2),
			nn.Conv2d(6, 16, kernel_size=5),
			nn.Sigmoid(),
			nn.AvgPool2d(kernel_size=2, stride=2),
			nn.Flatten(),
			nn.Linear(16*5*5, 120),
			nn.Sigmoid(),
			nn.Linear(120, 84),
			nn.Sigmoid(),
			nn.Linear(84,10))
	
	def forward(self, img):
		return self.net(img)

model = LeNet()
model.eval()
x = torch.rand(size=(1, 1, 32, 32), dtype=torch.float32)
torch.onnx.export(model, x, f='lenet.onnx', input_names=['input'],
										output_names=['output'], opset_version=11)
