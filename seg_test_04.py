#-*- coding:utf-8 -*-
# 遍历文件夹
import os  
# nii格式一般都会用到这个包
import nibabel as nib  
# 转换成图像 
import numpy as np
import imageio
from PIL import Image
from rich import print
# 主函数
def nii_to_image(self):   
    #读取nii.gz文件夹
    filenames_data_training = os.listdir(filepath_data_training)
    filenames_data_validation = os.listdir(filepath_data_validation)
    filenames_data_testing = os.listdir(filepath_data_testing)
    filenames_label_training = os.listdir(filepath_label_training)
    filenames_label_validation = os.listdir(filepath_label_validation)
    filenames_label_testing = os.listdir(filepath_label_testing)

## data
    # filenames_data_training
    for fdt in filenames_data_training:
#        print(filenames_data_training)
        img_path = os.path.join(filepath_data_training, fdt)
        img = nib.load(img_path)  # 读取nii
        img_ddata = img.get_fdata()
        img_name = fdt.split(".")[0] # 此处掉了.nii.gz的后缀

        # 开始转换为图像
        # z是图像的序列
        for i in range(img.shape[2]):
            slice_z = img_ddata[:, :, i]
            slice_z = Image.fromarray(slice_z)
            slice_z = slice_z.convert("RGB")
            # 保存图像
            imageio.imwrite(os.path.join(imgfile_data_training, img_name + '_data_training_' + '{}.jpg'.format(i)), slice_z)

    # filenames_data_training
    for fdv in filenames_data_validation:
#        print(filenames_data_validation)
        img_path = os.path.join(filepath_data_validation, fdv)
        img = nib.load(img_path)  # 读取nii
        img_ddata = img.get_fdata()
        img_name = fdv.split(".")[0] # 此处掉了.nii.gz的后缀

        # 开始转换为图像
        # z是图像的序列
        for i in range(img.shape[2]):
            slice_z = img_ddata[:, :, i]
            slice_z = Image.fromarray(slice_z)
            slice_z = slice_z.convert("RGB")
            # 保存图像
            imageio.imwrite(os.path.join(imgfile_data_validation, img_name + '_data_validation_' + '{}.jpg'.format(i)), slice_z)

    # filenames_data_testing
    for fdte in filenames_data_testing:
#        print(filenames_data_testing)
        img_path = os.path.join(filepath_data_testing, fdte)
        img = nib.load(img_path)  # 读取nii
        img_ddata = img.get_fdata()
        img_name = fdte.split(".")[0] # 此处掉了.nii.gz的后缀

        # 开始转换为图像
        # z是图像的序列
        for i in range(img.shape[2]):
            slice_z = img_ddata[:, :, i]
            slice_z = Image.fromarray(slice_z)
            slice_z = slice_z.convert("RGB")
            # 保存图像
            imageio.imwrite(os.path.join(imgfile_data_testing, img_name + '_data_testing_' + '{}.jpg'.format(i)), slice_z)
## label
    # filenames_label_training
    for flt in filenames_label_training:
#        print(filenames_label_training)
        img_path = os.path.join(filepath_label_training, flt)
        img = nib.load(img_path)  # 读取nii
        img_ddata = img.get_fdata()
        img_name = flt.split(".")[0] # 此处掉了.nii.gz的后缀

        # 开始转换为图像
        # z是图像的序列
        for i in range(img.shape[2]):
            slice_z = img_ddata[:, :, i]
            # 保存图像
            imageio.imwrite(os.path.join(imgfile_label_training, img_name + '_data_training_' + '{}.png'.format(i)), slice_z)

    # filenames_label_training
    for flv in filenames_label_validation:
#        print(filenames_label_validation)
        img_path = os.path.join(filepath_label_validation, flv)
        img = nib.load(img_path)  # 读取nii
        img_ddata = img.get_fdata()
        img_name = flv.split(".")[0] # 此处掉了.nii.gz的后缀

        # 开始转换为图像
        # z是图像的序列
        for i in range(img.shape[2]):
            slice_z = img_ddata[:, :, i]
            # 保存图像
            imageio.imwrite(os.path.join(imgfile_label_validation, img_name + '_data_validation_' + '{}.png'.format(i)), slice_z)

    # filenames_label_testing
    for flte in filenames_label_testing:
#        print(filenames_label_testing)
        img_path = os.path.join(filepath_label_testing, flte)
        img = nib.load(img_path)  # 读取nii
        img_ddata = img.get_fdata()
        img_name = flte.split(".")[0] # 此处掉了.nii.gz的后缀

        # 开始转换为图像
        # z是图像的序列
        for i in range(img.shape[2]):
            slice_z = img_ddata[:, :, i]
            # 保存图像
            imageio.imwrite(os.path.join(imgfile_label_testing, img_name + '_data_testing_' + '{}.png'.format(i)), slice_z)


if __name__ == "__main__":

    filepath_data_training = 'D:/Pancreas-CT/new/datasets/images/training/'
    filepath_data_validation = 'D:/Pancreas-CT/new/datasets/images/validation/'
    filepath_data_testing = 'D:/Pancreas-CT/new/datasets/images/testing/'

    imgfile_data_training = 'D:/Pancreas-CT/new/results/images/training/'
    imgfile_data_validation = 'D:/Pancreas-CT/new/results/images/validation/'
    imgfile_data_testing = 'D:/Pancreas-CT/new/results/images/testing/'
    
    filepath_label_training = 'D:/Pancreas-CT/new/datasets/annotations/training/'
    filepath_label_validation = 'D:/Pancreas-CT/new/datasets/annotations/validation/'
    filepath_label_testing = 'D:/Pancreas-CT/new/datasets/annotations/testing/'

    imgfile_label_training = 'D:/Pancreas-CT/new/results/annotations/training/'
    imgfile_label_validation = 'D:/Pancreas-CT/new/results/annotations/validation/'
    imgfile_label_testing = 'D:/Pancreas-CT/new/results/annotations/testing/'

    nii_to_image(filepath_data_training)
    nii_to_image(filepath_data_validation)
    nii_to_image(filepath_data_testing)
    nii_to_image(filepath_label_training)
    nii_to_image(filepath_label_validation)
    nii_to_image(filepath_label_testing)
    nii_to_image(None)