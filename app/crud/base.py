from typing import Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:
    """Базовый класс для базовых CRUD-операций."""

    def __init__(self, model):
        self.model = model

    async def get(
            self,
            obj_id: int,
            session: AsyncSession,
    ):
        """Получение объекта."""
        get_obj_in_db = await session.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )
        return get_obj_in_db.scalars().first()

    async def get_multi(
            self,
            session: AsyncSession
    ):
        """Получение всех объектов."""
        db_obj_all = await session.execute(select(self.model))
        return db_obj_all.scalars().all()

    async def create(
            self,
            obj_in,
            session: AsyncSession,
    ):
        """Создание объекта."""
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    @staticmethod
    async def update(
            db_obj,
            obj_in,
            session: AsyncSession,
    ):
        """Обновление объекта."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    @staticmethod
    async def remove(
            db_obj,
            session: AsyncSession,
    ):
        """Удаление объекта."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj
