from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_charity_project_exists
from app.core.db import get_async_session
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB
)
async def create_new_charity_project(
        charity: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
):
    new_charity_project = await charity_project_crud.create(
        charity,
        session
    )
    return new_charity_project


@router.get(
    '/{charity_project_id}',
    response_model=CharityProjectDB
)
async def get_charity_project(
        charity_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    await check_charity_project_exists(
        charity_id,
        session
    )
    charity_project = await charity_project_crud.get(
        charity_id,
        session
    )
    return charity_project


@router.delete(
    '/{charity_project_id}',
    response_model=CharityProjectDB
)
async def delete_charity_project(
        charity_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    charity_project = await check_charity_project_exists(
        charity_id,
        session
    )
    charity_project_delete = await charity_project_crud.remove(
        charity_project,
        session
    )
    return charity_project_delete


@router.patch(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
)
async def update_charity_project(
        charity_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session)
):
    charity_project = await check_charity_project_exists(
        charity_id,
        session
    )
    charity_project_update = await charity_project_crud.update(
        charity_project,
        obj_in,
        session
    )
    return charity_project_update
