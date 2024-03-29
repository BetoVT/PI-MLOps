import pandas as pd

def get_playTimeGenre(primary_key):    
    games = pd.read_csv('data\\final\\steam_games_genres.csv',
                        encoding="UTF-8", index_col=0)
    dates = pd.read_csv('data\\final\\steam_games_flat.csv',
                        encoding="UTF-8", usecols=['year'])
    users = pd.read_csv('data\\final\\users_items_flat.csv',
                        encoding="UTF-8", index_col=0)

    print(games)
    print(dates)

    games = pd.concat([games, dates], axis=1)
    games.dropna(subset=['year'], inplace=True)
    games.reset_index(drop=True, inplace=True)

    print(games)

    years = []
    playTimeGenre = {}
    genres = games.drop(columns=[primary_key, 'year']).columns.values.tolist()
    genre_games = []
    for i in range(1970, 2022, 1):
        years.append(i)

    for i in genres:
        playTimeGenre.update({i: 0})
        max_playtime = 0
        for j in years:
            temp = 0
            genre_games = games[primary_key].loc[(games[i] == True) & (games['year'] == j)].tolist()
            #print("Searching for games with genre", i, "released at year", j)
            for k in genre_games:
                temp = temp + users['playtime_forever'].loc[users['item_name'] == k].sum()
            if temp > max_playtime:
                #print("New max playtime for genre", i, "is", temp, "at year", j)
                playTimeGenre.update({i: [j]})
                #print("New dict: ", playTimeGenre)
                max_playtime = temp
                temp = 0


    df = pd.DataFrame.from_dict(playTimeGenre)

    df.to_csv('data\\output\\playTimeGenre.csv')

def get_userForGenre(primary_key):    
    games = pd.read_csv('data\\final\\steam_games_genres.csv',
                        encoding="UTF-8", index_col=0)
    dates = pd.read_csv('data\\final\\steam_games_flat.csv',
                        encoding="UTF-8", usecols=['year'])
    users = pd.read_csv('data\\final\\users_items_flat.csv',
                        encoding="UTF-8", index_col=[1, 0])

    games = pd.concat([games, dates], axis=1)
    games.dropna(subset=['year'], inplace=True)
    games.reset_index(drop=True, inplace=True)

    #print(users)

    years = []
    userForGenre = []
    genres = games.drop(columns=[primary_key, 'year']).columns.values.tolist()
    #userlist = users['user_id'].unique().tolist()
    #print(users.index.values.tolist())
    genre_games = []
    for user, userGames in users.groupby(level=0):
        #print(userGames.droplevel(0))
        max = 0
    """
    for i in range(1970, 2022, 1):
        years.append(i)

    for i in userlist:
        max_playtime = 0
        for j in genres:
            genre_games = games[primary_key].loc[(games[j] == True)].tolist()
            temp = 0
            print("Checando genero", j, "para usuario", i)
            for k in genre_games:
                if len(users['playtime_forever'].loc[(users['item_name'] == k) & (users['user_id'] == i)].values) == 1:
                    print("El usuario ha jugado", k, users['playtime_forever'].loc[(users['item_name'] == k) & (users['user_id'] == i)].values[0], "horas")
                    temp = temp + users['playtime_forever'].loc[(users['item_name'] == k) & (users['user_id'] == i)].values[0]
            if temp > max_playtime:
                print("El usuario", i, "tiene el mayor tiempo de juego en el genero", j, "con", max_playtime, "horas jugadas.")
                max_playtime = temp
                temp = 0

    for i in genres:
        max_playtime = 0
        genre_games = games[primary_key].loc[(games[i] == True)].tolist()
        max_user = {}
        temp = 0
        for j in genre_games:
            temp = temp + users['playtime_forever'].loc[users['item_name'] == j].sum()
        if temp > max_playtime:
            for k in years:
                genre_games = games[primary_key].loc[(games[i] == True) & (games['year'] == j)].tolist()
                max_user.update({i: j})
            print("New max playtime for genre", i, "is", temp, "at year", j)
            max_playtime = temp
            userForGenre.append(max_user)
            temp = 0
    """


    df = pd.DataFrame.from_dict(userForGenre)

    df.to_csv('data\\output\\userForGenre.csv')

#get_playTimeGenre('app_name')
get_userForGenre('app_name')