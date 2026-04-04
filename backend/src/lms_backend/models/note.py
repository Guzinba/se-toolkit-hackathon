from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime

class Note(SQLModel, table=True):
    __tablename__ = "notes"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(max_length=2000)
    # Храним теги как JSON-массив в Postgres
    tags: List[str] = Field(default_factory=list, sa_column_kwargs={"server_default": " '[]'::jsonb"})
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        schema_extra = {
            "example": {
                "content": "Купить молоко",
                "tags": ["shopping", "urgent"],
                "created_at": "2024-04-04T10:00:00"
            }
        }
