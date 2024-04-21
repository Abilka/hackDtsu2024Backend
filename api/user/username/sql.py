import api.user.login

import db
from api.user import table
import sqlalchemy.dialects.postgresql

class Database(db.Database):
    def get(self, username: str):
        statement = sqlalchemy.select(table.User.id).where(table.User.username == username)
        result = self.connect.execute(statement).fetchone()
        if result is not None:
            return True
        return result[-1]
