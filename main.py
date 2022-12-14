import pandas as pd
import requests
import json

null=""

header={
    'user-agent':''
}

url = 'http://map.amap.com/service/subway?_1666854811181&srhdata=3201_drw_nanjing.json'
response = requests.get(url,headers=header)

json_str = response.text

json_dict = eval(json_str)

lList=json_dict['l']
data_set = []

for case in lList:
    data_dict = {}
    data_dict['ln']=case['ln']
    date_set=[]
    st=case['st']
    for case in st:
        date_dict={}
        # date_dict['n'] = case['n']
        date_set.append(case['n'])
    data_dict['st']=date_set
    data_set.append(data_dict)

df=pd.DataFrame(data_set)

df.to_csv('data1.csv')
