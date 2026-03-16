from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import database as connection
from database import User, Videojuego, UserReview

from schemas import UserBaseModel

@asynccontextmanager
async def lifespan(_: FastAPI):
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User, Videojuego, UserReview])

    yield
    
    if not connection.is_closed():
        connection.close()

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

@app.post("/users/")
async def create_user(user: UserBaseModel):
    user = User.create(username = user.username, password = user.password)
    return {user.id}