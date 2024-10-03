import requests
import pandas as pd
from collections import OrderedDict
from opencc import OpenCC
import re


#將簡體字換成繁體字
def convert_to_traditional(text):
    if isinstance(text, str):
        converter = OpenCC('s2t')
        return converter.convert(text)
    else:
        return text
    
#檢查是否包含中文字符
def contains_non_chinese(text):
    if isinstance(text, str):
        return not bool(re.search(r'^[\u4e00-\u9fff]+$', text))  
    else:
        return False
    
#劇名非中文則使用簡體中文介面查詢並將結果翻成繁體中文，若查詢不到則用英文劇名代替
def findname_by_CN(id):
    url = "https://api.themoviedb.org/3/tv/"+str(id)+"/translations"
    converter = OpenCC('s2t')
    response = requests.get(url, headers=headers)
    a=requests.get(url, headers=headers).json()['translations'][:-1]
    name_cn=df.loc[df['id'] == id, 'en_name']
    for item in a:
        if item['iso_3166_1'] == 'CN':
            name_cn = converter.convert(item['data']['name'])
            break
    return name_cn

#用api爬下資料做成DataFrame
def get_data(start_date,end_date,language):
    url="https://api.themoviedb.org/3/discover/tv?air_date.gte="+start_date+"&air_date.lte="+end_date+"&include_adult=false&include_null_first_air_dates=false&language="+language+"&sort_by=popularity.desc&vote_average.lte=10&watch_region=TW&with_runtime.gte=0&with_runtime.lte=400&with_watch_monetization_types=flatrate%7Cfree%7Cads%7Crent%7Cbuy&with_watch_providers=8%7C337%7C581%7C624%7C625&page=1"
    response = requests.get(url, headers=headers)
    a=response.json()
    data=pd.DataFrame(a['results'])
    for i in range(2,a['total_pages']+1):
        url="https://api.themoviedb.org/3/discover/tv?air_date.gte="+start_date+"&air_date.lte="+end_date+"&include_adult=false&include_null_first_air_dates=false&language="+language+"&sort_by=popularity.desc&vote_average.lte=10&watch_region=TW&with_runtime.gte=0&with_runtime.lte=400&with_watch_monetization_types=flatrate%7Cfree%7Cads%7Crent%7Cbuy&with_watch_providers=8%7C337%7C581%7C624%7C625&page="+str(i)
        response = requests.get(url, headers=headers)
        a=response.json()
        data = data.append(a['results'], ignore_index=True)
    return data

#TMDB API憑證
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZGNhZTBiYmVlOThiMDBiNDVhNDM5YjkzMGU1Y2Y5ZiIsInN1YiI6IjY1NTZlMjQwNjdiNjEzNDVjY2FmYTUxZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.srbDZlzVH-DvF9UaHDWHwqf_3_A1L3_pkIrN3f1apdA"
}

##需要改變的地方##
#設定起始日與終止日
start_date="2021-01-01"
end_date="2022-12-31"
#1為中文資料，2為英文資料
data=get_data(start_date,end_date,"zh-TW")
data2=get_data(start_date,end_date,"en-US")

non_chinese_rows = data[data['name'].apply(contains_non_chinese)]['id']


#只要英文資料中的劇名  
df=data2['name']
df=df.rename('en_name')
#刪除不需要的欄位
data = data.drop(data.columns[[0,1]], axis=1)
data = data.drop(data.columns[[4,5]], axis=1)
data = data.drop(data.columns[6], axis=1)
#結合英文劇名和篩選後的中文資料
df = pd.concat([data,df], axis=1)
current_order = df.columns.tolist()
new_order = ['id', 'name', 'en_name','origin_country','overview','genre_ids','popularity','vote_average','vote_count']
df = df[new_order]
c = df['genre_ids'].tolist()

#將類別編號轉換成中文
#先用api爬下類別編號相對中文再做成字典
gen_url = "https://api.themoviedb.org/3/genre/tv/list?language=zh-TW"
gen_json= requests.get(gen_url, headers=headers).json()
gen_data=pd.DataFrame(gen_json['genres'])
converter = OpenCC('s2t')
gen_data['name']=gen_data['name'].apply(convert_to_traditional)
gen_dict = gen_data.set_index('id')['name'].to_dict()
v=[]
z=[]
for a in df['genre_ids']:
    for i in a:
        i=gen_dict.get(i, i)
        v.append(i)
    z.append(v)
    v=[]
df['genre_ids'] = z

non_chinese_rows = (df[df['name'].apply(contains_non_chinese)]['id']).tolist()
chinese_rows=[i for i in df['id'] if i not in non_chinese_rows ] 

for i in non_chinese_rows:
    df.loc[df['id'] == i, 'name']=findname_by_CN(i)

df.loc[df['id'] == 229553, 'name']='向陽奔跑'
df.loc[df['id'] == 234409, 'name']='Around the World at Birth'
df.loc[df['id'] == 234409, 'en_name']='Around the World at Birth'
for index, row in df.iterrows():
    if row['name'] == "":
        df.at[index, 'name'] = row['en_name']
##df是真正要的資料
#存成csv下載
df.to_csv('All_data(21~22).csv', index=False) 
