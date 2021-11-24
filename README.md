# seg_data
seg_test_01.py  .nii文件转化为.stl文件，但是问题在于生成的文件过大，既占用空间又不易理解
seg_test_02.py  .nii文件转化为.png文件，按x/y/z三个轴来对数据集文件进行切分，最后生成的文件转为RGB格式
seg_test_03.py  对图片进行聚类操作， n_culster=3时效果最好
seg_test_04.py  数据文件/label文件批量转化
seg_test_05.py  对图片进行水平镜像翻转，因为上一个文件转化出的label文件需要镜像翻转之后才能与数据文件匹配
seg_test_06.py  将label中的图像转化为0-255二值文件
seg_test_07.py  瞅一眼自己图片的尺寸
seg_test_08.py  在数据文件中勾勒label中的形状，需要两个文件格式一样
seg_test_09.py  将.jpg批量转化为.png
seg_test_10.py  将label文件映射到data文件上
seg_test_11.py  修改label文件的像素值
seg_test_12.py  展示图片的一些操作
