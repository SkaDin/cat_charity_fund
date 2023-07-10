from sqlalchemy import Column, Text

from app.core.db import Base


class CharityProject(Base):
    description = Column(Text, nullable=False)
