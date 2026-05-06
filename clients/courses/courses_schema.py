from pydantic import BaseModel, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: FileSchema  # Вложенная структура файла
    estimatedTime: str
    createdByUser: UserSchema  # Вложенная структура пользователя


class CreateCourseRequestSchema(BaseModel):
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


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
        Описание структуры ответа обновления курса.
        """
    course: CourseSchema


class GetCourseResponseSchema(BaseModel):
    """
        Описание структуры запроса получения курса.
        """
    course: CourseSchema