import requests

url = f"http://127.0.0.1:8000/api/v1/users/"

credentials = {
  "username": "User3",
  "password": "User3"
}

response = requests.post(url + "login", json=credentials)

if response.status_code == 200:
    print("Login exitoso")

    user_id = response.cookies.get_dict().get("user_id")

    response = requests.get(url + "reviews/", cookies={"user_id": user_id})
    if response.status_code == 200:
        for review in response.json():
            print(f"review: {review['review']}, score: {review['score']}")

else:
    print("Error en el login")
    print("Código de estado:", response.status_code)
    print("Respuesta:", response.json())

