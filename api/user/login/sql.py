import sqlalchemy

import db
from api.user import table
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session


class Database(db.Database):
    def new_token(self, **kwargs):
        if not self.authorization(kwargs):
            return False
        statement = sqlalchemy.insert(table.User).values(kwargs).returning(table.Auth.id)
        statement = statement.on_conflict_do_nothing()
        self.connect.execute(statement).fetchall()
        self.connect.commit()

    def authorization(self, **kwargs) -> str or bool:
        statement = sqlalchemy.select(table.User.id).where(table.User.username == kwargs['username'] and
                                                           table.User.password == kwargs['password'])
        result = self.connect.execute(statement).fetchall()
        if len(result) > 0:
            return result[-1]
        return False
