from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class BaseDTO(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,  # для работы с объектами классов
        validate_assignment=True,  # для включения валидации при обновлении
        str_strip_whitespace=True,
        populate_by_name=True,  # Aliased allowed из сырых данных JSON
        arbitrary_types_allowed=False,  # Строго конкретные типы данных, без Any
        extra='forbid'
    )


class TimestampDTOMixin(BaseModel):
    created_at: datetime = Field(
        description='Date and time of object creation',
        examples=["2025-06-25T00:00:00Z"],
    )
    updated_at: datetime = Field(
        description='Date and time of object last update ',
        examples=["2025-06-25T00:00:00Z"],
    )


class IdDTOMixin(BaseModel):
    id: int = Field(gt=0)


class PaginationRequestDTO(BaseModel):
    page: int = Field(
        default=1,
        ge=1
    )
    per_page: int = Field(
        default=10,
        ge=1,
        le=40
    )


class PaginationResponseDTO(BaseModel):
    page: int
    per_page: int
    total: int
    pages: int
    has_next: bool
    has_prev: bool
