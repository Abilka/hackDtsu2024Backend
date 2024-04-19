import db
import sqlalchemy

class User(db.Base):
    __tablename__ = "User"

    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(100), primary_key=True)
    password = sqlalchemy.Column(sqlalchemy.String(256))