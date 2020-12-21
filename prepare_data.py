import sys
sys.path.insert(1, './data_transform')
sys.path.insert(2, '../DOTA_devkit')

from ImgSplit import splitbase
from YOLO_Transform import dota2darknet
import dota_utils as util

split = splitbase(r'./example', 
                 r'./examplesplit', choosebestpoint=True)
split.splitdata(0.5)

dota2darknet('./examplesplit/images',
             './examplesplit/labelTxt',
             './examplesplit/labels',
             util.wordname_15)