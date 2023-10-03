import pandas as pd

def get_playTimeGenre(primary_key):    
    games = pd.read_csv('data\\final\\steam_games_genres.csv',
                        encoding="UTF-8", index_col=0)
    dates = pd.read_csv('data\\final\\steam_games.csv',
                        encoding="UTF-8", usecols=['year'])
    users = pd.read_csv('data\\processed\\users_items_flat.csv',
                        encoding="UTF-8", index_col=0)
    
    print(games)
    print(dates)

    games = pd.concat([games, dates], axis=1)
    games.dropna(subset=['year'], inplace=True)
    games.reset_index(drop=True, inplace=True)
    
    print(games)

    years = []
    playTimeGenre = {}
    genres = games.drop(columns=primary_key).columns.values.tolist()
    genre_games = []
    for i in range(1970, 2022, 1):
        years.append(i)

    for i in genres:
        playTimeGenre.update({i: 0})
        max_playtime = 0
        for j in years:
            temp = 0
            genre_games = games[primary_key].loc[(games[i] == True) & (games['year'] == j)].tolist()
            print("Searching for games with genre", i, "released at year", j)
            for k in genre_games:
                temp = temp + users['playtime_forever'].loc[users['item_name'] == k].sum()
            if temp > max_playtime:
                print("New max playtime for genre", i, "is", temp, "at year", j)
                playTimeGenre.update({i: j})
                print("New dict: ", playTimeGenre)
                max_playtime = temp
                temp = 0

    print(playTimeGenre)


    #for i in attributes:
    #    df.loc[df[foreign_key].str.contains(i),i] = True
    #df.drop(columns=foreign_key, inplace=True)
    #for i in users:

get_playTimeGenre('app_name')