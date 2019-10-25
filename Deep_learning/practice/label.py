import os,os.path
from model import TwoLayerNet
import numpy as np
import cv2
import torch
from torchvision import transforms

img_list = []
e = ['.png','.jpg','.jpeg']

path = '.'

for filename in os.listdir(path):
    for i in range(len(e)):
        if(filename.lower().endswith(e[i])):
            file = cv2.imread(filename)
            re_image = cv2.resize(file,(100,100))
            img_list.append(re_image)

image_arr = np.asarray(img_list)

img_as_tenosr = []

for i in range(len(image_arr)):
    img = transforms.ToTensor()(image_arr[i])
    img = img.view(-1)
    img_as_tenosr.append(img)

num_image = 5
num_class = 5

label = torch.empty(num_image, dtype = torch.long)

#0 is cat,1 is dog
label[0] = 0
label[1] = 1
label[2] = 2
label[3] = 3
label[4] = 4

model = TwoLayerNet(30000,100,5)

criterion = torch.nn.CrossEntropyLoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(),lr =1e-4)

img_as_tenosr = torch.stack(img_as_tenosr)

for t in range(500):
    y_pred = model(img_as_tenosr)
    loss = criterion(y_pred,label)
    print(t,loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()