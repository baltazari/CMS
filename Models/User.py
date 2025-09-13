from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, sa_column_kwargs={"unique": True})
    email: str = Field(index=True)
    password: str
    password_repeat: str
    phone_number: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
