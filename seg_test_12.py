from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('PANCREAS_0001_train_z_131.jpg') # 打开图像
gray = img.convert('L')               # 转换成灰度
r,g,b = img.split()                   # 分离三通道
pic = Image.merge('RGB',(r,g,b))      # 合并三通道

# 原图
plt.figure("beauty")
plt.subplot(2,3,1)
plt.title('origin')
plt.imshow(img)
plt.axis('off') # 坐标轴

# 灰度图
plt.subplot(2,3,2)
plt.title('gray')
plt.imshow(gray,cmap = 'gray')
plt.axis('off')

# 三通道合并图
plt.subplot(2,3,3)
plt.title('merge')
plt.imshow(pic)
plt.axis('off')

# 只有R通道图
plt.subplot(2,3,4)
plt.title('r')
plt.imshow(r,cmap = 'gray')
plt.axis('off')

# 只有G通道图
plt.subplot(2,3,5)
plt.title('g')
plt.imshow(g,cmap = 'gray')
plt.axis('off')

# 只有B通道图
plt.subplot(2,3,6)
plt.title('b')
plt.imshow(b,cmap = 'gray')
plt.axis('off')
plt.show()