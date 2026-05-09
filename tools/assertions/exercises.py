from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.assertions.base import assert_equal


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