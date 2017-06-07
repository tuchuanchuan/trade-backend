# coding: utf-8

from sqlalchemy import Column, Integer, String, ForeignKey

from .base import ORMBase


class Tag(ORMBase):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, nullable=False, )

    name = Column(String(16), nullable=False, default='', )
    father_id = Column(Integer, ForeignKey('tag.id'), nullable=False, default=0, )
    active = Column(Integer, nullable=False, default=0, )

    @classmethod
    def get_top_tags(cls, orm_session):
        return orm_session.query(cls).\
            filter(cls.father_id == 0).\
            filter(cls.active == 1).all()

    @classmethod
    def get_tags(cls, father_id, orm_session):
        return orm_session.query(cls).\
            filter(cls.father_id == father_id).\
            filter(cls.active == 1).all()
