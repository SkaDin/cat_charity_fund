from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_charity_project_exists, check_name_duplicate, delete_charity_project
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.models import CharityProject, Donation
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.schemas.donation import DonationCreate
from app.services.investment import investment

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def create_new_charity_project(
        charity: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
):
    await check_name_duplicate(
        charity.name,
        session
    )
    new_charity_project = await charity_project_crud.create(
        charity,
        session
    )
    await investment(
        new_charity_project,
        Donation,
        session
    )
    return new_charity_project


@router.get(
    '/',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True
)
async def get_all_charity_project(
        session: AsyncSession = Depends(get_async_session)
):
    charity_project_all = await charity_project_crud.get_multi(
        session
    )
    return charity_project_all


@router.delete(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],

)
async def delete_charity_projects(
        charity_project_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    charity_project = await check_charity_project_exists(
        charity_project_id,
        session
    )
    await delete_charity_project(charity_project)
    charity_project_delete = await charity_project_crud.remove(
        charity_project,
        session
    )
    return charity_project_delete


@router.patch(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True
)
async def update_charity_project(
        charity_project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session)
):
    charity_project = await check_charity_project_exists(
        charity_project_id,
        session
    )
    if obj_in.name is not None:
        await check_name_duplicate(
            obj_in.name,
            session
        )
    charity_project_update = await charity_project_crud.update(
        charity_project,
        obj_in,
        session
    )

    return charity_project_update
