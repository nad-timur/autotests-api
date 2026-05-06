from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

#  Создаём тестового пользователя
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)

#  Формируем учётные данные для авторизации
auth_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

#  Получаем приватный клиент и запрашиваем данные пользователя по ID
private_users_client = get_private_users_client(auth_user)
get_user_response = private_users_client.get_user_api(create_user_response.user.id)
get_user_response.raise_for_status()  # убедимся, что запрос успешен

#  Генерируем JSON-схему из Pydantic-модели ответа
get_user_response_schema = GetUserResponseSchema.model_json_schema()

#  Валидируем JSON-ответ сервера на соответствие схеме
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

print("Валидация прошла успешно!")