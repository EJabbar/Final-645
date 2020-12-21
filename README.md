# Final-645

## Structure

1- clone darknet, DOTA_devkit, and this repository in a directory.
  ```
  !git clone https://github.com/EJabbar/Final-645.git
  !git clone https://github.com/pjreddie/darknet.git
  !git clone https://github.com/CAPTAIN-WHU/DOTA_devkit.git
  
  ```
 2- Make darknet.
 
  ```
  make -C ./darknet
  
  ```
  3- Move to the "./Final-645" directory and unzip the images and labels of the DOTA dataset in the "./example" directory.
  
  ```
  cd ./Final-645
  mkdir example
  mkdir ./example/labelTxt
  unzip <PATH_TO_LABELS_ZIP_FILE> -d ./example/labelTxt
  unzip <PATH_TO_IMAGES_ZIP_FILES> -d ./example/
  
  ```
  
 4- Split large images (maximum size 1024*1024)
    Convert DOTA labels format to Darknet labels format.

  ```
  python prepare_data.py
  
  ```

  ```
.
├── Final-645
│   ├── README.md
│   ├── backup
│   ├── cfg
│   │   ├── dota.data
│   │   └── yolo-dota.cfg
│   ├── data
│   │   ├── dota.names
│   │   └── labels
│   │       ├── 100_0.png
│   │       ├── ...
│   │       └── make_labels.py
│   ├── data_transform
│   │   ├── YOLO_Transform.py
│   │   ├── dota_utils.py
│   │   └── imagetrans.py
│   ├── examplesplit
│   │   ├── images
│   │   │   └── sample-1.png
│   │   ├── labels
│   │   │   └── sample-1.txt
│   │   ├── results
│   │   │   └── result_test-1.png
│   │   ├── test.txt
│   │   ├── tests
│   │   │   └── test-1.png
│   │   └── train.txt
│   ├── test_dota.sh
│   └── train_dota.sh
├── darknet
├── DOTA_devkit

  ```

## Train

1- Create a backup directory.
  ```
  mkdir ./backup
  ```
2- Modify the cfg/dota.data config file to point to your data
  ```
  classes=15
  train=<PATH_TO_DIR>/examplesplit/train.txt
  valid=<PATH_TO_DIR>/examplesplit/test.txt
  names=data/dota.names
  backup=<PATH_TO_DIR>/backup
  
  ```
3- List the full path of all training and test images in the "examplesplit/train.txt" and "examplesplit/test.txt" files. 

4- Download the model weights pre-trained on ImageNet in the same directory of "train_dota.sh".
   Run the train.sh script.

  ```
  wget https://pjreddie.com/media/files/darknet19_448.conv.23
  sh train_dota.sh 
  
  ```
  
 
## Test

1- Download the trained weights (or use the weights that learned in the training phase). Put the file in the "./backup" directroy.

2- Put all the test images in the "./examplesplit/tests" directory. (max size of images: 1024*1024)

3- Run the test script.


  ```
  wget https://pjreddie.com/media/files/darknet19_448.conv.23
  sh test_dota.sh
  
  ```
4- Results will be saved in "./examplesplit/results" directory.
