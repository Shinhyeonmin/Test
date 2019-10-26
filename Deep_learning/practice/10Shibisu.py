# -*- coding: utf-8

from torch.utils.data.dataset import Dataset
from torchvision import transforms
import pandas as pd
import cv2
import numpy as np
import torch

class NKDataset(Dataset):

    #초기화 시켜줌
    def __init__(self,csv_path):
        self.to_tensor = transforms.ToTensor()
        self.data_info = pd.read_csv(csv_path,header=None)
        self.image_arr = np.asarray(self.data_info.iloc[:,0])
        self.label_arr = np.asarray(self.data_info.iloc[:,0])
        self.data_len = len(self.data_info.index)

    #경로를 통해 실제 데이터에 접근 해 데이터를 돌려 줌
    #__getitem__
    def __getitem__(self, index):


        single_image_name = self.image_arr[index]

        print(single_image_name)
        img_as_img = cv2.imread(single_image_name)

        img_as_tensor = self.to_tensor(img_as_img)

        single_image_label = self.label_arr[index]

        return(img_as_tensor,single_image_label)

    #데이터의 전체 길이를 구함
    def __len__(self):

        return self.data_len

#cav 의 경로 설정해 줘야 함.
csv_path = './file/Hyeon.csv'

custom_dataset = NKDataset(csv_path)

#batch size를 2로 하면 에러가 생김. 이유:enumerate는 하나씩 출력 함
my_dataset_loader = torch.utils.data.DataLoader(dataset=custom_dataset,
                                                batch_size=1,
                                                shuffle=False)

#enumerate 는 list 의 있는 내용을 순서를 매기면서 프린트를 한다
for (images,labels) in enumerate(my_dataset_loader):
    print(images,labels)