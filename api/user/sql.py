import db
import sqlalchemy
from api.user import table
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session
from .obj import ReturnUser

class Database(db.Database):
    def get_by_token(self, token: str):
        statement = sqlalchemy.select(table.Auth.user_id).where(table.Auth.access_token == token)
        result = self.connect.execute(statement).fetchone()
        if result is not None:
            return table.User(id=result[-1])
        return False

    def get_admin_by_token(self, token: str):
        statement = sqlalchemy.select(table.AdminAuth.user_id).where(table.AdminAuth.access_token == token)
        result = self.connect.execute(statement).fetchone()
        if result is not None:
            return table.AdminAccount(id=result[-1])
        return False


    def select_all_user(self):
        statement = sqlalchemy.select(table.User.id, table.User.username)
        result = self.connect.execute(statement).fetchall()
        return list(map(lambda x: ReturnUser(*x), result))