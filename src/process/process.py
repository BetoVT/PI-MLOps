import pandas as pd
import json
import os

PARAMS_USERS_ITEMS = ["{\'user_id\': \'", "\', \'items_count\': \'",
                      "\', \'steam_id\': \'", "\', \'user_url\': \'",
                      "\', \'items\': \'[", "}]\'}"]

PARAMS_USER_REVIEWS = ["{\'user_id\': \'", "\', \'user_url\': \'",
                       "\', \'reviews\': \'[", "}]\'}"]


def fixStr_users_items(line):
    line = line.replace("items_count\': ", "items_count\': \'")
    line = line.replace(", \'steam_id\'", "\', \'steam_id\'")
    line = line.replace("\'items\': [", "\'items\': \'[")
    line = line.replace("]}", "]\'}")
    return line

def fixStr_user_reviews(line):
    line = line.replace("\', \'reviews\': [", "\', \'reviews\': \'[")
    line = line.replace("\', \'reviews\': []", "\', \'reviews\': \'[]\'")
    line = line.replace("}]}", "}]\'}")
    return line

def fixJson(line, parameters):
    line = (line.replace("\\", "")
                .replace("\"", "\'"))
    for p in parameters:
        line = line.replace(p, p.replace("\'", "\""))
    return line


if os.path.exists('data\\processed\\steam_games.csv'):
    os.remove('data\\processed\\steam_games.csv')

if os.path.exists('data\\processed\\users_items.csv'):
    os.remove('data\\processed\\users_items.csv')

if os.path.exists('data\\processed\\user_reviews.csv'):
    os.remove('data\\processed\\user_reviews.csv')

steam_games = []
users_items = []
user_reviews = []

f = open('data\\raw\\output_steam_games.json', "r", encoding="UTF-8")
f2 = open('data\\raw\\australian_users_items.json', "r", encoding="UTF-8")
for i in range(88310):
    dump = f.readline()
    line = f2.readline()
    if "\'items\': []" in line: continue
    new_item = fixJson(fixStr_users_items(line), PARAMS_USERS_ITEMS)
    users_items.append(json.loads(new_item))
for i in range(32135):
    line = f.readline()
    steam_games.append(json.loads(line))
f.close
f2.close

f = open('data\\raw\\australian_user_reviews.json', "r", encoding="UTF-8")
for i in range(24999):
    line = f.readline()
    if "\', \'reviews\': []" in line: continue
    new_item = fixJson(fixStr_user_reviews(line), PARAMS_USER_REVIEWS)
    user_reviews.append(json.loads(new_item))
f.close


df = pd.DataFrame.from_dict(steam_games)
df2 = pd.DataFrame.from_dict(users_items)
df3 = pd.DataFrame.from_dict(user_reviews)

df.to_csv('data\\processed\\steam_games.csv')
df2.to_csv('data\\processed\\users_items.csv')
df3.to_csv('data\\processed\\user_reviews.csv')