from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    """Настройка для всех моделей."""

    @declared_attr
    def __tablename__(cls):  # noqa
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    """Функция-генератор асинхронных сессий."""
    async with AsyncSessionLocal() as async_session:
        yield async_session


class AbstractBase(Base):
    """Базовый абстрактный класс."""

    __abstract__ = True
    full_amount = Column(Integer, default=0)  # поле требуемой суммы
    invested_amount = Column(Integer, default=0)  # поле внесённой суммы
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    close_date = Column(DateTime)
