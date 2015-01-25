# coding: utf-8

from lib.user import User

user_list = []

## admin
admin = User()
admin.username = u"Admin User"
admin.email = "admin@domain.com"
admin.password = "admin1234"
admin.active = False
user_list.append(admin)