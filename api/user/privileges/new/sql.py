import db
import sqlalchemy
from .obj import Privileges

from api.user import table
import api.user.sql

class Database(db.Database):

    def new_privileges(self, data: Privileges, **kwargs):
        if not api.user.sql.Database().get_admin_by_token(kwargs['auth_admin']):
            return 'Не авторизован'
        statement = sqlalchemy.dialects.postgresql.insert(table.PrivilegesHistory).values(data.__dict__)
        statement = statement.on_conflict_do_nothing()
        self.connect.execute(statement)
        self.connect.commit()
        return data

