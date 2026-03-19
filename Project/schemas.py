from pydantic import BaseModel, field_validator
from pydantic import BaseModel
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

# ------------ Reseña ------------ #

class ReseñaRequestModel(BaseModel):
    id_usuario: int
    id_videojuego: int
    review: str
    score: int

class ReseñaResponseModel(ResponseModel):
    id: int
    videojuego_id: int
    review: str
    score: int


