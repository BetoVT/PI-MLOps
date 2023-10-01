import pandas as pd
import json
from warnings import simplefilter

PARAMS_ITEMS = ["{\'item_id': \'", "\', \'item_name\': \'",
                "\', \'playtime_forever\': \'", "\', \'playtime_2weeks\': \'",
                "\'}, {", "\'}]"]

PARAMS_ITEMS_ORIGINAL = ["\', 'playtime_forever': ",
                         ", \'playtime_2weeks\': ", "}, {", "}]"]

def search_item(s, i):
        
    return s

def count_items(s, count):
    lst = []
    for i in range(count):
        lst.append(search_item(s, i))
    return lst

def untangle_df(df, foreign_key):
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
    
    a = PARAMS_ITEMS_ORIGINAL
    b = PARAMS_ITEMS
    parameters = []
    for i in b:
        parameters.append(i.replace("\'", "\""))
    
    df['item_amount'] = df.apply(lambda row : count_items(row['items']), axis=1)


    #for i in df[foreign_key]:
    #    i = (i.replace(a[0], b[2])
    #          .replace(a[1], b[3])
    #          .replace(a[2], b[4])
    #          .replace(a[3], b[5]))
    #    #temp = json.loads(i)
    #    t.append(i)
    return df

def untangle_csv(primary_key, foreign_key):
    df = pd.read_csv('data\\processed\\users_items.csv',
                     encoding="UTF-8", index_col=0)
    df.drop_duplicates(inplace=True)
    df = untangle_df(df[[primary_key, foreign_key, 'items_count']].copy(), foreign_key)
    print(df)
    print(df['item_amount'].value_counts())
    print(df['item_amount'].sum())
    print(df['items_count'].value_counts())
    print(df['items_count'].sum())
    #print(df)
    #df.to_csv('data\\processed\\steam_games_' + foreign_key + '.csv')

untangle_csv('user_id', 'items')