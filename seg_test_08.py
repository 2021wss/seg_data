import cv2
import os
from PIL import Image 
import matplotlib.image as mping
import numpy as np
import matplotlib.pyplot as plt 
from tqdm import tqdm

img_datapath = 'D:/Pancreas-CT/new/results/test_test/images1/validation_png/'
label_datapath = 'D:/Pancreas-CT/new/results/test_test/annotations1/validation/'

for _,_,files in os.walk(img_datapath):
    for f in tqdm(files):
        img = cv2.imread(os.path.join(img_datapath,f), 1)
        label = cv2.imread(os.path.join(label_datapath,f), 0)

        contours,_ = cv2.findContours(label, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, contours, -1, (0,0,255), 2)

        img = img[:,:,::-1]
        img[..., 2] = np.where(label == 1, 255, img[..., 2])

#        plt.imshow(img)
#        plt.show()

        img = Image.fromarray(img)
        img.save('D:/Pancreas-CT/new/results/test_test/images1/validation_label' + '/' + f)