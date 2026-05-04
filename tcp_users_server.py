import socket

# Список для хранения истории сообщений
messages = []

# Создаём TCP-сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(10)
print("TCP-сервер запущен на localhost:12345")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Пользователь с адресом: {client_address} подключился к серверу")

    # Получаем сообщение от клиента (до 1024 байт)
    data = client_socket.recv(1024).decode().strip()
    print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

    # Добавляем сообщение в историю
    messages.append(data)

    # Отправляем клиенту всю историю, каждое сообщение с новой строки
    response = '\n'.join(messages)
    client_socket.send(response.encode())

    client_socket.close()