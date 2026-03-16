# Para validar los datos de entrada y salida de la API

from pydantic import BaseModel

class UserBaseModel(BaseModel):
    username: str
    password: str


