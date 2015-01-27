# conding: utf-8

from flask import Blueprint

bp = Blueprint('lib.static', __name__, static_folder='static')