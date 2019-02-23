import torch

batch_size = 2
class Cnn_Model(torch.nn.Module):

    def __init__(self):
        super(Cnn_Model,self).__init__()
        self.conv1 = torch.nn.Conv2d(3,20,kernel_size=3)
        self.relu = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(20,3,kernel_size=3)
        self.conv3 = torch.nn.Linear(27648,5)

    def forward(self,x):

        x =self.conv1(x)

        print("conv1",x.size())
        x = self.relu(x)
        y = self.conv2(x)

        print("conv2",y.size())
        x = self.relu(y)
        x = x.view(batch_size,-1)

        print('linear', x.size())
        x = self.conv3(x)

        print("conv3",x)

        print("last x size",x.size())

        x = x.view(batch_size,5)

        return x