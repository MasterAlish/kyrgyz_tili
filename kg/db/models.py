from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('db.sqlite3')


class BaseModel(Model):
    class Meta:
        database = db


class Word(BaseModel):
    word = TextField()
    alt = TextField(null=True)
    type = IntegerField()
