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
    cash =  sqlalchemy.Column(sqlalchemy.String(256))

class Card(db.Base):
    __tablename__ = "Card"

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    secret_key = sqlalchemy.Column(sqlalchemy.String(256))

class Privileges(db.Base):
    __tablename__ = "Privileges"

    user_id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    privileges_prefix = sqlalchemy.Column(sqlalchemy.String(16), primary_key=True)

class PrivilegesHistory(db.Base):
    __tablename__ = "PrivilegesHistory"

    privileges_prefix = sqlalchemy.Column(sqlalchemy.String(16), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(64))
    legend = sqlalchemy.Column(sqlalchemy.String(256))
    history = sqlalchemy.Column(sqlalchemy.String(256))


class AdminAccount(db.Base):
    __tablename__ = "AdminAccount"

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String(64), primary_key=True)
    password = sqlalchemy.Column(sqlalchemy.String(128))

class AdminAuth(db.Base):
    __tablename__ = "AdminAuth"

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer())
    access_token = sqlalchemy.Column(sqlalchemy.String(64))
    time_start = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    time_end = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now() + datetime.timedelta(days=2))

class LogInfo:
    __tablename__ = "LogInfo"

    user_id = sqlalchemy.Column(sqlalchemy.Integer())
    events = sqlalchemy.Column(sqlalchemy.String(256))
    timestamp = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())

class CashLog:
    __tablename__ = "CashLog"

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer())
    price = sqlalchemy.Column(sqlalchemy.Float())
    reason = sqlalchemy.Column(sqlalchemy.String(256))
    timestamp = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    okpo = sqlalchemy.Column(sqlalchemy.Integer())

