import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans

def load_data(file_path):
    f = open(file_path,'rb') # 二进制打开
    data = []
    img = image.open(f) # 以列表形式返回相片像素值
    m,n = img.size # 获得图片大小
#    print(m,n)
    for i in range(m):
        for j in range(n): # 将每个像素点RGB颜色处理到0-1范围内并存放到data
#            print(img.getpixel((i,j)))
            x,y,z = img.getpixel((i,j))
            data.append([x/256.0,y/256.0,z/256.0])
    f.close()
    return np.vstack(data),m,n  #以矩阵形式返回data,图片大小

img_data,row,col = load_data('PANCREAS_0001_train_z_131.jpg')
label = KMeans(n_clusters = 2).fit_predict(img_data) #聚类中心的个数为3
label = label.reshape([row,col])  # 聚类获得每个像素所属的类别
pic_new = image.new("L",(row,col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i,j),int(256/(label[i][j] + 1)))
pic_new.save('n_clusters2.jpg')