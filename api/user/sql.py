import db
import sqlalchemy
from api.user import table
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session

class Database(db.Database):
    def get_by_token(self, token: str):
        statement = sqlalchemy.select(table.Auth.user_id).where(table.Auth.access_token == token)
        result = self.connect.execute(statement).fetchone()
        return table.User(id=result[-1])

