import asyncio
import websockets
from websockets import ServerConnection


async def handle_user(websocket: ServerConnection):
    """Обрабатывает одно WebSocket-соединение."""
    async for message in websocket:
        # Логируем полученное сообщение
        print(f"Получено сообщение от пользователя: {message}")

        # Отправляем пять ответных сообщений с порядковым номером
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)


async def main():
    server = await websockets.serve(handle_user, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())