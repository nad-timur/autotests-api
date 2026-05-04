import socket

# Создаём TCP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Отправляем сообщение серверу
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ и выводим его
response = client_socket.recv(1024).decode()
print(response)

client_socket.close()