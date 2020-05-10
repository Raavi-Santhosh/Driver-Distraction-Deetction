import cv2
import os
import random
import shutil

def train_validate_split(train_size = 0.8):

    train_images_path = "./Dataset/imgs/train/"
    new_dataset_path = "./Dataset/new_dataset/"

    os.makedirs(new_dataset_path + "train/")
    os.makedirs(new_dataset_path + "val/")
    
    random.seed(2)

    TRAIN_SPLIT = train_size
    
    dir_list = os.listdir(train_images_path)

    for dir in dir_list:
        if dir.startswith("."):
            continue
        else:
            images_list = os.listdir(train_images_path + dir)
            dir_size = len(images_list)
            
            train_images = random.sample(images_list, round(dir_size * TRAIN_SPLIT))
            val_images = list(set(images_list) - set(train_images))
            
            os.makedirs(new_dataset_path + "train/" + dir)
            os.makedirs(new_dataset_path + "val/" + dir)
            
            for image in train_images:
                shutil.copy(train_images_path + dir + '/' + image , new_dataset_path + 'train/' + dir + '/' + image)

            for image in val_images:
                shutil.copy(train_images_path + dir + '/' + image , new_dataset_path + 'val/' + dir + '/' + image)
            
if __name__ == "__main__":
    train_validate_split()