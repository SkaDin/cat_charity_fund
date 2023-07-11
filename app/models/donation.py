from sqlalchemy import Column, ForeignKey, Text, Integer

from app.core.db import AbstractBase


class Donation(AbstractBase):
    comment = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
