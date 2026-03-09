from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    if connection.is_closed():
        connection.connect()
        print("Iniciando el servidor...")
    
    yield
    
    if not connection.is_closed():
        connection.close()
        print("Cerrando el servidor...")
    
app = FastAPI(title= "Proyecto FastAPI",
              description= "Proyecto de ejemplo con FastAPI",
              version= "1.0.0",
              lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"message": "Hola, bienvenido a mi proyecto FastAPI!"}

@app.get("/about")
async def read_about():
    return {"message": "Este es un proyecto de ejemplo usando FastAPI"}