# coding: utf-8

from .application import app
from .src import setup_packages
from .src import setup_main
from . import middleware
from . import context
from . import system

setup_packages(app)
setup_main(app)