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
    number = Column(Integer, nullable=False, default=1, )
    unit_price = Column(Integer, nullable=False, default=0, )  # 单位是分
    deal_type = Column(Integer, nullable=False, default=0, )  # 授权类型
    is_deleted = Column(Integer, nullable=False, default=0, )

    created_datetime = Column(Datetime, default=datetime.datetime.now)
