from pydantic import BaseModel, field_validator
from pydantic.utils import GetterDict

from peewee import ModelSelect

from typing import Any

class PeeweeGetterDict(GetterDict):
    def get(self, key : Any, default : Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res
    
class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class ReviewValidator():
    @field_validator("score", mode="before")
    def validacion_score(cls, score: int):
        if not (0 <= score <= 10):
            raise ValueError("La puntuación debe estar entre 0 y 10")
        return score

# ------------ Usuario ------------ #
    
class UserRequestModel(BaseModel):
    username: str
    password: str

    @field_validator("username", mode="before")
    def validate_username(cls, value):
        if len(value) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
        elif len(value) > 50:
            raise ValueError("El nombre de usuario no puede tener más de 50 caracteres")
        return value

class UserResponseModel(ResponseModel):
    id: int
    username: str

# ------------ Videojuego ------------ #

class VideojuegoResponseModel(ResponseModel):
    id: int
    title: str

# ------------ Reseña ------------ #

class ReviewRequestModel(BaseModel, ReviewValidator):
    user_id: int
    videojuego_id: int
    review: str
    score: int
    
class ReviewResponseModel(ResponseModel):
    id: int
    videojuego: VideojuegoResponseModel
    review: str
    score: int

class ReviewModificarModel(BaseModel, ReviewValidator):
    review: str
    score: int

