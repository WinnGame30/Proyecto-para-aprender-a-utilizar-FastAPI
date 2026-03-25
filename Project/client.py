import requests

url = "http://127.0.0.1:8000/api/v1/reviews"
review = { 
    "user_id": 1,
    "videojuego_id" : 1,
    "review": "Excelente juego, lo recomiendo mucho",
    "score": 10
}


response = requests.post(url, json = review)


if response.status_code == 200:
    print("Reseña creada exitosamente")

else:
    print(response.content)