import db
from api.user import table
import sqlalchemy
from .obj import GetCategory
class Database(db.Database):
    def get(self):
        statement = sqlalchemy.select(table.ServiceCategory)
        result = self.connect.execute(statement).fetchall()
        return list(map(lambda x: GetCategory(*x), result))