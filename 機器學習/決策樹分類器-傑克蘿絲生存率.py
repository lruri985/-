from sklearn import tree
import numpy as np
import pandas as pd

data_ori=pd.read_csv("C:/Users/lruri/Dropbox/PC/Desktop/練習/Python/傑克蘿絲生存率資料集/train.csv")
data=data_ori.loc[:,['Sex','Age','Fare','Survived']]
#把male,female轉換成0,1
data.loc[data['Sex']=='male','Sex']=0
data.loc[data['Sex']=='female','Sex']=1

#有存活下的人
data_sur=data[data['Survived']==1]
#有存活且為男性
df_male=data_sur[data_sur['Sex']==0]
#有存活且為女性
df_female=data_sur[data_sur['Sex']==1]
#柱狀圖分析(男女)
df=pd.DataFrame({'Sex':['male','female'],'val':[len(df_male),len(df_female)]})
ax=df.plot.bar(x='Sex',y='val',rot=0)

#有存活且小於30歲
df_young=data_sur[data_sur['Age']<30]
#有存活且大於30歲
df_older=data_sur[data_sur['Age']>30]
#柱狀圖分析(老少)
df=pd.DataFrame({'Age':['young','older'],'val':[len(df_young),len(df_older)]})
ax=df.plot.bar(x='Age',y='val',rot=0)

#決策樹分類器
data_tree=data_ori.drop(columns=['Name','Ticket','Cabin'])

#轉換欄位(Embarked)
typeEmbarked=list(set(data_tree['Embarked']))
#把欄位文字按順序轉換成0~n數字
for i in range(len(typeEmbarked)):
    print(typeEmbarked[i])
    rows=data_tree['Embarked']==typeEmbarked[i]
    data_tree.loc[rows,'Embarked']=i
    
#轉換欄位(Sex)
typeSex=list(set(data_tree['Sex']))
#把欄位文字按順序轉換成0~n數字
for i in range(len(typeSex)):
    print(typeSex[i])
    rows=data_tree['Sex']==typeSex[i]
    data_tree.loc[rows,'Sex']=i
    
#用999補NA值，因為決策樹對離群值不敏感
data_tree=data_tree.fillna(999)

#切割:訓練(前750)測試(750後)
x_train=data_tree[:750]
x_test=data_tree[750:]
y_train=x_train.pop('Survived')#x_train會刪掉survived

#建立模型
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)

#驗證模型
from sklearn.metrics import accuracy_score,recall_score

y_test=x_test.pop('Survived')
y_pred=clf.predict(x_test)
#正確率:每一次預測的準確度
print('accuracy_score',accuracy_score(y_test,y_pred))
#召回率:是否能找出資料及中存活的樣本
print('recall_score',recall_score(y_test,y_pred))