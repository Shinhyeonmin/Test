import torch
from Deep_learning.CNN_project.cnn_model import Cnn_Model
from Deep_learning.CNN_project.data14 import NKDataset

def train(my_dataset_loader,model,criterion,optimizer,epoch):
    model.train()# -*- coding: utf-8

    for i, data in enumerate(my_dataset_loader,0):
        images, label = data


        #그냥 images를 하면 에러가 뜬다. 데이터 shape이 일치하지 않아서.
        y_pred = model(images)
        loss = criterion(y_pred,label)

        print(epoch,loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def test(my_dataset_loader, model, criterion, epoch):

    model.eval()

    for i, data in enumerate(my_dataset_loader, 0):
        images, label=data
        y_pred=model(images)
        loss = criterion(y_pred, label)

        print(epoch, loss.item())

csv_path = './hand_img/Hyeon.csv'

custom_dataset = NKDataset(csv_path)

my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=2,
                                                shuffle=False,
                                                num_workers=1)

D_in = 30000
H = 100
D_out=5

model = Cnn_Model()

criterion = torch.nn.CrossEntropyLoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(),lr=1e-4)

for epoch in range(500):
    print('epoch',epoch)
    train(my_dataset_loader,model,criterion,optimizer,epoch)
    test(my_dataset_loader,model,criterion,epoch)