from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {"mensaje": "FastAPI funcionando correctamente"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
  return {"mensaje": f"Hola, {nombre}!"}

@app.get("/buscar")
def buscar(q: str | None = None):
  return {"busqueda": q}