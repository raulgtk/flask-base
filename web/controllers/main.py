# coding: utf-8

from flask import g
from flask import flash
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from lib.user import login_required

from ..blueprint import bp

@bp.route('/')
@login_required
def home():
    return render_template('layout.html')

@bp.route('/helloworld/')
@login_required
def hellolword():
    return render_template('layout.html')