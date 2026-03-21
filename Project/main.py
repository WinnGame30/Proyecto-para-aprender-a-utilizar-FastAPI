from fastapi import FastAPI
from fastapi import HTTPException

from contextlib import asynccontextmanager

from database import database as connection
from database import User, Videojuego, UserReview

from schemas import UserRequestModel, ReseñaRequestModel
from schemas import UserResponseModel, ReseñaResponseModel

from typing import List

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

@app.post("/users", response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).exists():
        raise HTTPException(status_code=409, detail="El username ya existe")

    hash_password = User.create_password(user.password)

    user = User.create(username = user.username,
                       password = hash_password)
    
    return user

@app.post("/reseñas_videojuegos", response_model=ReseñaResponseModel)
async def create_review(reseña: ReseñaRequestModel):

    if User.select().where(User.id == reseña.id_usuario).first() is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if Videojuego.select().where(Videojuego.id == reseña.id_videojuego).first() is None:
        raise HTTPException(status_code=404, detail="El videojuego no existe")

    reseña = UserReview.create(user_id = reseña.id_usuario,
                               videojuego_id = reseña.id_videojuego,
                               review = reseña.review,
                               score = reseña.score)
    
    return reseña

@app.get("/listado_reseñas", response_model=List[ReseñaResponseModel])
async def listado_reseñas():
    reseñas = UserReview.select()
    return reseñas

@app.get("/listado_reseñas/{id}", response_model=ReseñaResponseModel)
async def reseña_particular(id: int):
    reseña = UserReview.select().where(UserReview.id == id).first()

    if reseña is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    return reseña