import os
import random 
 
filepath=r'VOC/JPEGImages'
saveBasePath=r"VOC"
 
trainval_percent=1
train_percent=0.7
total_xml = os.listdir(filepath)
#a=total_xml[1].split('.jpg')
#print(a[0])

num=len(total_xml)  
print(num)
#assert 0
list=range(num)  
tv=int(num*trainval_percent)  
tr=int(tv*train_percent)  
trainval= random.sample(list,tv)  
train=random.sample(trainval,tr)  
 
print("train and val size:",tv)
print("train size:",tr)

ftrainval = open(os.path.join(saveBasePath,'ImageSets/Main/trainval.txt'), 'w')  
ftrain = open(os.path.join(saveBasePath,'ImageSets/Main/train.txt'), 'w')  
fval = open(os.path.join(saveBasePath,'ImageSets/Main/test.txt'), 'w')  


for i  in list: 
    a=total_xml[i].split('.jpg')
    name=a[0]+'\n'  
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
 
  
ftrainval.close()  
ftrain.close()  
fval.close()
