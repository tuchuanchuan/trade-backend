# coding: utf-8
import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from .base import ORMBase


class SearchHistory(ORMBase):
    __tablename__ = 'search_history'

    id = Column(Integer, primary_key=True, nullable=False, )

    account_id = Column(Integer, ForeignKey('account.id'), nullable=False, )

    keyword = Column(String(512), nullable=False, default='', )
    search_datetime = Column(DateTime, default=datetime.datetime.now, nullable=False, )

    account = relationship('Account')
