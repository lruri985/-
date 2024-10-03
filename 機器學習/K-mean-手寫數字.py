from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

digits=load_digits()
print(digits.keys())
print("資料筆數:")
print(digits.data.shape,"\n")

print("資料欄位名稱，分別是:")
print(digits.target_names,"\n")

print("第一筆資料內容:")
print(digits.data[0],"\n")

print("第一筆的影像內容:")
print(digits.images[0],"\n")
plt.imshow(digits.images[0],cmap=plt.cm.binary)

print("第一筆的預測目標:")
print(digits.target[0],"\n")

#一次看前十筆圖像資料
#第一列
plt.figure(figsize=(10,10))
for i in range(1,6):
    plt.subplot(1,5,i)
    plt.imshow(digits.images[i],cmap=plt.cm.binary)
plt.show()
#第二列
plt.figure(figsize=(10,10))
for i in range(6,11):
    plt.subplot(2,5,i)
    plt.imshow(digits.images[i],cmap=plt.cm.binary)
plt.show()

#訓練模型(分十群)
estimator=KMeans(n_clusters=10)
estimator.fit(digits.data)
c_0=np.where(estimator.labels_==0)[0]
c_1=np.where(estimator.labels_==1)[0]
c_2=np.where(estimator.labels_==2)[0]
print(c_0[0:10],c_1[0:10],c_2[0:10],sep="\n")

#將集群分為三列，把圖列出來
#第一列
plt.figure(figsize=(20,20))
for i in range(1,11):
    plt.subplot(1,10,i)
    plt.imshow(digits.images[c_0[i]],cmap=plt.cm.binary,interpolation='sinc')
plt.show()
#第二列
plt.figure(figsize=(20,20))
for i in range(1,11):
    plt.subplot(2,10,i)
    plt.imshow(digits.images[c_1[i]],cmap=plt.cm.binary,interpolation='sinc')
plt.show()
#第三列
plt.figure(figsize=(20,20))
for i in range(1,11):
    plt.subplot(3,10,i)
    plt.imshow(digits.images[c_2[i]],cmap=plt.cm.binary,interpolation='sinc')
plt.show()

#訓練模型(分三群)
estimator=KMeans(n_clusters=3)
estimator.fit(digits.data)
c_0=np.where(estimator.labels_==0)[0]
c_1=np.where(estimator.labels_==1)[0]
c_2=np.where(estimator.labels_==2)[0]
print(c_0[0:10],c_1[0:10],c_2[0:10],sep="\n")

#將集群分為三列，把圖列出來
#第一列
plt.figure(figsize=(20,20))
for i in range(1,11):
    plt.subplot(1,10,i)
    plt.imshow(digits.images[c_0[i]],cmap=plt.cm.binary,interpolation='sinc')
plt.show()
#第二列
plt.figure(figsize=(20,20))
for i in range(1,11):
    plt.subplot(2,10,i)
    plt.imshow(digits.images[c_1[i]],cmap=plt.cm.binary,interpolation='sinc')
plt.show()
#第三列
plt.figure(figsize=(20,20))
for i in range(1,11):
    plt.subplot(3,10,i)
    plt.imshow(digits.images[c_2[i]],cmap=plt.cm.binary,interpolation='sinc')
plt.show()