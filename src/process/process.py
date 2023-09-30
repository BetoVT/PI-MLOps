import pandas as pd
import json
import os

parameters = ["\'user_id\': \'", "\', \'user_url\': \'",
              "\', \'reviews\':", "\'funny\': \'", "\'}, {",
              "\', \'posted\': \'", "\', \'last_edited\': \'",
              "\', \'item_id\': \'", "\', \'helpful\': \'",
              "\', \'recommend\': ", ", \'review\': \'", "\'}]}"]

def fixJson(s):
    line = s
    line = (line.replace("\\", "")
                .replace("\"", "\'")
                .replace(": True", ": \"True\"")
                .replace(": False", ": \"False\""))
    for i in parameters:
        line = line.replace(i, i.replace("\'", "\""))
    return line

if os.path.exists('Project\data\\processed\\steam_games.csv'):
    os.remove('Project\data\\processed\\steam_games.csv')

if os.path.exists('Project\data\\processed\\users_items.csv'):
    os.remove('Project\data\\processed\\users_items.csv')

if os.path.exists('Project\data\\processed\\users_reviews.csv'):
    os.remove('Project\data\\processed\\users_reviews.csv')

steam_games = []
users_items = []
users_reviews = []

f = open('data\\raw\\output_steam_games.json', "r", encoding="UTF-8")
for i in range(88310):
    line = f.readline()
    users_items.append(json.loads(line))
for i in range(32135):
    line = f.readline()
    steam_games.append(json.loads(line))
f.close

f = open('data\\raw\\australian_user_reviews.json', "r", encoding="UTF-8")
for i in range(24999):
    line = f.readline()
    users_reviews.append(json.loads(fixJson(line)))
f.close


df = pd.DataFrame.from_dict(steam_games)
df2 = pd.DataFrame.from_dict(users_items)
df3 = pd.DataFrame.from_dict(users_reviews)

df = df.drop(columns=['title', 'user_id', 'steam_id', 'items', 'items_count'])
df2 = df2.drop(columns=['publisher', 'genres', 'app_name', 'title',
                        'url', 'release_date', 'tags', 'reviews_url',
                        'discount_price', 'specs', 'price', 'early_access',
                        'id', 'developer', 'metascore', ''])

df.to_csv('data\\processed\\steam_games.csv')
df2.to_csv('data\\processed\\users_items.csv')
df3.to_csv('data\\processed\\users_reviews.csv')