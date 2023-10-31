import pandas as pd

def developerAPI(developer):
    games = pd.read_csv('data\\output\\developer.csv', encoding="UTF-8",
                        usecols=['app_name', 'developer', 'year', 'price'],
                        index_col=['developer', 'year'])
    dev = games.index.get_level_values(0)
    year = games.index.get_level_values(1)
    devList = []
    for i in range(2022, 1970, -1):
        cond = ((dev == developer) & (year == float(i)))
        slice = games[cond]
        if not slice.empty:
            total_items = slice['app_name'].count()
            free_items = slice['app_name'].loc[slice['price'] == 0.0].count()
            free_items = str(float((free_items / total_items * 100))) + '%'
            iter_dict = {"Año": i,
                         "Cantidad de items": total_items,
                         "Contenido Free": free_items}
            devList.append(iter_dict)

    return devList

def userdataAPI(User_id):
    users = pd.read_csv('data\\output\\userdata.csv', encoding="UTF-8")
    output = {"Usuario X": users.at[0, 'Usuario X'],
              "Dinero gastado": users.at[1, 'Dinero gastado'],
              "% de recomendación": users.at[2, '% de recomendación'],
              "Cantidad de items": users.at[3, 'Cantidad de items']}
    return output

def UserForGenreAPI(genre):
    output = {}
    return output

def best_developer_yearAPI(year):
    output = {}
    return output

def developer_revies_analysisAPI(developer):
    output = {}
    return output

user='doctr'

print(userdataAPI(user))