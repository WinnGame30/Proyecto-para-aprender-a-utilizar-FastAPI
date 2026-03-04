from pydantic import BaseModel
from pydantic import ValidationError
from pydantic import model_validator

class User(BaseModel):
  username: str
  password: str
  repeat_password: str
  email: str
  age: int

  @model_validator(mode="after")
  def repeat_password_validation(self):
    if self.password != self.repeat_password:
      raise ValueError("Las contraseñas no coinciden")
    return self
  
try:
  user = User(username="Wi", password="12345678910", repeat_password="123456789",
              email="winn@example.com", age=25)
  print(user)

except ValidationError as e:
  print(e)