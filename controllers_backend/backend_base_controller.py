# coding: UTF-8

from tools.utils import cached_property
from base_controller import BaseController as TradeBaseController

from models.user import Admin


class BaseController(TradeBaseController):

    @cached_property
    def current_user(self):
        if 'trade_backend_id' in self.session:
            user = self.orm_session.query(Admin).\
                filter_by(id=self.session['trade_backend_id']).\
                first()
            return user
        return None

    def prepare(self):
        if not self.current_user or self.current_user.forbidden:
            self.session['trade_backend_id'] = 0
            self.redirect('/login')
