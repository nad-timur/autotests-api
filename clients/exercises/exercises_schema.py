from pydantic import BaseModel, ConfigDict, Field
from tools.fakers import fake


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

    title: str = Field(default_factory=fake.sentence)
    maxScore: int = Field(alias="maxScore", default_factory=fake.max_score)
    minScore: int = Field(alias="minScore", default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    estimatedTime: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
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

    title: str | None = Field(default_factory=fake.sentence)
    maxScore: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    minScore: int | None = Field(alias="minScore", default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimatedTime: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


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