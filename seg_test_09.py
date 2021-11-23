import os
import cv2
from PIL import Image
import imageio

def JPG_PNG(Jpgpath):
    
    Jpg_path = os.listdir(Jpgpath)
#    print(Jpg_path)

    for f in Jpg_path:
        img = Image.open(os.path.join(jpg_path,f))
#        print(img)
        jpg_name = f.split(".")[0]
        print(jpg_name)
        img.save(os.path.join(png_path,jpg_name + '.png'))


if __name__ == "__main__":
    jpg_path = 'D:/Pancreas-CT/new/results/test_test/images1/validation/'
    png_path = 'D:/Pancreas-CT/new/results/test_test/images1/validation_png/'
    JPG_PNG(jpg_path)

