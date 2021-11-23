#-*- coding:utf-8 -*-
import os
import nibabel as nib
import imageio
## .nii to .stl
## 问题是：生成文件过大，且表意不明
import vtk
import glob
import SimpleITK as sitk
import numpy as np

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"

def nii_to_image(self):
    
    #读取nii.gz文件夹
    filenames_data = os.listdir(filepath_data)
    filenames_label = os.listdir(filepath_label)

    #读取nii.gz文件
    for d in filenames_data:
        d = d.split(".")[0]
        print(d)
        img_path = os.path.join(filepath_data,d)
        img_name = img_path.split(".")[0]
        print(img_name)
#        img_ddata = img_name.getfdata()
        multi_label_image = sitk.ReadImage(img_path)
        img_npy = sitk.GetArrayFromImage(multi_label_image)
        labels = np.unique(img_npy)

        reader = vtk.vtkNIFTIImageReader()
        reader.SetFileName(img_path)
        reader.Update()

        for label in labels:
            if int(label) != 0:

                surf = vtk.vtkDiscreteMarchingCubes()
                surf.SetInputConnection(reader.GetOutputPort())
                surf.SetValue(0,int(label))
                surf.Update()

                smoother = vtk.vtkWindowedSincPolyDataFilter()
                if vtk.VTK_MAJOR_VERSION <= 5:
                    smoother.SetInput(surf.GetOutput())
                else:
                    smoother.SetInputConnection(surf.GetOutputPort())
                
                smoother.SetNumberOfIterations(30)
                smoother.NonManifoldSmoothingOn()
                smoother.NormalizeCoordinatesOn()
                smoother.GenerateErrorScalarsOn()
                smoother.Update()

                writer = vtk.vtkSTLWriter()
                writer.SetInputConnection(smoother.GetOutputPort())
                writer.SetFileTypeToASCII()

                writer.SetFileName(f'{img_name}_{label}.stl')
                writer.Write()

if __name__ == "__main__":
    filepath_data = 'D:/Pancreas-CT/data/'
    filepath_label = 'D:/Pancreas-CT/label/'
    nii_to_image(filepath_data)
