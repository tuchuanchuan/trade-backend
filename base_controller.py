# coding: UTF-8
import json
import logging

from sqlalchemy.orm import sessionmaker
from tornado.web import HTTPError, RequestHandler

import settings
from tools.utils import cached_property
from tools.db import get_engine, get_redis_connection
from tools.session import Session
from models.user import Account


class BaseController(RequestHandler):

    @cached_property
    def session(self):
        """Session

        :rtype: tools.session.Session
        """
        session = Session(sessionid=self.session_id, conn=get_redis_connection())
        if not self.session_id:
            self.set_secure_cookie('sell_sid', session.sessionid, domain=settings.COOKIE_DOMAIN)
        return session

    @session.deleter
    def session(self):
        """del session"""
        del self._session  # pylint: disable=no-member

    @cached_property
    def session_id(self):
        """session id, 前后台共用一个sid"""
        return self.get_secure_cookie("trade_sid")

    @cached_property
    def current_user(self):
        raise NotImplementedError

    @cached_property
    def orm_session(self):
        return sessionmaker(bind=get_engine())()

    def on_finish(self):
        if hasattr(self, "_orm_session"):
            self.orm_session.rollback()

    _ARG_DEFAULT = object()

    @cached_property
    def body_data(self):
        """用于angularjs"""
        try:
            return json.loads(self.request.body.decode())
        except ValueError:
            return {}

    def get_argument(self, name, default=_ARG_DEFAULT, strip=True):
        if name in self.body_data:
            return self.body_data[name]

        return super(BaseController, self).get_argument(name, default=default, strip=True)

    def write_error(self, status_code, **kwargs):
        if 'exc_info' in kwargs:
            exception = kwargs['exc_info'][1]
            if isinstance(exception, HTTPError) and status_code == 403:
                self.write(dict(ret=1, msg='forbidden'))
                self.set_status(403)
                return
        super().write_error(status_code, **kwargs)

    def log_exception(self, typ, value, tb):
        if isinstance(value, HTTPError) and value.status_code == 403:
            self.write(dict(ret=1, msg='forbidden'))
            self.set_status(403)
            self.finish()
        else:
            logging.error("Uncaught exception %s\n%r", self._request_summary(),
                          self.request, exc_info=(typ, value, tb))

    @classmethod
    def to_dict(cls, obj, attrs):
        res = {}
        for name in attrs:
            value = getattr(obj, name)
            res[name] = value if value is not None else ""
        return res

    def write(self, chunk):
        if isinstance(chunk, dict):
            chunk = json.dumps(chunk, default=str)
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        super().write(chunk)
