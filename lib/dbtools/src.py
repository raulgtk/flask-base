# coding: utf-8

from sqlalchemy.engine import reflection
from sqlalchemy import create_engine

from .models.db import engine  # noqa
from .models.db import session  # noqa
from .models.db import Model  # noqa

def db_add(instance):
    session.add(instance)

def db_flush():
    session.flush()

def db_commit():
    session.commit()

def db_delete(instance):
    session.delete(instance)

def create_all():
    Model.metadata.create_all(bind=engine)

