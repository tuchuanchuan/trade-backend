# coding: utf-8
import redis

from sqlalchemy import create_engine, event, exc

import settings

_engine = None
_redis = None


def ping_connection(dbapi_connection, connection_record, connection_proxy):
    """检测mysql连接状态"""
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("SELECT 1")
    except exc.OperationalError as ex:
        import logging
        logging.warn("", exc_info=True)
        if ex.args[0] in (2006,  # MySQL server has gone away
                          2013,  # Lost connection to MySQL server during query
                          2055,  # Lost connection to MySQL server at '%s', system error: %d
                          ):
            raise exc.DisconnectionError()
        else:
            raise
    cursor.close()


def get_engine():
    global _engine
    if not _engine:
        _engine = create_engine(
            settings.DB_URL,
            echo=settings.DEBUG,
            echo_pool=True,
            pool_recycle=3600,
        )
        event.listen(_engine, "checkout", ping_connection)
    return _engine


def get_redis_connection():
    global _redis
    if not _redis:
        _redis = redis.Redis(connection_pool=redis.ConnectionPool(
            host=settings.REDIS_SETTINGS.get('HOST', '127.0.0.1'),
            port=settings.REDIS_SETTINGS.get('PORT', 6379),
            db=settings.REDIS_SETTINGS.get('db', 0),
            ))
    return _redis
