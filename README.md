# Final-645

## Train
1- download the DOTA dataset.

2- Use the DOTA_devkit/ImgSplit.py to split the images and labels. (image of size 1024*1024)
  ```
  from ImgSplit import splitbase
  
  split = splitbase(r'DOTA_Data', r'examplesplit', choosebestpoint=True)
  split.splitdata(0.5)
  
  ```
3- Copy the generated images and labels to the "examplesplit/images" and "examplesplit/labelTxt" directories.

4- Convert the Label Format of DOTA to Darknet.
  ```
  import sys

  from YOLO_Transform import dota2darknet

  import dota_utils as util
  dota2darknet('/content/examplesplit/images',
               '/content/examplesplit/labelTxt',
               '/content/examplesplit/labels',
               util.wordname_15)
  ```


5- Modify the cfg/dota.data config file to point to your data
  ```
  classes=15
  train=<PATH_TO_DIR>/examplesplit/train.txt
  valid=<PATH_TO_DIR>/examplesplit/test.txt
  names=data/dota.names
  backup=<PATH_TO_DIR>/backup
  
  ```
6- List the full path of all training and test images in the "examplesplit/train.txt" and "examplesplit/test.txt" files. 

7- Move to the main directory. Download the model weights pre-trained on ImageNet. Run the train.sh script.

  ```
  wget https://pjreddie.com/media/files/darknet19_448.conv.23
  sh train-dota.sh 
  
  ```
