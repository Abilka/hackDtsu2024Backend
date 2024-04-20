import sqlalchemy
import api.user.card.obj
import db
from api.user import table
class Database(db.Database):
    def delete(self, secret_key):
        statement = sqlalchemy.delete(table.Card).where(table.Card.secret_key == secret_key)
        self.connect.execute(statement)
        self.connect.commit()

