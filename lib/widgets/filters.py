# coding: utf-8

from init import app
from datetime import timedelta

@app.template_filter()
def datetime_format(date):
    return date.strftime('%d/%m/%Y %H:%M')

@app.template_filter()
def date_format(date):
    return date.strftime('%d/%m/%Y')

@app.template_filter()
def month_format(date):
    return date.strftime('%B %Y')

@app.template_filter()
def time_format(date):
    return date.strftime('%H:%M')

@app.template_filter()
def apply_tax(subtotal, tax):
    return subtotal * tax / 100
