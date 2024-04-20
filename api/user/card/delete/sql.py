import sqlalchemy
import api.user.card.obj
import db
from api.user import table
class Database(db.Database):
    def delete(self, card_id):
        statement = sqlalchemy.delete(table.Card).where(table.Card.id == card_id)
        self.connect.execute(statement)
        self.connect.commit()

