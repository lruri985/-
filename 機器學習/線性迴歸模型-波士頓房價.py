from sklearn.datasets import load_boston #波士頓價資料集
from  sklearn.linear_model import LinearRegression#線性迴歸模型
from sklearn.model_selection import train_test_split#切分訓練集和測試集
from sklearn.metrics import mean_squared_error#驗證模型

my_data=load_boston()
print("資料筆數:")
print(my_data.data.shape)
print("\n")

print("資料的欄位名稱，分別是:")
print(my_data.feature_names)
print("\n")

print("第一筆資料內容:")
print(my_data.data[0])
print("\n")

print("第一筆要預測的目標:")
print(my_data.target[0])
print("\n")

#設定x是資料，y是答案
#切割資料集(80%是訓練集，20%是測試集)
train_x,test_x,train_y,test_y=train_test_split(my_data.data,my_data.target,test_size=0.2,random_state=43,shuffle=True)

print("原始資料的維度大小:",my_data.data.shape)
print("訓練集的維度大小:",train_x.shape)
print("測試集的維度大小:",test_x.shape)

#訓練模型
my_model=LinearRegression()
my_model.fit(train_x,train_y)
#用訓練後的模型預測測試集
pred=my_model.predict(test_x)
#用MSE(mean_squared_error)評估模型的實際誤差
score=mean_squared_error(test_y,pred)
print("模型評估完測試集的MSE:",score)

train_x_f4=train_x[:,[4,5,6,7]]
test_x_f4=test_x[:,[4,5,6,7]]

#訓練模型
model_f4=LinearRegression()
model_f4.fit(train_x_f4,train_y)
#用訓練後的模型預測測試集
pred_f4=model_f4.predict(test_x_f4)
#用MSE(mean_squared_error)評估模型的實際誤差
score_f4=mean_squared_error(test_y,pred_f4)
print("模型評估完測試集的MSE:",score_f4)