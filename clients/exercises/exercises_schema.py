from pydantic import BaseModel, ConfigDict
from clients.courses.courses_schema import CourseSchema


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    courseId: str


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнения.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
        Описание структуры запроса на обновления упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = None
    maxScore: int | None = None
    minScore: int | None = None
    description: str | None = None
    estimatedTime: str | None = None


class UpdateExerciseResponseSchema(BaseModel):
    """
        Описание структуры ответа обновления упражнения.
    """
    exercise: ExerciseSchema


class GetExerciseResponseSchema(BaseModel):
    """
        Описание структуры запроса получения упражнения.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
        Описание структуры запроса получения списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True)

    courseId: str


class GetExercisesResponseSchema(BaseModel):
    """
        Описание структуры ответа получения списка упражнений.
    """
    exercises: list[ExerciseSchema]