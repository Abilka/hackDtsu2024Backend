import db
from api.user import table
import sqlalchemy
import api.user.sql
from .obj import GetCategory
class Database(db.Database):
    def new(self, auth_admin: str, data: GetCategory):
        if not api.user.sql.Database().get_admin_by_token(auth_admin):
            return {"result": 'Не авторизован'}

        statement = sqlalchemy.dialects.postgresql.insert(table.ServiceCategory).values(data.__dict__)
        statement = statement.on_conflict_do_nothing()
        self.connect.execute(statement)
        self.connect.commit()
        self.connect.close()
        return {"result": True}