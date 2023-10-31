from fastapi import FastAPI
import pandas as pd
import functions as f

def developerAPI_f(developer):
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

app = FastAPI()

@app.get("/developer")
def developerAPI(developer):
    return developerAPI_f(developer)

@app.get("/userdata")
def userdataAPI(User_id):
    output = {}
    return output

@app.get("/UserForGenre")
def UserForGenreAPI(genre):
    output = {}
    return output

@app.get("/best_developer_year")
def best_developer_yearAPI(year):
    output = {}
    return output

@app.get("/developer_revies_analysis")
def developer_revies_analysisAPI(developer):
    output = {}
    return output