from sqlalchemy import Column, Text

from app.core.db import Base, BaseAbstract


class Donation(Base, BaseAbstract):
    comment = Column(Text, nullable=True)
