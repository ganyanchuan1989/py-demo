from peewee import *

database = MySQLDatabase('douyindb', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT',
                                        'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'gxz153759'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    name = CharField()
    sex = CharField()
    age = IntegerField(default=0)

    class Meta:
        table_name = 'com_person'
