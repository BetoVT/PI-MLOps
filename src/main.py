from fastapi import FastAPI
import functions

app = FastAPI()


@app.get("/inicio")
async def ruta_prueba():
    return "Hola"