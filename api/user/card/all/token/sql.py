import api.user.sql
from ..obj import GetAllCard

import sqlalchemy

import db
from api.user import table
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session

class Database(db.Database):
    def select_by_token(self, **kwargs):
        user = api.user.sql.Database().get_by_token(kwargs['auth_hash'])
        statement = sqlalchemy.select(table.Card).where(table.Card.user_id == user.id)
        result = self.connect.execute(statement).fetchall()
        return list(map(lambda x: GetAllCard(x[0], x[2]), result))


