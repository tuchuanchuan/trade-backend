# coding: utf-8
import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from .base import ORMBase


class Collection(ORMBase):
    __tablename__ = 'collection'

    id = Column(Integer, primary_key=True, nullable=False, )

    account_id = Column(Integer, ForeignKey('account.id'), nullable=False, )
    track_id = Column(Integer, ForeignKey('track.id'), nullable=False, )
    is_deleted = Column(Integer, nullable=False, default=0, )

    created_datetime = Column(Datetime, default=datetime.datetime.now)

    account = relationship('Account')
    track = relationship('Track')
