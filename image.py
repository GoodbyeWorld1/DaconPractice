import numpy as np
import matplotlib.pyplot as plt
#Open Train Image
trainImgFile=open('dataset/train.csv','rt')

train=[]
#Read File
data=trainImgFile.readline()
data=trainImgFile.readline()
#print(data.split(','))
while data:
    data=data.split(',')
    #print(data)
    num=data[1]
    letter=data[2]
    imgData=data[3:]
    train.append({'digit':int(num),'letter':letter,'img':np.asarray(imgData,dtype=int)})
    data=trainImgFile.readline()

plt.figure()
for i in range(100):
    plt.subplot(10,10,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train[i]['img'].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(str(train[i]['digit'])+' '+train[i]['letter'])
plt.show()

trainImgFile.close()