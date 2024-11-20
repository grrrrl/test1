import cv2
import numpy as np


# 感知哈希算法
def pHash(image):
    image = cv2.resize(image, (32, 32), interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('image', image)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    # 将灰度图转为浮点型，再进行dct变换
    dct = cv2.dct(np.float32(image))
    #     print(dct)
    # 取左上角的8*8，这些代表图片的最低频率
    # 这个操作等价于c++中利用opencv实现的掩码操作
    # 在python中进行掩码操作，可以直接这样取出图像矩阵的某一部分
    dct_roi = dct[0:8, 0:8]
    avreage = np.mean(dct_roi)
    hash = []
    for i in range(dct_roi.shape[0]):
        for j in range(dct_roi.shape[1]):
            if dct_roi[i, j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash


# 计算汉明距离
def Hamming_distance(hash1, hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num


if __name__ == "__main__":
    image_file1 = './2.jpg'
    image_file2 = './3.jpg'
    img1 = cv2.imread(image_file1)
    img2 = cv2.imread(image_file2)
    hash1 = pHash(img1)
    hash2 = pHash(img2)
    dist = Hamming_distance(hash1, hash2)
    # 将距离转化为相似度
    similarity = 1 - dist * 1.0 / 64
    print(dist)
    print(similarity)
