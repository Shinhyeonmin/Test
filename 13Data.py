# -*- coding: utf-8


from torch.utils.data.dataset import Dataset
import torch
from coding import NKModel
from data import NKDataset

#Data Load
csv_path = './file/Hyeon.csv'

custom_dataset = NKDataset(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=1,
                                                shuffle=False,
                                                num_workers=1)

#Model Load
#input,hidden, output size
D_in = 30000 #(100*100*3)
H = 1000
D_out = 2

model = NKModel(D_in,H,D_out)

#CrossEntropyLoss를 사용
criterion = torch.nn.CrossEntropyLoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr = 1e-4)#1/10000

for t in range(500):

    for i,data in enumerate(my_dataset_loader,0):
        #Forward pass: Compute predicted y by passing x to the model
        #fc 구조 이기 때문에 일렬로 펴는 작업이 필요함.
        images,label = data

        print("label is ",label)
        #그냥 images를 하면 에러가 뜬다. 데이터 shape이 일치하지 않아서.
        images = images.view(1,30000)


        y_pred = model(images)

        #Compute and print loss
        loss = criterion(y_pred,label)

        print(t,loss)

        #Zero gradients, perform a backward pass, and update the weights
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
