from fastapi import FastAPI

app = FastAPI(title= "Proyecto FastAPI",
              description= "Proyecto de ejemplo con FastAPI",
              version= "1.0.0")

@app.get("/")
async def read_root():
    return {"message": "Hola, bienvenido a mi proyecto FastAPI!"}

@app.get("/about")
async def read_about():
    return {"message": "Este es un proyecto de ejemplo usando FastAPI"}