import torch
from Deep_learning.CNN_project.Regression_model import Regression_model
from Deep_learning.CNN_project.data14 import NKDataset
from tensorboardX import SummaryWriter
import os

def save_checkpoint(state,filename='checkpoint.pth.bar'):
    torch.save(state,filename)

class AverageMeter(object):

    def __init__(self):
        self.reset()
    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0
    def update(self, val, n = 1):
        self.val = val
        self.sum += val*n
        self.count += n
        self.avg = self.sum/self.count

def train(my_dataset_loader,model,criterion,optimizer,epoch,writer):

    model.train()
    losses = AverageMeter()
    top1 = AverageMeter()

    for i, data in enumerate(my_dataset_loader,0):
        #fc 구조여서 일열로 쫙 펴야 한다.
        images, label = data
        images = torch.autograd.Variable(images)
        label = torch.autograd.Variable(label)

        #그냥 images를 하면 데이터 shape가 일정하지 않아서 에러가 난다.
        y_pred = model(images)

        label = label.float()
        #Compute and print loss
        loss = criterion(y_pred, label)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss = loss.float()
        losses.update(loss.item(),images.size(0))

    writer.add_scalar('Train/accuaracy',top1.avg,epoch)

def test(my_dataset_loader, model,criterion, epoch,test_writer):
    losses = AverageMeter()
    model.eval()

    for i, data in enumerate(my_dataset_loader,0):
        images, label = data
        y_pred = model(images)
        label = label.float()
        loss = criterion(y_pred, label)
        loss = loss.float()
        losses.update(loss.item(), images.size(0))

    print('*, epoch : {epoch:.2f} Prec@1 {losses.avg:.3f}'
          .format(epoch = epoch,losses = losses))

    test_writer.add_scalar('test/loss', losses.avg, epoch)
    return losses.avg

csv_path =  './File/study.csv'
custom_dataset = NKDataset(csv_path)
study_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=2,
                                                shuffle=True,
                                                num_workers=1)
csv_path =  './File/test.csv'

custom_dataset = NKDataset(csv_path)
test_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=2,
                                                shuffle=True,
                                                num_workers=1)


model = Regression_model()
criterion = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(),lr=1e-3)
writer = SummaryWriter('./log')
test_writer = SummaryWriter('./log/test')

lr = 1e-2
save_dir = "./save_dir"

def adjust_learing_rate(optimizer,epoch,lr):
    lr = lr*(0.1**(epoch // 10))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

def save_checkpoint(state,filename='checkoint.pth.tar'):
    torch.save(state,filename)

for epoch in range(500):

    adjust_learing_rate(optimizer, epoch,lr)
    train(study_dataset_loader,model,criterion,optimizer,epoch,writer)

    if(epoch == 0):
        prec = test(test_dataset_loader,model,criterion,epoch,test_writer)
        best_prec = prec
    else:
        prec = test(test_dataset_loader,model,criterion,epoch,test_writer)

    if(prec<best_prec):
        best_epoch = epoch
        best_prec = prec
        save_checkpoint({
            'epoch':epoch +1,
            'state_dict':model.state_dict(),
            'best_prec1':best_prec,
            'best_epch':best_epoch
        },filename=os.path.join(save_dir,'checkpoint_{}.tar'.format(epoch)))