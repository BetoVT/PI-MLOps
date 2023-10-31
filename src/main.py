from fastapi import FastAPI
import functions as f

app = FastAPI()

@app.get("/developer")
def developerAPI(developer):
    return f.developerAPI(developer)

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