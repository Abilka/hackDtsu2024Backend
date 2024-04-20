import api.user.login

import db
from api.user import table
import sqlalchemy.dialects.postgresql

class Database(db.Database):
    def new(self, **kwargs):
        statement = sqlalchemy.dialects.postgresql.insert(table.User).values(kwargs)
        statement = statement.on_conflict_do_nothing()
        self.connect.execute(statement).fetchall()
        self.connect.commit()
        return api.user.login.auth_user(kwargs['username'], kwargs['password'])