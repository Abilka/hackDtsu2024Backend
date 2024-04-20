import db
from api.user import table
import sqlalchemy

class Database(db.Database):
    def get_balance_user(self, user_id: str):
        statement = sqlalchemy.select(table.User.cash).where(table.User.id == user_id)
        result = self.connect.execute(statement).fetchone()
        return result[-1]