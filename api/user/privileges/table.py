import db
import sqlalchemy

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