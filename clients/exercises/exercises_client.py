from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.users.private_users_client import User


class Exercise(TypedDict):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    courseId: str


class CreateExerciseResponseDict(TypedDict):
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения курса.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получить список упражнений для заданного курса.

        :param query: Словарь с ключом `courseId`.
        :return: Словарь с ключом `exercises` и значением – списком упражнений.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> Exercise:
        """
        Получить одно упражнение по его ID.

        :param exercise_id: Идентификатор упражнения.
        :return: Словарь с полями упражнения.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Создать новое упражнение.

        :param request: Данные для создания упражнения.
        :return: Словарь с ключом `exercise`, содержащим созданное упражнение.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(
            self, exercise_id: str, request: UpdateExerciseRequestDict
    ) -> UpdateExerciseResponseDict:
        """
        Обновить существующее упражнение.

        :param exercise_id: Идентификатор упражнения.
        :param request: Данные для обновления.
        :return: Словарь с ключом `exercise`, содержащим обновлённое упражнение.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))