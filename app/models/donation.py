from sqlalchemy import Column, Text

from app.core.db import AbstractBase


class Donation(AbstractBase):
    comment = Column(Text, nullable=True)
