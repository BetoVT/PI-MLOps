from fastapi import FastAPI

app = FastAPI()


@app.get("/inicio")
async def ruta_prueba():
    return "Hola"

@app.get("/inicio2")
async def ruta_prueba2():
    return "Adios"

@app.get("/PlayTimeGenre")
def playTimeGenre(genre):
    year = 0
    return year

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
