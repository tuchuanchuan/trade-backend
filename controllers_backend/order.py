# coding: UTF-8

from sqlalchemy import or_

import settings
from controllers_backend.backend_base_controller import BaseController

from models.order import Order


class OrderOverviewController(BaseController):
    urls = '/order/overview/?'

    def get(self):
        self.render('order/overview.html')


class OrderListController(BaseController):
    urls = '/order/list/?'

    def get(self):
        self.render('order/list.html')


class OrderQueryController(BaseController):
    urls = '/order/query/?'

    def get(self):
        date = self.get_argument('date', '')
        search_type = self.get_argument('search_type', '')
        search_key = self.get_argument('search_key', '')
        page = int(self.get_argument('page', 1) or 1)

        query = self.orm_session.query(Order)
        if search_type == 'long_id':
            query = query.filter(Order.long_id == search_key)
        elif search_type == 'account_id':
            account_id_list = map(int, search_key.split(','))
            query = query.filter(Order.account_id.in_(account_id_list))
            if date:
                query = query.filter(Order.created_datetime.between(date, date))
        count = query.count()
        order_list = query.limit(20).offset(10*(page-1)).all()

        self.write(dict(
            ret=0,
            order_list=[self.to_dict(order, attrs) for order in order_list],
            page_count=int((count)-1/10+1),
            current=page,
        ))
