# coding: utf-8
import pandas as pd
import re

df = pd.read_csv('items_shops_detail_tokyo_1.csv')
# データクリーニング
for i, v in df.iterrows():
    if v['lunch_price'] == 'null':
       v['lunch_price']  = ''

    if pd.isnull(v['sheats']):
        v['sheats']  = 0
    else:
        v['sheats']  = v['sheats'].replace('席','')

    if v['point'] == '-':
        v['point'] = 0
    else:
        v['point'] = float(v['point'])

    if v['dinner_price'][-1:] == '～':
        #max only
        v['dinner_price'] = re.sub('[￥～, ]','',v['dinner_price'])
        print(v['dinner_price'])
    elif v['dinner_price'][1:2] == '～':
        #min only
        v['dinner_price'] = re.sub('[￥～, ]','',v['dinner_price'])
        print(v['dinner_price'])
    elif v['dinner_price'].find('～') > 0:
        v['dinner_price'] = re.sub('[￥, ]','',v['dinner_price'])
        min_max = v['dinner_price'].split('～')
        print(str(min_max))

#食べログ
#high = df.query('point >= 4 & resevation == "予約可"')
#high.to_csv('high.csv')
