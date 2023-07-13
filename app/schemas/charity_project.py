from datetime import datetime

from pydantic import BaseModel, Field, PositiveInt, validator


class CharityProjectBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )
    description: str = Field(
        ...,
        min_length=1,
    )
    full_amount: PositiveInt


class CharityProjectCreate(CharityProjectBase):
    @validator('name')
    def validate_name(cls, value): # noqa
        if not value:
            raise ValueError('Имя не может быть пустым!')
        return value


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int = 0
    fully_invested: bool = False
    create_date: datetime
    close_date: datetime = None

    class Config:
        orm_mode = True
