import os
import numpy as np
from PIL import Image
from tqdm import tqdm

def generate_rgb(gray_array):
    print('gray_array.shape',gray_array.shape) # 打印出灰度图的shape
    x = gray_array.shape[0]
    y = gray_array.shape[1]
    rgb = np.zeros([x,y,3],int) # 扩充为rgb通道
    gray_array = np.array(gray_array) # 化为矩阵形式
    for i in range(x):
        for j in range(y):
            if gray_array[i,j,0] & gray_array[i,j,1] & gray_array[i,j,2] == 255: # 目标体（原来为白色）
                rgb[i,j,0] = 255       # rgb通道的，r（红色）通道
                rgb[i,j,1] = 0         # rgb通道的，g（绿色）通道
                rgb[i,j,2] = 0         # rgb通道的，b（蓝色）通道
            
            if gray_array[i,j,0] & gray_array[i,j,1] & gray_array[i,j,2] == 0:   # 目标体（原来为黑色）
                rgb[i,j,0] = 0         # rgb通道的，r（红色）通道
                rgb[i,j,1] = 255       # rgb通道的，g（绿色）通道
                rgb[i,j,2] = 0         # rgb通道的，b（蓝色）通道                
    return rgb

label_datapath = 'D:/Pancreas-CT/new/results/test_test/annotations1/testing/' # 对应的label 0-255 二值
label_datapath_rgb = 'D:/Pancreas-CT/new/results/test_test/annotations1/testing_rgb/'

for _,_,files in os.walk(label_datapath):
    for f in tqdm(files):
        source_img = Image.open(os.path.join(label_datapath,f)) # 读取照片
        source_img = np.array(source_img) # 化为矩阵
        img = generate_rgb(source_img) # 调用generate_rgb函数
        img = Image.fromarray(np.uint8(img))
        img.save(label_datapath_rgb + '/' + f)      