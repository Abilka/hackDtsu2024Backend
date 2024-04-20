import db
import sqlalchemy
from api.user import table
from .obj import CashOperation

class Database(db.Database):
    def get(self):
        pass