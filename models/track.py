# coding: utf-8

from sqlalchemy import Column, Integer, String, ForeignKey

from .base import ORMBase


class Track(ORMBase):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True, nullable=False, )

    file_path = Column(String, nullable=False, )
    active = Column(Integer, nullable=False, default=0, )  # 标志上下架, 1:上架中
