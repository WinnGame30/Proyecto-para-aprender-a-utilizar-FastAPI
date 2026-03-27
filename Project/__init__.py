from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Depends

from contextlib import asynccontextmanager

from .database import database as connection
from .database import User, Videojuego, UserReview

from .Routers import user_router, review_router

from fastapi.security import OAuth2PasswordRequestForm

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
              version= "1.0.1",
              lifespan=lifespan)

api_v1 = APIRouter(prefix="/api/v1")

api_v1.include_router(user_router)
api_v1.include_router(review_router)

@api_v1.post("/auth")
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    return {
        "username" : data.username,
        "password" : data.password
        }
    

app.include_router(api_v1)

@api_v1.get("/about")
async def read_about():
    return {"message": "Este es un proyecto de ejemplo usando FastAPI"}

