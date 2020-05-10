import cv2
import os

def resize_testdata():
    """Function to create new resized test images"""
    
    train_path = './Dataset/new_dataset/train/'
    val_path = "./Dataset/new_dataset/val/"

    new_train_path = "./Dataset/ds_resize_gray/train/"
    new_val_path = "./Dataset/ds_resize_gray/val/"

    os.makedirs(new_val_path)
    os.makedirs(new_train_path)

    for path in [train_path,val_path]:
        dir_list = os.listdir(path)
        
        for dir in dir_list:
            if dir.startswith('.') is False:
                if path is train_path:
                    os.mkdir(new_train_path + dir)
                else:
                    os.mkdir(new_val_path + dir)

                img_list = os.listdir(path + dir)
                
                for img in img_list:
                    if img.startswith('.') is False:
                        src  = cv2.imread(path + dir + '/' + img, cv2.IMREAD_GRAYSCALE)
                        dist = cv2.resize(src,(256,256))
                        if path is train_path:
                            cv2.imwrite(new_train_path + dir + '/' + img , dist)
                        else:
                            cv2.imwrite(new_val_path + dir + '/' + img , dist)

if __name__ == "__main__":
    resize_testdata()