# coding: utf-8

from sqlalchemy import Column, Integer, String, ForeignKey

from .base import ORMBase


class Tag(ORMBase):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, nullable=False, )

    name = Column(String(16), nullable=False, default='', )
    type_name = Column(String(16), nullable=False, default='', )
    active = Column(Integer, nullable=False, default=0, )
