from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/PlayTimeGenre")
def playTimeGenre(genre):
    df = pd.read_csv('data\\final\\playTimeGenre.csv')
    d = df.to_dict()
    return {"Año de lanzamiento con más horas jugadas para " + genre: d[genre][0]} 

@app.get("/UserForGenre")
def userForGenre(genre):
    user = 1.1
    yearList = 1.2
    return user, yearList

@app.get("/UsersRecommend")
def usersRecommend(year):
    gameList = 2
    return gameList

@app.get("/UsersNotRecommend")
def usersNotRecommend(genre):
    gameList = 3
    return gameList

@app.get("/SentimentAnalysis")
def sentimentAnalysis(entName):
    reviews = 4
    return reviews

print(playTimeGenre('Action'))