import db
import sqlalchemy
from api.user import table
from .obj import CashOperation
import api.user.sql
class Database(db.Database):
    def get(self, token: str):
        user_id = api.user.sql.Database().get_by_token(token)
        user_id = user_id.id
        statement = sqlalchemy.select(table.CashLog.timestamp, table.CashLog.price, table.CashLog.reason, table.CashLog.inn, table.CashLog.category_id).where(table.CashLog.user_id == user_id)
        result = self.connect.execute(statement).fetchall()
        cash_list = list(map(lambda x: CashOperation(*x), result))
        return sorted(cash_list, key=lambda x: x.date, reverse=True)