# Final-645

## Train
download the DOTA dataset.

Use the DOTA_devkit/ImgSplit.py to split the images and labels. (image of size 1024*1024)
  ```
  from ImgSplit import splitbase
  
  split = splitbase(r'DOTA_Data', r'examplesplit', choosebestpoint=True)
  split.splitdata(0.5)
  
  ```
