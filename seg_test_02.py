#-*- coding:utf-8 -*-
# 遍历文件夹
import os  
# nii格式一般都会用到这个包
import nibabel as nib  
# 转换成图像 
import numpy as np
import imageio
from PIL import Image
# 主函数
def nii_to_image(self):   
    #读取nii.gz文件夹
    filenames_data = os.listdir(filepath_data)
    filenames_label = os.listdir(filepath_label)
    # data
    for d in filenames_data:
        img_path = os.path.join(filepath_data,d)
#        print('img_path = ',img_path)
        img = nib.load(img_path)  # 读取nii
        img_ddata = img.get_fdata()
        # clip the image within [-125,275]
#        data_clipped = np.clip(img_ddata,-2050,1600)
        # normalised each 3D image to [0,1]
#        data_normalised = (data_clipped - (-2050) / (1600 - (-2050)))

        img_name = d.split(".")[0] # 此处掉了.nii.gz的后缀
#        print('img_name = ',img_name)
        img_d_path_x = os.path.join(imgfile_data_x,img_name)
#        print('imgfile_data_x = ',imgfile_data_x)
#        print('img_d_path_x = ',img_d_path_x)
        img_d_path_y = os.path.join(imgfile_data_y,img_name)
#        print('img_d_path_x = ',img_d_path_y)
        img_d_path_z = os.path.join(imgfile_data_z,img_name)
#        print('img_d_path_x = ',img_d_path_z)

        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_d_path_x):
            # 新建文件夹
            os.mkdir(img_d_path_x) 
        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_d_path_y):
            # 新建文件夹
            os.mkdir(img_d_path_y) 
        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_d_path_z):
            # 新建文件夹
            os.mkdir(img_d_path_z) 

        # 开始转换为图像
        # z是图像的序列
        for i in range(img.shape[2]):
            # 选择哪个方向的切片都可以
            """
            slice_x = data_normalised[i, :, :] * 255
            slice_x = Image.fromarray(slice_x)
            slice_x = slice_x.convert("L")
            
            slice_y = data_normalised[:, i, :] * 255
            slice_y = Image.fromarray(slice_y)
            slice_y = slice_y.convert("L")

            slice_z = data_normalised[:, :, i] * 255
            slice_z = Image.fromarray(slice_z)
            slice_z = slice_z.convert("L")            
            """
            slice_x = img_ddata[i, :, :]
            slice_x = Image.fromarray(slice_x)
            slice_x = slice_x.convert("RGB")            
            slice_y = img_ddata[:, i, :]
            slice_y = Image.fromarray(slice_y)
            slice_y = slice_y.convert("RGB")
            slice_z = img_ddata[:, :, i]
            slice_z = Image.fromarray(slice_z)
            slice_z = slice_z.convert("RGB")
            # 保存图像
            imageio.imwrite(os.path.join(img_d_path_x, img_name + '_train_x_' + '{}.jpg'.format(i)), slice_x)
            imageio.imwrite(os.path.join(img_d_path_y, img_name + '_train_y_' + '{}.jpg'.format(i)), slice_y)
            imageio.imwrite(os.path.join(img_d_path_z, img_name + '_train_z_' + '{}.jpg'.format(i)), slice_z)

    # label
    for l in filenames_label:
        img_path = os.path.join(filepath_label, l)
        img = nib.load(img_path)  # 读取nii.gz
        img_ldata = img.get_fdata()

        # 去掉nii的后缀名
        lname = l.split(".")[0] # 此处掉了.nii.gz的后缀 
        img_l_path_x = os.path.join(imgfile_label_x, lname)
        img_l_path_y = os.path.join(imgfile_label_y, lname)
        img_l_path_z = os.path.join(imgfile_label_z, lname)

        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_l_path_x):
            # 新建文件夹
            os.mkdir(img_l_path_x)  
        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_l_path_y):
            # 新建文件夹
            os.mkdir(img_l_path_y) 
        # 创建nii对应的图像的文件夹
        if not os.path.exists(img_l_path_z):
            # 新建文件夹
            os.mkdir(img_l_path_z) 
            
        # 开始转换为图像
        (x, y, z) = img.shape
        # z是图像的序列
        for i in range(z):
            # 选择哪个方向的切片都可以
            slice_x = img_ldata[i, :, :]
            slice_y = img_ldata[:, i, :]
            slice_z = img_ldata[:, :, i]
            # 保存图像
            imageio.imwrite(os.path.join(img_l_path_x, lname + '_train_x_' + '{}.png'.format(i)), slice_x)
            imageio.imwrite(os.path.join(img_l_path_y, lname + '_train_y_' + '{}.png'.format(i)), slice_y)
            imageio.imwrite(os.path.join(img_l_path_z, lname + '_train_z_' + '{}.png'.format(i)), slice_z)

if __name__ == "__main__":
    filepath_data = 'D:/Pancreas-CT/data/'
    filepath_label = 'D:/Pancreas-CT/label/'    
    imgfile_data_x = 'D:/Pancreas-CT/datasets/train_x/'
    imgfile_data_y = 'D:/Pancreas-CT/datasets/train_y/'
    imgfile_data_z = 'D:/Pancreas-CT/datasets/train_z/'
    imgfile_label_x = 'D:/Pancreas-CT/datasets/label_x/'
    imgfile_label_y = 'D:/Pancreas-CT/datasets/label_y/'
    imgfile_label_z = 'D:/Pancreas-CT/datasets/label_z/'  
    nii_to_image(filepath_data)
    nii_to_image(filepath_label)
    nii_to_image()