# Mobilenetv3_SSD
大量參考(Debug):https://github.com/shaoshengsong/MobileNetV3-SSD-Compact-Version/blob/master/README.md

 
**環境**   
Ubuntu18.04  
PyTorch 1.4

Dataset格式支援：VOC2007

**一. 下載數據**  
Training Set:   
`wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar`  
Testing Set :  
`wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar`

Extract:  
`tar xvf VOCtrainval_06-Nov-2007.tar`  
`tar xvf VOCtest_06-Nov-2007.tar`  

再把training跟testing的資料夾合併，將Annotations與JPEGImages丟入 MobilenetV3_SSD/VOC2007內再分別找到VOCtest_06-Nov-2007/VOCdevkit/VOC2007/ImageSets/Main/test.txt，
與VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt   
將test.txt與trainval.txt放入MobilenetV3_SSD/VOC2007/ImageSets/Main

**二.生成 TEST_images.json,TEST_objects.json,TRAIN_images.json,TRAIN_objects.json**  
先打開create_data_lists.py
