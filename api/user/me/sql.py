import hashlib

import sqlalchemy
import db
from api.user import table
import api.user.sql
from .obj import ReturnUser
class Database(db.Database):
    def get(self, token: str):
        user = api.user.sql.Database().get_by_token(token)
        user_id = user.id
        statement = sqlalchemy.select(table.User.username,
                                      table.User.name,
                                      table.User.family,
                                      table.User.two_name,
                                      table.User.cash).where(table.User.id == user_id)
        result = self.connect.execute(statement).fetchone()
        return {'result': ReturnUser(*result)}