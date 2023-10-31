import pandas as pd

def get_developer(primary_key):
    games = pd.read_csv('data\\final\\steam_games_flat.csv', encoding="UTF-8",
                        usecols=[primary_key, 'developer', 'year', 'price'])
    games.dropna(inplace=True)
    games.reset_index(drop=True, inplace=True)
    games.set_index(['developer', 'year'], inplace=True)
    games.to_csv('data\\output\\developer.csv')

    """ cond = ((dev == developer) & (year == float(i)))
        slice = games[cond]
        if not slice.empty:
            total_items = slice['app_name'].count()
            free_items = slice['app_name'].loc[slice['price'] == 0.0].count()
            free_items = str(float((free_items / total_items * 100))) + '%'
            iter_dict = {"Año": i,
                         "Cantidad de items": total_items,
                         "Contenido Free": free_items}
            devList.append(iter_dict)
"""

def get_userdata(primary_key):
    games = pd.read_csv('data\\final\\steam_games_flat.csv', encoding="UTF-8",
                        usecols=['id', 'price'], dtype={'id': 'string'})
    users = pd.read_csv('data\\final\\users_items_flat.csv', encoding="UTF-8",
                        usecols=[primary_key, 'item_id'],
                        index_col=[primary_key], dtype={'item_id': 'string'})
    revws = pd.read_csv('data\\final\\user_reviews_flat.csv', encoding="UTF-8",
                        usecols=[primary_key, 'item_id', 'recommend'],
                        index_col=[primary_key], dtype={'item_id': 'string'})
    games.dropna(inplace=True)
    users.dropna(inplace=True)
    revws.dropna(inplace=True)
    userlist = users.index.unique().to_series().to_list()
    lst = []
    cont = 0
    ttl = len(userlist)
    checkpoint = 100
    for i in userlist:
        usergames = users[users.index == i]
        usergames = usergames['item_id'].tolist()
        userrevws = revws[revws.index == i]
        user_recommended = userrevws['recommend'].loc[userrevws['recommend'] == True].count()
        total = 0
        for j in usergames:
            gameprice = games['price'].loc[games['id'] == j]
            if gameprice.empty:
                continue
            total = total + gameprice.values[0]
        total = round(total, 2)
        rec_percent = str(round(user_recommended / len(usergames) * 100)) + "%"
        iter_dict = {"Usuario X": i,
                     "Dinero gastado": (str(total) + ' USD'),
                     "% de recomendación": rec_percent,
                     "cantidad de items": len(usergames)}
        lst.append(iter_dict)

        cont = cont + 1
        if cont == checkpoint:
            print("Checked", cont, "users out of", ttl)
            checkpoint = checkpoint + 100
    df = pd.DataFrame.from_dict(lst)
    print(df)
    games.to_csv('data\\output\\userdata.csv')



get_developer('app_name')
get_userdata('user_id')