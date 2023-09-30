import pandas as pd
import json
from warnings import simplefilter

def fill_empty_data(df):
    df.at[2580, 'app_name'] = "Duet"
    df.drop(df.index[74], inplace=True)
    return df

def untangle_df(df, foreign_key):
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
    attributes = []

    for i in df[foreign_key].unique():
        if isinstance(i, float):
            continue

        temp = json.loads(i.replace("[\'", "[\"")
                           .replace("\', ", "\", ")
                           .replace(", \'", ", \"")
                           .replace("\']", "\"]")
                           .replace("(", "")
                           .replace(")", ""))
        
        for j in temp:
            if j not in attributes:
                attributes.append(j)

    df[foreign_key].fillna('', inplace=True)
    df[attributes] = [False] * len(attributes)

    for i in attributes:
        df.loc[df[foreign_key].str.contains(i),i] = True
        #df.loc[df[foreign_key].str.match('|'.join(i))] = True
    df.drop(columns=foreign_key, inplace=True)
    return df

def untangle_csv(primary_key, foreign_key):
    df = pd.read_csv('data\\processed\\steam_games.csv',
                     encoding="UTF-8", index_col=0)
    df = fill_empty_data(df)
    df = untangle_df(df[[primary_key, foreign_key]].copy(), foreign_key)
    df.to_csv('data\\processed\\steam_games_' + foreign_key + '.csv')

untangle_csv('app_name', 'genres')
untangle_csv('app_name', 'tags')
untangle_csv('app_name', 'specs')