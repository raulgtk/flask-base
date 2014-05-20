# coding: utf-8

import os

from fabric.api import task
from fabric.api import local
from fabric.api import settings
from fabric.utils import abort
from fabric.operations import prompt
from fabric.contrib.console import confirm

from init import app
from lib.dbtools import create_all

@task
def run(host=None):
    """ Run development server """

    if host:
        app.host = host
    app.run()

@task
def db_reset():
    if not app.debug:
        abort("Database cannot be reset when in production mode (ie. DEBUG = False)")

    print "The database contents will be deleted."
    if confirm("Are you sure?"):
        print "Resetting database..."
        create_all()