import pandas as pd
import json
from warnings import simplefilter

PARAMS_ITEMS = ["{\'item_id': \'", "\', \'item_name\': \'",
                "\', \'playtime_forever\': \'", "\', \'playtime_2weeks\': \'",
                "\'}, {", "\'}]"]

PARAMS_ITEMS_ORIGINAL = ["\', 'playtime_forever': ",
                         ", \'playtime_2weeks\': ", "}, {", "}]"]

def fixStr_user_reviews(line):
    a = PARAMS_ITEMS_ORIGINAL
    b = PARAMS_ITEMS
    for i in range(len(a)):
        line = line.replace(a[i], b[i + 2].replace("\'", "\""))
    for i in range(len(b)):
        line = line.replace(b[i], b[i].replace("\'", "\""))
    return line

def search_item(s, past_length):
    str_strt = s.find("{\"item_id\": \"", past_length)
    str_end = s.find("\"}", past_length) + 2
    s = s[str_strt:str_end]
    #print(s)
    return s

def add_items(s, count):
    s = fixStr_user_reviews(s)
    lst = []
    past_length = 0
    for i in range(count):
        new_item = search_item(s, past_length)
        lst.append(json.loads(new_item))
        #print("Saved length: ", past_length)
        past_length = past_length + len(new_item) + 2
    return lst

#print(add_items(test, test_count))

def untangle_df(df, foreign_key):
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
    items = []
    for i in range(df.shape[0]):
        s = df.at[i, 'items']
        count = df.at[i, 'items_count']
        #print("count is: ", count)
        #print("line is: ", i + 1)
        #print("string is: ", s)
        items = items + add_items(s, count)
    
    return items

def untangle_csv(primary_key, foreign_key):
    df = pd.read_csv('data\\processed\\users_items.csv',
                     encoding="UTF-8", index_col=0)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    df2 = pd.DataFrame.from_dict(untangle_df(df[[primary_key, foreign_key, 'items_count']].copy(), foreign_key))
    print(df2)
    df2.to_csv('data\\processed\\user_' + foreign_key + '_flat.csv')

untangle_csv('user_id', 'items')