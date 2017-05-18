# coding=utf-8

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class ORMBase(object):
    __table_args__ = dict(mysql_charset="utf8", )  # 默认utf-8, nullable=False
