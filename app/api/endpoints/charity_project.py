from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import CharityProjectCreate, CharityProjectDB

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB
)
async def create_new_charity_project(
        charity: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
):
    new_project = await charity_project_crud.create(
        charity,
        session
    )
    return new_project


@router.get(
    '/',
    response_model=CharityProjectDB
)
async def get_charity_project(
        charity_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    charity_project = await charity_project_crud.get(
        charity_id,
        session
    )
    return charity_project
