import pandas as pd
import json
import os

if os.path.exists('Project\data\\processed\\steam_games.csv'):
    os.remove('Project\data\\processed\\steam_games.csv')

if os.path.exists('Project\data\\processed\\users_items.csv'):
    os.remove('Project\data\\processed\\users_items.csv')

if os.path.exists('Project\data\\processed\\users_reviews.csv'):
    os.remove('Project\data\\processed\\users_reviews.csv')

data = []

parameters = ('publisher', 'genres', 'app_name', 'title',
              'url', 'release_date', 'tags',
              'discount_price','reviews_url', 'specs',
              'price', 'early_access', 'id', 'developer',
              'sentiment', 'metascore')

data = []
data2 = []
data3 = []

f = open('Project\data\\raw\\output_steam_games.json', "r")
for i in range(120445):
    line = f.readline()
    if i < 88310:
        data2.append(json.loads(line))
        continue
    data.append(json.loads(line))
f.close

#f = open('Project\data\\raw\\australian_user_reviews.json', "r")
#for i in range(25799):
#    line = f.readline()
#    data3.append(json.dumps(line))
#f.close


df = pd.DataFrame.from_dict(data)
df = df.drop(columns=['user_id', 'steam_id', 'items', 'items_count'])
df.to_csv('Project\data\\processed\\steam_games.csv')

df2 = pd.DataFrame.from_dict(data2)
df2 = df2.drop(columns=['publisher', 'genres', 'app_name', 'title',
                    'url', 'release_date', 'tags', 'reviews_url',
                    'discount_price', 'specs',
                    'price', 'early_access', 'id', 'developer', 'metascore'])
df2.to_csv('Project\data\\processed\\users_items.csv')

#df3 = pd.DataFrame.from_dict(data3)
##df3.to_csv('Project\data\\processed\\users_reviews.csv')






##print(data[0]['publisher'])
#print(type(data[0]['publisher']))
#print(len(data[0]['publisher']))