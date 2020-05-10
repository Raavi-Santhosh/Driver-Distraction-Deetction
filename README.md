# Driver Distraction Detection

Download the dataset form [kaggle](https://www.kaggle.com/c/state-farm-distracted-driver-detection).

1. Use **train_val_split.py** python script to divide the train dataset into train and validation

2. Use **resize_gray.py** python script to resize the images in train and val folder into 256X256 in gray-scale to reduce the computation.

3. You can use the model which is save in **Saved Model** folder to make predictions

4. The Evaluated accuracy is **95%**. You can push this accuracy by training the model from the saved point.

5. Walkthrough the **Model Implementation Notebook** at the end *test_model()* function predicts the images by taking the images randomly.


#### Sample output

![](https://github.com/Raavi-Santhosh/Driver-Distraction-Deetction/blob/master/predicted.jpg "sample prediction")
