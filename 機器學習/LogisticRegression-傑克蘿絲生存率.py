import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

titanic_train=pd.read_csv("C:/Users/lruri/Dropbox/PC/Desktop/練習/Python/傑克蘿絲生存率資料集/train.csv")
titanic_test=pd.read_csv("C:/Users/lruri/Dropbox/PC/Desktop/練習/Python/傑克蘿絲生存率資料集/test.csv")
print(f'訓練資料的筆數與特徵值數目:{titanic_train.shape}')
print(f'測試資料的筆數與特徵值數目:{titanic_test.shape}')
#前後五筆資料
titanic_train.head()
titanic_test.head()

#處理缺失值
#統計缺失值
print(titanic_train.isna().sum())
print("----")
print(titanic_test.isna().sum())
#用平均值補上Age
titanic_train.Age.fillna(titanic_train.Age.mean(),inplace=True)
titanic_test.Age.fillna(titanic_test.Age.mean(),inplace=True)
#刪掉Cabin，因為缺失值太多
titanic_train.drop(columns='Cabin',inplace=True)
titanic_test.drop(columns='Cabin',inplace=True)
#用眾數補Embarked，因為只缺失兩筆
titanic_train.Embarked.fillna(titanic_train.Embarked.mode()[0],inplace=True)
titanic_test.Embarked.fillna(titanic_test.Embarked.mode()[0],inplace=True)
#用平均補Fare
titanic_test.Fare.fillna(titanic_test.Fare.mean(),inplace=True)
#檢查缺失值
print(titanic_train.isna().sum())
print("----")
print(titanic_test.isna().sum())

#轉換資料型態
print(titanic_train.dtypes)
#刪掉Name和Ticket，因為是不重複字串無法直觀轉換
titanic_train.drop(columns=['Name','Ticket'],inplace=True)
titanic_test.drop(columns=['Name','Ticket'],inplace=True)
#用sklearn的LabelEncoder做label encoding(標籤編碼)
le=LabelEncoder()
titanic_train.Sex=le.fit_transform(titanic_train.Sex)
titanic_test.Sex=le.fit_transform(titanic_test.Sex)

titanic_train.Embarked=le.fit_transform(titanic_train.Embarked)
titanic_test.Embarked=le.fit_transform(titanic_test.Embarked)
#檢查資料型態
print(titanic_train.dtypes)
print('----')
print(titanic_test.dtypes)

#準備訓練集和測試集
#刪掉PassengerId(無意義)和Survived(預測目標)
train_x=titanic_train.drop(columns=['PassengerId','Survived'])
train_y=titanic_train['Survived']
test_x=titanic_test.drop(columns=['PassengerId'])

#建立模型
from sklearn.linear_model import LogisticRegression
estimator=LogisticRegression()
estimator.fit(train_x,train_y)

pred=estimator.predict(test_x)
submit=pd.DataFrame({'PassengerId':titanic_test.PassengerId,'Survived':pred})

#結果存成csv
submit.to_csv('titanic_baseline.csv',index=False)