from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, Extra


class DonationBase(BaseModel):
    comment: Optional[str]
    full_amount: PositiveInt
    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    pass


class DonationUserDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationSuperuserDB(DonationUserDB):
    user_id: int
    invested_amount: int = 0
    fully_invested: bool = False
    close_date: datetime = None

    class Config:
        orm_mode = True
