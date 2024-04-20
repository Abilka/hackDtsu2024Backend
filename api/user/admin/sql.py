import api.user.login

import db
from api.user import table
import sqlalchemy.dialects.postgresql
from .login import sql

class Database(db.Database):
    def new(self, **kwargs):
        statement = sqlalchemy.dialects.postgresql.insert(table.AdminAccount).values(kwargs)
        statement = statement.on_conflict_do_nothing()
        self.connect.execute(statement).fetchall()
        self.connect.commit()
        return sql.Database().new_token(username=kwargs['username'], password=kwargs['password'])