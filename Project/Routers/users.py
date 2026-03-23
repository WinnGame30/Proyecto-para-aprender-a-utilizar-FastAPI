from fastapi import HTTPException
from fastapi import APIRouter
from fastapi.security import HTTPBasicCredentials
from fastapi import Response
from fastapi import Cookie

from ..database import User

from ..schemas import UserRequestModel, UserResponseModel, ReviewResponseModel

from typing import List

router = APIRouter(prefix="/users")

@router.post("/login", response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):
    
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if user.password != User.create_password(credentials.password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    response.set_cookie(key = "user_id", value = user.id)
    return user

@router.post("/", response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).exists():
        raise HTTPException(status_code=409, detail="El username ya existe")

    hash_password = User.create_password(user.password)

    user = User.create(username = user.username,
                       password = hash_password)
    
    return user

@router.get("/reviews", response_model=List[ReviewResponseModel])
async def get_reviews(user_id: int = Cookie(default=None)):
    
    user = User.select().where(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=401, detail="No estás autenticado")
    
    return [user_review for user_review in user.reviews]