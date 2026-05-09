from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, ExerciseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(
    request: CreateExerciseRequestSchema,
    response: CreateExerciseResponseSchema,
):
    """
    Проверяет, что ответ на создание упражнения соответствует данным запроса.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API с данными созданного упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.maxScore, request.max_score, "max_score")
    assert_equal(response.exercise.minScore, request.min_score, "min_score")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimatedTime, request.estimated_time, "estimated_time")
    assert_equal(response.exercise.courseId, request.course_id, "course_id")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.maxScore, expected.maxScore, "max_score")
    assert_equal(actual.minScore, expected.minScore, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimatedTime, expected.estimatedTime, "estimated_time")
    assert_equal(actual.courseId, expected.courseId, "course_id")


def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет ответ получения данных задания.

    :param get_exercise_response: Ответ API при запросе задания.
    :param create_exercise_response: Ответ API при создании задания.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema
):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Исходный запрос на обновление задания.
    :param response: Ответ API с обновленными данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.maxScore, request.maxScore, "max_score")
    assert_equal(response.exercise.minScore, request.minScore, "min_score")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimatedTime, request.estimatedTime, "estimated_time")

def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    # Ожидаемое сообщение об ошибке, если файл не найден
    expected = InternalErrorResponseSchema(details="Exercise not found")
    # Используем ранее созданную функцию для проверки внутренней ошибки
    assert_internal_error_response(actual, expected)


def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercise_responses: Список API ответов при создании заданий.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)
