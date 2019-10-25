import cv2
import os, os.path
import torch
import numpy as np
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

print(img_list)

img_arr = np.asarray(img_list)

img_as_tenosr = []

for i in range(len(img_arr)):
    img_as_tenosr.append(transforms.ToTensor()(img_arr[i]))
print(img_as_tenosr)
