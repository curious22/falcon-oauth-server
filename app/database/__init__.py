# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app import log
from decouple import config

LOG = log.get_logger()


def get_engine(uri):
    LOG.info('Connecting to database..')
    options = {
        'pool_recycle': 3600,
        'pool_size': 10,
        'pool_timeout': 30,
        'max_overflow': 30,
        'echo': False,
        'execution_options': {
            'autocommit': True
        }
    }
    return create_engine(uri, **options)


db_session = scoped_session(sessionmaker())
engine = get_engine(config('DB_URI'))


def init_session():
    db_session.configure(bind=engine)

    from app.model import Base
    Base.metadata.create_all(engine)
