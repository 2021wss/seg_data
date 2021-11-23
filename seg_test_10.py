# OpenCV方式
import cv2
import os
from tqdm import tqdm

img_datapath = 'D:/Pancreas-CT/new/results/test_test/images1/testing_png/' # 原图
label_datapath = 'D:/Pancreas-CT/new/results/test_test/annotations1/testing/' # 对应的label 0-255 二值
img_label_datapath = 'D:/Pancreas-CT/new/results/test_test/images1/testing_label_1/'

# addWeighted()函数是将两张相同大小，相同类型的图片（叠加）线性融合的函数，可以实现图片的特效

for _,_,files in os.walk(img_datapath):
    for f in tqdm(files):
        image = cv2.imread(os.path.join(img_datapath,f))
        label = cv2.imread(os.path.join(label_datapath,f))
        label_img = cv2.addWeighted(image,0.7,label,0.3,10) # image的权重是0.7，label的权重是0.3
        # 相当于对图片做一个亮度调整，gamma为0的话代表不调整，gamma为10，图片每个像素加上10，相当于提高亮度，这个值也可以是负的
        cv2.imwrite(img_label_datapath + '/' + f,label_img)