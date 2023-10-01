import pandas as pd
import json
from warnings import simplefilter

def fill_empty_data(df):
    
    #print(df['user_id'].isna().sum())
    #print(df['steam_id'].isna().sum())
    #print(df['user_id'].unique().size)
    #print(df['steam_id'].unique().size)

    #print(df['user_id'].value_counts())
    #print(df['steam_id'].value_counts())

    df2 = df.duplicated(subset=['user_id'], keep=False)
    df3 = df.duplicated(subset=['steam_id'], keep=False)
    df4 = df.duplicated(subset=['user_id', 'steam_id'], keep=False)

    df2 = df[df2].sort_values('user_id')
    df3 = df[df3].sort_values('steam_id')
    df5 = df[df4].sort_values('user_id')
    df6 = df[df4].sort_values('steam_id')


    df2.to_csv('data\\processed\\users_items_flat_test2.csv')
    df3.to_csv('data\\processed\\users_items_flat_test3.csv')
    #df[df4].to_csv('data\\processed\\users_items_flat_test4.csv')
    df5.to_csv('data\\processed\\users_items_flat_test5.csv')
    df6.to_csv('data\\processed\\users_items_flat_test6.csv')

    #print(df)

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
    df = pd.read_csv('data\\processed\\users_items.csv',
                     encoding="UTF-8", index_col=0)
    df.drop_duplicates(inplace=True)
    df = fill_empty_data(df)
    #df = untangle_df(df[[primary_key, foreign_key]].copy(), foreign_key)
    #df.to_csv('data\\processed\\steam_games_' + foreign_key + '.csv')

untangle_csv('app_name', 'genres')
#untangle_csv('app_name', 'tags')
#untangle_csv('app_name', 'specs')