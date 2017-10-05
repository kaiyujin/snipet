# coding: utf-8
import pandas as pd
import re

df = pd.read_csv('items_shops_detail_tokyo_1.csv')
# 列追加
df['dinner_min_price'] = df['dinner_price']
df['dinner_max_price'] = df['dinner_price']
df['lunch_min_price'] = df['lunch_price']
df['lunch_max_price'] = df['lunch_price']

def clean_price(v, key_prefix):
    if v[key_prefix+'_price'][-1:] == '～':
        #max only
        v[key_prefix+'_price'] = re.sub('[￥～, ]','',v[key_prefix+'_price'])
        v[key_prefix+'_min_price'] = ''
        v[key_prefix+'_max_price'] = v[key_prefix+'_price']
    elif v[key_prefix+'_price'][1:2] == '～':
        #min only
        v[key_prefix+'_price'] = re.sub('[￥～, ]','',v[key_prefix+'_price'])
        v[key_prefix+'_min_price'] = v[key_prefix+'_price']
        v[key_prefix+'_max_price'] = ''
    elif v[key_prefix+'_price'].find('～') > 0:
        v[key_prefix+'_price'] = re.sub('[￥, ]','',v[key_prefix+'_price'])
        min_max = v[key_prefix+'_price'].split('～')
        v[key_prefix+'_min_price'] = min_max[0]
        v[key_prefix+'_max_price'] = min_max[1]


# データクリーニング
for i, v in df.iterrows():

    if pd.isnull(v['sheats']):
        v['sheats']  = 0
    else:
        v['sheats']  = v['sheats'].replace('席','')

    if v['point'] == '-':
        v['point'] = 0
    else:
        v['point'] = float(v['point'])

    clean_price(v, 'lunch')
    clean_price(v, 'dinner')

high = df.query('point >= 3.5 & resevation == "予約可"')
high.to_csv('high.csv')
