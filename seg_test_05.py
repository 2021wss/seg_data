import cv2
import os
import copy

def DataAugment(dir_path):
    if not os.path.exists(dir_path):
        print('路径不存在')
    else:
        dirs = os.listdir(dir_path)

        for subdir in dirs:
            print(subdir)
            sub_dir = dir_path + '/' + subdir
            img = cv2.imread(sub_dir)

            size = img.shape # 获得图像的形状

            iLR = copy.deepcopy(img) # 获得一个与原始图像相同的图像，注意这里要使用深度复制
            h = size[0]
            w = size[1]

            for i in range(h):
                for j in range(w):
                    iLR[i,w-j-1] = img[i,j]
            
            new_name = "%s" % (sub_dir)
            cv2.imwrite(new_name,iLR)


if __name__ == '__main__':
    dir_path = 'D:/Pancreas-CT/new/results/annotations/testing/'
    DataAugment(dir_path)