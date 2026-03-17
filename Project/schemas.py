from pydantic import BaseModel, field_validator
# Para validar los datos de entrada y salida de la API

from pydantic import BaseModel

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

class UserResponseModel(BaseModel):
    id: int
    username: str
