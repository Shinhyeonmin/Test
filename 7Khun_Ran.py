#Edin... 소속
import torch

class TwoLayerNet(torch.nn.Module):

    def __init__(self,D_in,H,D_out):

        super(TwoLayerNet,self).__init__()
        self.linear1 = torch.nn.Linear(D_in,H)
        self.linear2 = torch.nn.Linear(H,D_out)

    def forward(self,x):

        h_relu = self.linear1(x).clamp(min=0)
        h_pred = self.linear2(h_relu)

        return h_pred