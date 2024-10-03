from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iris=load_iris()
print(iris.keys())

print("資料筆數:")
print(iris.data.shape,"\n")

print("資料欄位名稱，分別是:")
print(iris.feature_names,"\n")

print("第一筆資料內容:")
print(iris.data[0],"\n")

print("第一筆的預測目標:")
print(iris.target[0],"\n")

#製作散布圖(花萼長度和花萼寬度)
scatter=plt.scatter(iris.data[:,0],iris.data[:,1],c=iris.target)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend(handles=scatter.legend_elements()[0],labels=iris.target_names.tolist())

#製作散布圖(花瓣長度和花瓣寬度)
scatter=plt.scatter(iris.data[:,2],iris.data[:,3],c=iris.target)
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.legend(handles=scatter.legend_elements()[0],labels=iris.target_names.tolist())

#KMeans模型將資料分成三群
estimator=KMeans(n_clusters=3)
estimator.fit(iris.data)
print(estimator.labels_)
estimator.cluster_centers_

#用原始label作圖
scatter=plt.scatter(iris.data[:,2],iris.data[:,3],c=iris.target)
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.legend(handles=scatter.legend_elements()[0],labels=iris.target_names.tolist())
#用K-Means分權好的label來作圖
scatter=plt.scatter(iris.data[:,2],iris.data[:,3],c=estimator.labels_)
plt.xlabel('Petal length')
plt.ylabel('Petal width')
#把質心用紅色星星標出來
plt.scatter(estimator.cluster_centers_[:,2],estimator.cluster_centers_[:,3],marker='*',c='red',s=100)
plt.legend(*scatter.legend_elements())
plt.show()

#3D繪圖(環境)
#elev不同高度視角，azim不同水平角度
fig=plt.figure(figsize=(8,6))
ax=Axes3D(fig,rect=[0,0,.95,1],elev=40,azim=130)
ax.set_zlim(2,4.5)
#3D繪圖(原始資料)(花瓣長度，花瓣寬度，花萼寬度)
ax.scatter(iris.data[:,2],iris.data[:,3],iris.data[:,1],c=iris.target)
ax.scatter(estimator.cluster_centers_[:,2],estimator.cluster_centers_[:,3],estimator.cluster_centers_[:,1],marker='*',c='red',s=100)
plt.legend(*scatter.legend_elements(),loc='lower right')
plt.show()

##3D繪圖(分群資料)(花瓣長度，花瓣寬度，花萼寬度)
ax.scatter(iris.data[:,2],iris.data[:,3],iris.data[:,1],c=estimator.labels_)
plt.legend(handles=scatter.legend_elements()[0],labels=iris.target_names.tolidsst(),loc='lower right')
plt.show()