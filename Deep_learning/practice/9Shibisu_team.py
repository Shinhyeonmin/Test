from PIL import Image
import numpy as np

img = Image.open("./hand_img/a2.jpg")

print(img.size)

img = img.resize((100,100),Image.ANTIALIAS)

print(img.size)

print(type(img))