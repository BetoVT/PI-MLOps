import pandas as pd
import json

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
    return s

def add_items(s, count, primary_key):
    s = fixStr_user_reviews(s)
    lst = []
    past_length = 0
    user_id = {'user_id': primary_key}
    for i in range(count):
        new_item = search_item(s, past_length)
        item_to_append = {**user_id, **json.loads(new_item)}
        past_length = past_length + len(new_item) + 2
        if item_to_append['playtime_forever'] == '0':
            continue
        else:
            lst.append(item_to_append)
    return lst

def untangle_df(df, primary_key):
    items = []
    for i in range(df.shape[0]):
        s = df.at[i, 'items']
        count = df.at[i, 'items_count']
        new_items = add_items(s, count, df.at[i, primary_key])
        items.extend(new_items)
    new_df = pd.DataFrame.from_dict(items)
    return new_df

def untangle_csv(primary_key):
    df = pd.read_csv('data\\processed\\users_items.csv',
                     encoding="UTF-8", index_col=0)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    df2 = untangle_df(df[[primary_key, 'items', 'items_count']].copy(),
                      primary_key)
    df2.to_csv('data\\processed\\user_items_flat.csv')

untangle_csv('user_id')