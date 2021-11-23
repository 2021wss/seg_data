import cv2

if __name__ == '__main__':
    data_path = 'PANCREAS_0061_data_testing_71.jpg'
    img = cv2.imread(data_path)
    size = img.shape
    print(size)
    print(img.size)