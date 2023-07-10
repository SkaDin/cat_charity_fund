from sqlalchemy import Column, Text

from app.core.db import Base, BaseAbstract


class CharityProject(Base, BaseAbstract):
    description = Column(Text, nullable=False)

