# coding: UTF-8
import time

from tornado.web import HTTPError

import settings
from controllers_backend.backend_base_controller import BaseController
from models.user import Admin


class LoginController(BaseController):
    urls = ['/login/?', '/?']

    def prepare(self):
        pass

    def get(self):
        if self.session and self.current_user:
            self.redirect('/index')
            return
        self.render('login.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

        user = Admin.login(self.orm_session, username, password)
        if user and not user.forbidden:
            self.session['trade_backend_id'] = user.id
            self.set_secure_cookie(
                'trade_backend_sid',
                self.session.sessionid,
                domain=settings.COOKIE_DOMAIN,
                expires_days=None,
            )
            user.last_login_ip = self.request.remote_ip
            user.last_login_time = time.time()
            self.session.save()
            # self.write(dict(ret=0, msg=u'ok', uri='/index'))
            self.redirect('/index')
        else:
            raise HTTPError(403)


class LogoutController(BaseController):
    urls = '/logout/?'

    def prepare(self):
        pass

    def get(self):
        if self.session:
            self.session['trade_backend_id'] = 0
            self.session.save()
            self.redirect('/')
