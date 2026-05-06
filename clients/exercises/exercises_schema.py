from pydantic import BaseModel, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from clients.courses.courses_schema import CourseSchema

class ExerciseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    courseId: CourseSchema
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
        Описание структуры ответа обновления курса.
        """
    exercise: ExerciseSchema


class GetExerciseResponseSchema(BaseModel):
    """
        Описание структуры запроса получения курса.
        """
    exercise: ExerciseSchema