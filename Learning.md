# Proyecto para aprender a utilizar FastAPI

Proyecto personal para aprender FastAPI y desarrollar APIs con Python

## Objetivo

Aprendizaje continuo y escalonado:
- APIs
- HTTP
- REST
- CRUD
- Manejo de Errores
- Documentación

## Contenido

- HTTP
- REST
- APIs
- CONEXION A BASES DE DATOS CON PEEWEE
- SCHEMAS
- PYDANTIC

### Notas Generales

#### 03/02/2026
##### HTTP
Protocolo de comunicación con el que seremos capaces de enviar y recibir información.

##### HTTPs
A diferencia de la primera, esta genera una conexión segura y encriptada entre el servidor y el cliente.

##### Cookies
Archivos que el cliente crea y almacena para guardar datos de navegación.

##### Sesión
Valores que se almacen en el servidor con la finalidad de almacenar información de una petición al pasar de una página a otra.

##### Verbos
Métodos para generar una buena comunicación entre el cliente y el servidor.
  - GET: Utilizar para obtener un objeto del servidor (imagén, video, etcétera)
  - POST: Crear recursos en el servidor (nuevos archivos)
  - PUT: Actualizar recursos en el servidor (registros o archivos existentes).
  - DELETE: Eliminar un recurso por parte del servidor.

##### Arquitectura CLIENTE-SERVIDOR
Un cliente (dispositivo) realiza una petición a un servidor (REQUEST) y el servidor entrega información (RESPONSE) al cliente mediante lo solicitado. Se utiliza el protocolo HTTP o HTTPS para realizar el envío de información entre uno y otro.

##### Status Code
Al utilizar, ya sea, el protocolo HTTP o HTTPS existen diferentes estatus para notificar el estado de una petición. Estos estatus se representan mediante un valor numérico, y a cada uno de estos valores se les conocen como status code.
Podemos agruparlos en 5 categorías.
  - Respuestas informativas (100–199),
  - Respuestas satisfactorias (200–299),
  - Redirecciones (300–399),
  - Errores de los clientes (400–499),
  - Errores de los servidores (500–599).

##### Arquitectura REST
Sistema que utiliza el Protocolo HTTP, y sus verbos (métodos), para definir las acciones a realizar. La utilización de las URLs como recursos para cada uno de los métodos, siendo capaz de tener 6 direcciones URL para cada recurso.

#### 04/02/2026

##### CURL
Herramienta de linea de comandos integrada para testear servicios web, transferir información para diferentes protocolos de internet (http, https, sttp, etcétera).

##### APIs
Siglas pertenecientes el título Apllication Programming Interface, utilizada para la comunicación entre aplicaciones. Existen 2 tipos de API:
  - Locales
  - Remotas: Se componen de servicios web

##### Buenas Practicas
- HATEOAS: La API se autodescribe; cada recurso tiene información de cual es el recurso siguiente o de la cantidad de recursos totales que hay.
- SEGURIDAD: Proteger las APIs privadas para evitar usurpación de información.
- TESTEAR: Para evitar problemas u errores mientras está en ejecución.
- DOCUMENTACION: Para poder compartir con los demás y sepan como funciona.

#### 06/02/2026

##### Ejemplo de servidor sencillo con PYTHON

```python
from wsgiref.simple_server import make_server

def application(env, start_response):
  headers = [ ("Content-Type", "text/plain") ]

  start_response("200 OK", headers)

  return [b"Hola mundo, desde mi primer servidor en Python!"]

server = make_server("localhost", 8000, application)
server.serve_forever()
```

#### 08/02/2026

##### Ejemplo de servidor con retorno de HTML

```python
from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<html>
  <head>
    <title>Servidor en Python</title>
    <body>
      <h1>Hola mundo, desde mi primer servidor en Python!</h1>
    </body>
  </head>
</html>
"""

def application(env, start_response):
  headers = [ ("Content-Type", "text/html") ]

  start_response("200 OK", headers)

  return [bytes(HTML, "utf-8")]

server = make_server("localhost", 8000, application)
server.serve_forever()
```

#### 10/02/2026

##### Creación de plantillas

Las plantillas nos permite implementar variables, ciclos, condiciones, entre otros. Así podemos generar páginas web dinámicas. En este caso se utiliza de la libreria "jinja2".

Mediante la utilización de dos juegos de llaves colocamos el nombre de la variable la cual será reemplazada, al renderizar el template, por el valor de la variable que nosotros indiquemos.

##### Ejemplo de template

```HTML
<!DOCTYPE html>
<html>
  <head>
    <title>{{ title }}</title>
    <body>
      <h1>Hola {{ name }}</h1>
    </body>
  </head>
</html>
```

#### 11/02/2026

##### Obtener el template y renderizar

Se requiere de importar dos clases, Enviroment y FileSystemLoader.

```Python
from wsgiref.simple_server import make_server
from jinja2 import Environment, FileSystemLoader

def application(env, start_response):
  headers = [ ("Content-Type", "text/html") ]

  start_response("200 OK", headers)
  
  env = Environment(loader=FileSystemLoader("templates"))

  template = env.get_template("index.html")

  html =template.render(
    {
      "title": "Servidor en Python",
      "name": "Fernando"
      })
  
  return [bytes(html, "utf-8")]

server = make_server("localhost", 8000, application)
server.serve_forever()
```

#### 23/02/2026

##### Primer cliente en PYTHON

Para poder realizar una petición utilizando PYTHON sobre el protocolo HTTP podemos utilziar el modulo URLLIB. Y a su vez, para realizar una solicitud a URLIB podemos utilizar el modulo REQUEST.

```Python
from urllib import request

URL = "http://localhost:8000/"

response = request.urlopen(URL)

print(response.read())
```

#### 02/03/2026

##### Type Hints

Nos permiten definir el tipo de dato que va a contener nuestra variable y así mejorar nuestro código y permitir una lectura y desarollo más rápidos. Enfocadas para auxiliar a los programados para seguir estandares de codificación.

En variables:
```Python
a: str = "Esto es una cadena"
b: int = 15
c: float = 19.5
d: bool = True
```

En funciones:
```Python
def suma(numero1: int, numero2: int) -> int
    return numero1 + numero2
```

En el anterior ejemplo tenemos una suma sencilla, pero le estámos diciendo a Python que la variable 1 y la variable 2, así como el resultado del método suma, van a contener un dato de tipo int.

En clases:
```Python
class User():
  def __init__(self, username: str, password: str) -> None:
    self.username = username
    self.password = password

  def saluda(self) -> str:
    return f"Hola {username}"

ejemplo = User("WinnGame", "1234")
print(ejemplo.saluda())
```

En colecciones:

```Python
from typing import List
calificaciones: List[int] = [10, 5, 9, 7, 9, 10, 10, 5]

def promedio(calificaciones: List[int]) -> float:
  return sum(calificaciones)/ len(calificaciones)

print(promedio(calificaciones))
```

En temas de colecciones podemos ser específicos indicando el tipo de dato que va a contener nuestra lista, tupla o diccionario. Pero es necesario importar List de Typing, aplica de la misma forma para Tuple[] y para Dict[].

##### Libreria Pydantic

Es una libreria que FASTAPI utiliza, ya que ayuda a validar los datos de entrada y de salida, y las validaciones se implementan utilizando anotaciones. Es necesario utilizar la clase BaseModel para validar que los valores que almacenen los atributos sean los correctos con respecto a los type hints.

```Python
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
```

#### 03/03/2026

##### Validator

Podemos crear nuestras propias validaciones utilizando del decorador VALIDATOR para nuestros modelos.

Ejemplo para validar un solo dato:

```Python
from pydantic import BaseModel
from pydantic import FieldValidator
from pydantic import ValidationError

class User(BaseModel):
  username: str
  password: str
  email: str
  age: int

  @field_validator("username")
  def username_validation_lenght(cls, usernamer):
    if (len(usernamer) < 3):
      raise ValueError("La longitud mínima es de 4 caracteres")
    if (len(usernamer) > 50):
      raise ValueError("La longitud máxima es de 50 caracteres")
    return usernamer
  
try:
  informacion = {
  "username": "Wi",
  "password": "123456789",
  "email": "winn@example.com",
  "age": 25
  }

  user = User(**informacion)
  print(user)

except ValidationError as e:
  print(e.json())
```

Ejemplo para validar uno o más datos:

```Python
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
```

##### FastApi

Para utilizar la libreria FastApi es necesario instalar y, posteriormente, importar la clase:

```Py
from fastapi import FastAPI
```

Es necesario crear nuestra aplicación y podemos definirla con title, description y version.

```Py
app = FastAPI(title= "Proyecto FastAPI",
              description= "Proyecto de ejemplo con FastAPI",
              version= "1.0.0")
```

Podemos crear diferentes rutas, o urls, para definir las acciones que quermeos que nuestra aplicación tenga dependiendo del método http y lo que desee el usuario.

```Py
# Get para indicar las peticiones
@app.get("/")
def read_root():
    return {"message": "Hola, bienvenido a mi proyecto FastAPI!"}
```

Y podemos indicar en nuestra url que trabaje de manera asincrona por si recibe múltiples peticiones al mismo tiempo.

```Py
async def read_root():
```

#### 08/03/2026

##### Eventos

Podemos realizar eventos antes que el servidor inicie y eventos después de que el servidor se esté apagando, con startup y shutdown respectivamente. Actualmente se hace uso de la función lifespan de la siguiente forma:

```Python
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando la aplicación...")
    yield
    print("Cerrando la aplicación...")
```

Donde asynccontextmanager es un decorador de Python que convierte una función con yield en un context manager asíncrono. Lo obtenemos al importar de la libreria contextlib. Ejemplo con main:

```Python
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando la aplicación...")
    yield
    print("Cerrando la aplicación...")

app = FastAPI(title= "Proyecto FastAPI",
              description= "Proyecto de ejemplo con FastAPI",
              version= "1.0.0",
              lifespan=lifespan)
```

##### Conexión a Base de Datos

Para hacer posible que nuestro programa se conecte con una base de datos debemos hacer uso de un ORM llamado PEEWEE, también llamado Object-Relational Mapper, es ligero para Python y permite trabajar con bases de datos usando objetos y clases de Python en lugar de escribir SQL directamente.
Conectamos y después creamos una nueva Base de Datos

```SQL
mysql -u root -p

CREATE DATABASE fastapi_project
```

Para conocer la aplicación con el gestor de base de datos:

```Python
from peewee import *

database = MySQLDatabase("fastapi_project", user="root", password="contraseña",
                         host="localhost", port=3306)
```

Ejemplo de conexión de servidor con base de datos:

```Python
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    if connection.is_closed():
        connection.connect()
        print("Iniciando el servidor...")
    
    yield
    
    if not connection.is_closed():
        connection.close()
        print("Cerrando el servidor...")
    
app = FastAPI(title= "Proyecto FastAPI",
              description= "Proyecto de ejemplo con FastAPI",
              version= "1.0.0",
              lifespan=lifespan)
```

#### 11/03/2026

Este día se realizó un ejemplo de creación de tablas en bases de datos, se utilizaron modelos para definir las tablas y atributos para definir las columnas.

#### 15/03/2026

Este día de realizó un ejemplo de modelos dentro de nuestro ejercicio para la creación de campos en las tablas, se definin parámetros específicos para cada Usuario, Videojuego y Reseña. Se aprende a utilizar un archivo schemas para validar los datos de entrada y salida de la API.

Se realizó la codificación para la creación de nuevos usuarios.
```PYTHON
@app.post("/users/")
async def create_user(user: UserBaseModel):
    user = User.create(username=user.username, password=user.password)
    return {"id": user.id, "username": user.username}
```

#### 16/03/2026

Utilizar FIELD VALIDATOR para validar la longitud de un nombre de usuario.

```Python
@field_validator("username", mode="before")
def validate_username(cls, value):
  if len(value) < 3:
    raise ValueError("El nombre de usuario debe tener al menos 3 caracteres")
  elif len(value) > 50:
    raise ValueError("El nombre de usuario no puede tener más de 50 caracteres")
  return value
```

Aprender a encriptar contraseñas. Este ejemplo de realizó con HASH MD5.

```PYTHON
@classmethod
    def creat_password(cls, password: str):
        h = hashlib.md5()
        password = h.update(password.encode("utf-8"))
        return h.hexdigest()
```

```PYTHON
@app.post("/users")
async def create_user(user: UserBaseModel):
    hash_password = User.creat_password(user.password)

    user = User.create(username = user.username,
                       password = hash_password)
    return {user.id}
```

Actualizar ante una posible excepción por usuario duplicado

```Python
@app.post("/users")
async def create_user(user: UserBaseModel):

    if User.select().where(User.username == user.username).exists():
        return HTTPException(status_code=409, detail="El username ya existe")

    hash_password = User.creat_password(user.password)

    user = User.create(username = user.username,
                       password = hash_password)
    return {user.id}
```

Utilizar un modelo para la respuesta del servidor

```PYTHON
class UserResponseModel(BaseModel):
    id: int
    username: str
```

```PYTHON
return UserResponseModel(id = user.id, username = user.username)
```

#### 18/03/2026

Se aprendieron a utilizar RESPONSE MODELS.

#### 20/03/2026

Validar puntaje entre 0 y 10

```Python
    @field_validator("score", mode="before")
    def validacion_score(cls, score):
        if score < 0 or score > 10:
            raise ValueError("La puntuación debe estar entre 0 y 10")
        return score
```

Obtener reseñas específicas

```Python
@app.get("/listado_reviews/{id}", response_model=ReviewResponseModel)
async def review_particular(id: int):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    return review
```

#### 21/03/2026

Modificar reseñas

```Python
@app.put("/modificar_review/{id}", response_model=ReviewResponseModel)
async def modificar_review(id: int, modificacion: ReviewModificarModel):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    review.review = modificacion.review
    review.score = modificacion.score

    review.save()

    return review
```

Eliminar reseñas

```Python
@app.delete("/eliminar_review/{id}", response_model = ReviewResponseModel)
async def eliminar_review(id: int):
    review = UserReview.select().where(UserReview.id == id).first()

    if review is None:
        raise HTTPException(status_code=404, detail="La reseña no existe")
    
    review.delete_instance()
    return review
```

#### 22/03/2026

Se modularizo y se crearon routers dentro del proyecto

#### 24/03/2026

Familiarizacion con la libreria request

```python
import requests

url = "http://127.0.0.1:8000/api/v1/reviews"

response = requests.get(url)

if response.status_code == 200:
    print("Petición realizada con éxito")

    print (response.content)
```

GET

```python
import requests

url = "http://127.0.0.1:8000/api/v1/reviews"
encabezados = { "accept": "application/json" }
queryset = { "page": 1, "limit": 2 }

response = requests.get(url, headers = encabezados, params = queryset)

if response.status_code == 200:
    print("Petición realizada con éxito")

    if response.headers.get("Content-Type") == "application/json":
        
        reviews = response.json()
        for review in reviews:
            print(f'score: {review["score"]} - review: {review["review"]}')
```

POST

```python

```