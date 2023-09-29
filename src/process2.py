import pandas as pd
import numpy as np
import json

df = pd.read_csv('Project\data\\processed\\steam_games.csv', encoding="UTF-8", index_col=0)
df.at[2580, 'app_name'] = "Duet"
df.drop(df.index[74], inplace=True)

df2 = df[['app_name', 'genres']].copy()

genres = []

for i in df2.genres.unique():
    if isinstance(i, float):
        continue
    temp = json.loads(i.replace("\'", "\""))
    for j in temp:
        if j not in genres:
            genres.append(j)

for i in genres:
    df[i] = False

df2.genres.fillna('', inplace=True)

for i in genres:
    df2.loc[df2['genres'].str.contains(i),i] = True

df2.drop(columns='genres', inplace=True)
df2.to_csv('Project\data\\processed\\steam_games_genres.csv')