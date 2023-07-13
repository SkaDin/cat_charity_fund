from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class DonationBase(BaseModel):
    comment: Optional[str]


class DonationCreate(DonationBase):
    full_amount: PositiveInt


class DonationUserDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationSuperuserDB(DonationBase):
    user_id: Optional[int]
    invested_amount: int = 0
    fully_invested: bool = False
    close_date: datetime = None

    class Config:
        orm_mode = True
