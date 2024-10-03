from sklearn.datasets import load_breast_cancer#乳癌資料集
from sklearn.neighbors import KNeighborsClassifier#KNN模型
from sklearn.model_selection import train_test_split#切割資料集

my_data=load_breast_cancer()
print(my_data.keys())

print("資料筆數:")
print(my_data.data.shape)
print("\n")

print("第一筆資料內容:")
print(my_data.data[0])
print("\n")
#觀察第一筆分類目標
print("第一筆的分類目標:")
print(my_data.target[0])
print("\n")
#觀察要預測目標的名稱種類
print("預測目標的名稱種類，分別是惡性腫瘤及良性腫瘤:")
print(my_data.target_names)
print("\n")

#設定x是資料，y是答案
#切割資料集(80%是訓練集，20%是測試集)
train_x,test_x,train_y,test_y=train_test_split(my_data.data,my_data.target,test_size=0.2,random_state=18,shuffle=True)

print("原始資料的維度大小:",my_data.data.shape)
print("訓練集的維度大小:",train_x.shape)
print("測試集的維度大小:",test_x.shape)

#訓練模型(預設K值為5)
my_model=KNeighborsClassifier()
my_model.fit(train_x,train_y)
#評分
test_score=my_model.score(test_x,test_y)
print("模型評估完測試集的準確度為:",test_score)
