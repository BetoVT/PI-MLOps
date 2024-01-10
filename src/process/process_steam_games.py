import pandas as pd
import numpy as np
import json
from warnings import simplefilter

def fix_date(s):
    found_date = False
    for i in range(1969, 2022, 1):
        if str(i) in str(s):
            s = int(i)
            found_date = True
    
    if not found_date:
        s = np.nan
        
    return s

def fix_price(s):
    free_conditions = ['Free', 'Free to Play', 'Free To Play',
                       'Play for Free!', 'Install Now', 'Play Now',
                       'Free to Try', 'Free Movie', 'Free to Use']
    
    unambiguos_contitions = ['Play WARMACHINE: Tactics Demo', 'Third-party',
                             'Free Demo', 'Free Mod', 'Install Theme',
                             'Free HITMAN™ Holiday Pack', 'Play the Demo',
                             'Free to Try']


    if s == 'Starting at $449.00':
        return float(449)
    elif s == 'Starting at $499.00':
        return float(499)
    elif s in free_conditions:
        return float(0)
    elif s in unambiguos_contitions:
        return np.nan
    elif s != '':
        return float(s)
        
    return np.nan

def fill_empty_data(df):
    #Possible to fill data with web-scraping
    #Filling manually for now
    df.at[2580, 'app_name'] = "Duet"
    df.drop(df.index[74], inplace=True)
    df.reset_index(drop=True, inplace=True)
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
    df.drop(columns=foreign_key, inplace=True)
    return df

def untangle_csv(primary_key, foreign_key):
    df = pd.read_csv('data\\processed\\steam_games.csv',
                     encoding="UTF-8", index_col=0)
    df = fill_empty_data(df)
    df = untangle_df(df[[primary_key, foreign_key]].copy(), foreign_key)
    df.to_csv('data\\final\\steam_games_' + foreign_key + '.csv')

def untangle_main():
    df = pd.read_csv('data\\processed\\steam_games.csv',
                     encoding="UTF-8", index_col=0, dtype={'id': 'string'})
    df = fill_empty_data(df)
    df['year'] = df.apply(lambda row : fix_date(row['release_date']), axis = 1)
    df['price'] = df.apply(lambda row : fix_price(row['price']), axis = 1)
    df.drop(columns=['genres', 'url', 'tags' ,'reviews_url',
                     'title', 'specs', 'early_access',
                     'release_date'], inplace = True)
    df.to_csv('data\\final\\steam_games_flat.csv')


untangle_csv('app_name', 'genres')
untangle_csv('app_name', 'tags')
untangle_csv('app_name', 'specs')
untangle_main()