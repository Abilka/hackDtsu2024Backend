from ..obj import GetAllCard

import sqlalchemy

import db
from api.user import table
import api.user.sql
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session

class Database(db.Database):
    def select_by_user_id(self, **kwargs):
        if not api.user.sql.Database().get_admin_by_token(kwargs['auth_admin']):
            return 'Не авторизован'
        statement = sqlalchemy.select(table.Card).where(table.Card.user_id == kwargs['user_id'])
        result = self.connect.execute(statement).fetchall()
        return list(map(lambda x: GetAllCard(x[1], x[2]), result))


