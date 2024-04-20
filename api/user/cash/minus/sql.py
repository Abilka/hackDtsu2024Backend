import db
import sqlalchemy
from api.user import table

class Database(db.Database):

    def minus(self, **kwargs):

        statement = sqlalchemy.insert(table.CashLog).values(kwargs)
