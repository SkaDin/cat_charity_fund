from datetime import datetime
from typing import Union

from fastapi import Depends
from select import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.user import current_superuser
from app.models import User, Donation
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate


async def investments(
        project: CharityProject,
        donation: Donation
):
    donation.invested_amount += donation.full_amount
    donation.invested_amount += project.invested_amount
    if project.invested_amount >= project.full_amount:
        project.fully_invested = True
        project.close_date = datetime.utcnow()
        if project.invested_amount:
            donation.invested_amount = project.invested_amount
            return project
        return project


async def delete_charity_projects(
        charity_project_id: CharityProject,
        user: User = Depends(current_superuser)
):
    if charity_project_id.invested_amount and not user.is_superuser:
        raise ValueError('Нельзя удалить проект с инвестициями!')
