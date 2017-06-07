# coding: utf-8
import uuid
import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from .base import ORMBase


class Order(ORMBase):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, nullable=False, )
    long_id = Column(String(64), unique=True, default=None, )

    account_id = Column(Integer, ForeignKey('account.id'), nullable=False, )
    status = Column(Integer, nullable=False, default=0, )
    pay_amount = Column(Integer, nullable=False, default=0, )
    remark = Column(String(512), nullable=False, default='', )
    created_datetime = Column(DateTime, default=datetime.datetime.now, )
    finished_datetime = Column(DateTime, )

    def generate_order_id(self):
        self.long_id = uuid.uuid4().hex

    @property
    def description(self):
        pass

    @property
    def status_text(self):
        pass

    @property
    def total_ammount(self):
        """订单内所有项价格总和"""
        pass


class OrderDetail(ORMBase):
    __tablename__ = 'order_detail'

    id = Column(Integer, primary_key=True, nullable=False, )

    order_id = Column(Integer, ForeignKey('order.id'), nullable=False, )
    track_id = Column(Integer, ForeignKey('track.id'), nullable=False, )
    amount = Column(Integer, nullable=False, default=1, )  # 单位是分
    unit_price = Column(Integer, nullable=False, default=0, )  # 单位是分
    deal_type = Column(Integer, nullable=False, default=0, )  # 授权类型
