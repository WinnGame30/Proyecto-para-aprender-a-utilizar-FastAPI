from pydantic import BaseModel

class User(BaseModel):
  id: str
  password: str
  email: str
  age: int

informacion = {
  "id": "123456789",
  "password": "123456789",
  "email": "winn@example.com",
  "age": 25
}

user = User(**informacion)
print(user)