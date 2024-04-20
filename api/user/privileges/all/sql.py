import db
import sqlalchemy

from .obj import Privileges
from api.user import table
class Database(db.Database):
    def get_all(self):
        statement = sqlalchemy.select(table.PrivilegesHistory)
        result = self.connect.execute(statement).fetchall()
        return list(map(lambda x: Privileges(*x), result))

