# coding: utf-8

import os

from flask import Flask

from conf.settings import STATIC_ROOT

project_dir = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))
static_root = os.path.join(project_dir, STATIC_ROOT)
app = Flask(__name__, static_folder=None, static_url_path='static')

# set configuration
app.config.from_object('conf.settings')
app.secret_key = app.config['SECRET_KEY']
app.debug = app.config['DEBUG']
app.project_dir = project_dir