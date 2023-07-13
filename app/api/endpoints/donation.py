from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.donation import donation_crud
from app.schemas.donation import DonationUserDB, DonationCreate, DonationSuperuserDB

router = APIRouter()


@router.post(
    '/',
    response_model=DonationUserDB,
    response_model_exclude_none=True
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session)
):
    new_donation = await donation_crud.create(
        donation,
        session
    )
    return new_donation


@router.get(
    '/',
    response_model=List[DonationSuperuserDB],
)
async def get_all_donation(
        session: AsyncSession = Depends(get_async_session)
):
    donations = await donation_crud.get_multi(
        session
    )
    return donations
