from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    @staticmethod
    async def get_charity_project_by_id(
            charity_project_name: str,
            session: AsyncSession,
    ) -> Optional[CharityProject]:
        charity_project = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_project_name
            )
        )
        return charity_project.scalars().first()

    # async def update_charity_project_same_name(
    #         self,
    #
    # ):


charity_project_crud = CRUDCharityProject(CharityProject)
