from ..obj import GetAllCard

import sqlalchemy

import db
from api.user import table
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session

class Database(db.Database):
    def select_by_user_id(self, **kwargs):
        statement = sqlalchemy.select(table.Card).where(table.Card.user_id == kwargs['user_id'])
        result = self.connect.execute(statement).fetchall()
        return list(map(lambda x: GetAllCard(x[1], x[2]), result))


