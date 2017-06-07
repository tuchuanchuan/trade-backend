# coding: utf-8

from sqlalchemy.orm import sessionmaker
from tools.db import get_engine
from models.user import Admin

if __name__ == '__main__':
    session = sessionmaker(bind=get_engine())(autoflush=False)

    admin = Admin.create_user('tcc', '123123')
    session.add(admin)
    session.commit()
