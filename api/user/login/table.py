import datetime

import db
import sqlalchemy

class Auth(db.Base):
    __tablename__ = "Auth"

    user_id = sqlalchemy.Column(sqlalchemy.Integer())
    access_token = sqlalchemy.Column(sqlalchemy.String(64))
    time_start = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    time_end = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now() + datetime.timedelta(days=2))