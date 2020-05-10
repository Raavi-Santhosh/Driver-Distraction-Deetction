import cv2
import os

def preprocess():
    TEST_PATH = "./Dataset/imgs/test/"
    NEW_TEST_PATH = "./Dataset/ds_resize_gray/test/"

    os.makedirs(NEW_TEST_PATH)

    img_list = os.listdir(TEST_PATH)
    for image in img_list:
        if image.startswith(".") is False:
            src = cv2.imread(TEST_PATH + image,cv2.IMREAD_GRAYSCALE)
            dist = cv2.resize(src,(256,256))
            cv2.imwrite(NEW_TEST_PATH + image,dist)

if __name__ == "__main__":
    preprocess()
