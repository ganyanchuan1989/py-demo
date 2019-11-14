from peewee import *

database = MySQLDatabase('douyindb', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT',
                                        'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'gxz153759'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class ComDy(BaseModel):
    tags = CharField()
    user_id = CharField()
    user_url = CharField()
    v_url = CharField()
    v_size = IntegerField(default=0)

    class Meta:
        table_name = 'com_dy'
