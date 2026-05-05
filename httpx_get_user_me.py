import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Формируем accessToken
access_token = login_response_data["token"]["accessToken"]

# Выполняем запрос с данными о пользователе
get_user = httpx.get("http://localhost:8000/api/v1/users/me", headers={
    "Authorization": f"Bearer {access_token}"
})

get_user_data = get_user.json()

# Выводим ответ от сервера с данными о пользователе и статус код ответа
print("User data:", get_user_data)
print("Status Code:", get_user.status_code)

