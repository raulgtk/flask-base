# coding: utf-8

from wtforms import FieldList

class ModelFieldList(FieldList):

    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super(ModelFieldList, self).__init__(*args, **kwargs)
 
    def populate_obj(self, obj, name):
        if self.model:
            while len(getattr(obj, name)) < len(self.entries):
                getattr(obj, name).append(self.model())
        super(ModelFieldList, self).populate_obj(obj, name)