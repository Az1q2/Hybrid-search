from pydantic import BaseModel, Field


class DocumentCreate(BaseModel):
    title: str = Field(..., max_length=255, description="Заголовок документа")
    content: str = Field(..., min_length=10, description="Текст документа (минимум 10 символов)")


class DocumentResponse(DocumentCreate):
    id: int

    class Config:
        from_attributes = True


class SearchQuery(BaseModel):
    query: str = Field(..., min_length=2, description="Текст поискового запроса")
    top_k: int = Field(5, ge=1, le=20, description="Сколько результатов вернуть (от 1 до 20)")