#터미널에 python Edin_Dan.py 치기
import torch
from TwoLayerNet import TwoLayerNet

N,D_in,H, D_out = 64,1000,100,10

x = torch.randn(N,D_in)
y = torch.randn(N,D_out)

model = TwoLayerNet(D_in,H,D_out)

criterion = torch.nn.MSELoss(reduction = "sum")

learning_rate = 1e-4

optimizer = torch.optim.Adam(model.parameters(),lr = learning_rate)

for t in range(500):
    y_pred = model(x)

    loss = criterion(y_pred,y)

    print(t,loss.item())

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()
