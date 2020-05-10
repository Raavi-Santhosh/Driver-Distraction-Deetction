import cv2
import os

def resize_testdata():
    """Function to create new resized test images"""
    
    test_path = "./Dataset/imgs/test/"
    new_test_path = "./Dataset/new_imgs/test/"

    imgs_list = os.listdir(test_path)
    os.makedirs(new_test_path)
    for img in imgs_list:
        src = cv2.imread(test_path+img,cv2.IMREAD_COLOR)
        dist = cv2.resize(src,(256,256))
        dist = cv2.cvtColor(dist,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(new_test_path+img, dist)

def resize_traindata():
    """Function to create new resized train images"""

    train_path = "./Dataset/imgs/train/"
    new_train_path = "./Dataset/new_imgs/train/"

    dirs_list = os.listdir(train_path)
    os.makedirs(new_train_path)
    for dir in dirs_list:
        os.mkdir(new_train_path+dir)
        imgs_list = os.listdir(train_path+dir)
        for img in imgs_list:
            src = cv2.imread(train_path+dir+'/'+img)
            dist = cv2.resize(src,(256,256))
            dist = cv2.cvtColor(dist,cv2.COLOR_BGR2GRAY)
            cv2.imwrite(new_train_path+dir+'/'+img,dist)

resize_testdata()
resize_traindata()