# coding: utf-8
import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from .base import ORMBase


class Order(ORMBase):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, nullable=False, )
    order_id = Column(Integer, nullable=False, unique=True, )

    account_id = Column(Integer, ForeignKey('account.id'), nullable=False, )
    status = Column(Integer, nullable=False, default=0, )
    remark = Column(String(512), nullable=False, default='', )
    created_datetime = Column(DateTime, default=datetime.datetime.now, )
    finished_datetime = Column(DateTime, )


class OrderDetail(ORMBase):
    __tablename__ = 'order_detail'

    id = Column(Integer, primary_key=True, nullable=False, )

    order_id = Column(Integer, ForeignKey('order.id'), nullable=False, )
    track_id = Column(Integer, ForeignKey('track.id'), nullable=False, )
    amount = Column(Integer, nullable=False, default=1, )  # 单位是分
    unit_price = Column(Integer, nullable=False, default=0, )  # 单位是分
    deal_type = Column(Integer, nullable=False, default=0, )  # 授权类型
