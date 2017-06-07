# coding: UTF-8

import settings
from controllers_backend.backend_base_controller import BaseController

from models.tag import Tag
from models.user import Account


class TagListController(BaseController):
    urls = '/operation/index_config/?'

    def get(self):
        pass


class UserListController(BaseController):
    urls = '/operation/user/list/?'

    def get(self):
        search_type = self.get_argument('search_type')
        search_key = self.get_argument('search_key')

        if search_type == 'id':
            user_id_list = map(int, search_key.split(','))
            user_list = self.orm_session.query(Account).filter(Account.id.in_(user_id_list)).all()
        elif search_type == 'email':
            user_list = self.orm_session.query(Account).filter(Account.username == search_key).all()
        self.render('operation/user.html', user_list=user_list)
