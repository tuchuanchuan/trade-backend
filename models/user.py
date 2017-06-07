# coding: utf-8
import uuid
import hashlib
import datetime

from sqlalchemy import Column, String, Integer, SMALLINT

from .base import ORMBase


class UserInterface(object):

    def verify(self, password):
        if self.forbidden:
            return False
        return self.hashed_password == hashlib.sha512(password.encode('utf-8') + self.password_salt.encode('utf-8')).hexdigest()

    def change_password(self, new_password):
        self.password_salt = uuid.uuid4().hex
        self.hashed_password = hashlib.sha512((new_password + self.password_salt).encode('utf-8')).hexdigest()

    @classmethod
    def login(cls, session, username, password):
        user = session.query(cls).filter_by(username=username).first()
        if user and user.verify(password):
            return user
        return None

    @classmethod
    def create_user(cls, username, password, **kwargs):
        """新建一个用户

        @param: username String generate a random username when None
        @param: password String generate a random password when None
        """
        user = cls(username=username, **kwargs)
        user.password_salt = uuid.uuid4().hex
        user.hashed_password = hashlib.sha512((password + user.password_salt).encode('utf-8')).hexdigest()
        return user


class Account(ORMBase, UserInterface):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, nullable=False, )

    username = Column(String(64), nullable=False, default='', unique=True, )
    nick = Column(String(32), nullable=False, default='', )
    hashed_password = Column(String(128), nullable=False, )  # hashed password
    password_salt = Column(String(64), nullable=False, )  # password salt
    forbidden = Column(SMALLINT, nullable=False, default=0)  # 是否被禁止
    last_login_ip = Column(String(128), nullable=False, default='', )  # 上次登录ip
    last_login_time = Column(Integer, nullable=False, default=0)  # 上次登录时间戳


class Admin(ORMBase, UserInterface):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, nullable=False, )

    username = Column(String(64), nullable=False, default='', unique=True, )
    hashed_password = Column(String(128), nullable=False, )  # hashed password
    password_salt = Column(String(64), nullable=False, )  # password salt
    level = Column(Integer, nullable=False, default=0, )  # 后台用户权限
    forbidden = Column(SMALLINT, nullable=False, default=0)  # 是否被禁止
    last_login_ip = Column(String(128), nullable=False, default='', )  # 上次登录ip
    last_login_time = Column(Integer, nullable=False, default=0)  # 上次登录时间戳
