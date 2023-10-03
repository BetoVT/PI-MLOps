from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/PlayTimeGenre")
def playTimeGenre(genre):
    playTimeGenre = {'Action': [2012], 'Casual': [2015], 'Indie': [2006], 'Simulation': [2013], 'Free to Play': [2013], 'RPG': [2011], 'Sports': [2013], 'Adventure': [2011], 'Racing': [2016], 'Early Acess': [2013],
                 'Massively Multiplayer': [2013], 'Animation &amp; Modeling': [2013], 'Video Production': [2014], 'Utilities': [2014], 'Web Publishing': [2012], 'Education': [2013],
                 'Software Training': [2014], 'Design &amp; Illustration': [2014], 'Photo Editing': [2016], 'Accounting': [0]}
    return {"Año de lanzamiento con más horas jugadas para " + genre: playTimeGenre[genre][0]} 

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