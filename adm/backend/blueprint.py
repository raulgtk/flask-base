# conding: utf-8

from flask import Blueprint

bp = Blueprint('backend', __name__, template_folder='templates', static_folder='static', url_prefix='/admin')