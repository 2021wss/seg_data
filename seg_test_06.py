import PIL.Image as Image
from tqdm import tqdm
import numpy as np
import os 
import time

data_path = 'D:/Pancreas-CT/new/results/annotations/training/'
# data_path1 = 'D:/Pancreas-CT/old/train_data_z/PANCREAS_0001-1/'

for _,_,files in os.walk(data_path):
    for f in tqdm(files):
        img = Image.open(os.path.join(data_path,f))
        img = np.asarray(img).copy()
        img[img <= 100] = 0
        img[img > 100] = 255
        img = Image.fromarray(img)
#        img = img.convert("RGB")
        img.save(os.path.join(data_path,f))

