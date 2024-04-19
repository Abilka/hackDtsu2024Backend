import datetime

import db
import sqlalchemy

class Auth(db.Base):
    __tablename__ = "Auth"

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer())
    access_token = sqlalchemy.Column(sqlalchemy.String(64))
    time_start = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    time_end = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now() + datetime.timedelta(days=2))

class User(db.Base):
    __tablename__ = "User"

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String(100), primary_key=True)
    password = sqlalchemy.Column(sqlalchemy.String(256))
    name = sqlalchemy.Column(sqlalchemy.String(256))
    family = sqlalchemy.Column(sqlalchemy.String(256))
    two_name = sqlalchemy.Column(sqlalchemy.String(256))

