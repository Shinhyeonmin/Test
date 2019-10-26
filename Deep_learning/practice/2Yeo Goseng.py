
'''
import numpy as np

N,D_in,H,D_out = 5,10,10,10

x = np.random.randn(N,D_in)
y = np.random.randn(N,D_out)


w1 = np.random.randn(D_in,H)
w2 = np.random.randn(H,D_out)

learning_rate = 1e-6 #10^-6

for t in range(500):

    h = x.dot(w1)

    h_relu = np.maximum(h,0)

    y_pred = h_relu.dot(w2)

    loss = np.square(y_pred - y).sum()

    print(t, loss)

    grad_y_pred = 2.0 *(y_pred-y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)

    grad_h = grad_h_relu.copy()
    grad_h[h<0]=0

    grad_w1 = x.T.dot(grad_h)

    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
'''
# torch 실행이 안되어서 test.py에 넣어놈. 터미널에 python test.py 치기
import torch
dtype = torch.float

device = torch.device("cpu")

N,D_in,H,D_out = 64,1000,100,10

x = torch.randn(N,D_in,device = device,dtype=dtype)
y = torch.randn(N,D_out,device = device,dtype=dtype)

#weight
w1 = torch.randu(D_in,H,device=device,dtype=dtype)
w2 = torch.randu(H,D_out,device=device,dtype=dtype)

learning_rate = 1e-6

for t in range(500):

    h =x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)

    loss = (y_pred - y).pow(2).sum().item()
    print(t, loss)


    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)

    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()

    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2