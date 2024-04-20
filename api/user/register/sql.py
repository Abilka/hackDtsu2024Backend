import api.user.login

import db
from api.user import table
import sqlalchemy.dialects.postgresql

class Database(db.Database):
    def new(self, **kwargs):
        if self.user_is_instance(kwargs['username']):
            return False
        statement = sqlalchemy.dialects.postgresql.insert(table.User).values(kwargs)
        statement = statement.on_conflict_do_nothing()
        self.connect.execute(statement).fetchall()
        self.connect.commit()
        # return api.user.login.auth_user(kwargs['username'], kwargs['password'])
        return True

    def user_is_instance(self, username: str):
        statement = sqlalchemy.select(table.User).where(table.User.username == username)
        result = self.connect.execute(statement).fetchone()
        if result is not None:
            return True
        return False
