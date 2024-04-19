import hashlib

import sqlalchemy

import api.user.card.obj
import db
from api.user import table
import api.user.sql
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session
import random
import string

def generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
class Database(db.Database):
    def new_card(self, **kwargs):

        user_id = api.user.sql.Database().get_by_token(kwargs['user_token']).id
        statement = sqlalchemy.dialects.postgresql.insert(table.Card).values(user_id=user_id).returning(table.Card.id)
        card_id = self.connect.execute(statement).fetchone()[-1]
        secret_key = hashlib.sha512(str(card_id).encode('utf-8') + str(user_id).encode('utf-8')).hexdigest()
        statement = sqlalchemy.update(table.Card).values(secret_key=secret_key).where(table.Card.id == card_id)
        self.connect.execute(statement)
        self.connect.commit()
        return api.user.card.obj.Card(secret_key)

