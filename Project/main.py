from fastapi import FastAPI
from fastapi import HTTPException

from contextlib import asynccontextmanager

from database import database as connection
from database import User, Videojuego, UserReview

from schemas import UserRequestModel, ReviewRequestModel
from schemas import UserResponseModel, ReviewResponseModel, ReviewModificarModel

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
              version= "1.0.1",
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

@app.post("/reviews", response_model=ReviewResponseModel)
async def create_review(new_review: ReviewRequestModel):

    if User.select().where(User.id == new_review.id_usuario).first() is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if Videojuego.select().where(Videojuego.id == new_review.id_videojuego).first() is None:
        raise HTTPException(status_code=404, detail="El videojuego no existe")

    review = UserReview.create(user_id = new_review.id_usuario,
                               videojuego = new_review.id_videojuego,
                               review = new_review.review,
                               score = new_review.score)
    
    return review

@app.get("/reviews", response_model=List[ReviewResponseModel])
async def listado_reviews(page: int = 1, limit : int = 10):
    reviews = UserReview.select().paginate(page, limit)
    return reviews

@app.get("/reviews/{id}", response_model=ReviewResponseModel)
async def review_particular(id: int):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    return review

@app.put("/reviews/{id}", response_model=ReviewResponseModel)
async def modificar_review(id: int, modificacion: ReviewModificarModel):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    review.review = modificacion.review
    review.score = modificacion.score

    review.save()

    return review

@app.delete("/reviews/{id}", response_model = ReviewResponseModel)
async def eliminar_review(id: int):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    review.delete_instance()
    return review