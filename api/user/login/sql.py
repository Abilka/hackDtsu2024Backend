import hashlib

import sqlalchemy

import db
from api.user import table
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session


class Database(db.Database):
    def new_token(self, **kwargs):
        user_data: table.User = self.authorization(username=kwargs['username'], password=kwargs['password'])
        if not user_data:
            return False
        user_data.username = kwargs['username']
        user_data.password = kwargs['password']
        statement = sqlalchemy.insert(table.Auth).values(user_id=user_data.id).returning(table.Auth.id)
        token_id = self.connect.execute(statement).fetchone()[-1]
        access_token = hashlib.sha256(str(token_id).encode('utf-8') + user_data.password.encode('utf-8')).hexdigest()
        statement = sqlalchemy.update(table.Auth).values(access_token=access_token).where(table.Auth.id == token_id)
        self.connect.execute(statement)
        self.connect.commit()
        return access_token

    def authorization(self, **kwargs) -> str or bool:
        statement = sqlalchemy.select(table.User.id).where(table.User.username == kwargs['username'],
                                                           table.User.password == kwargs['password'])
        result = self.connect.execute(statement).fetchall()
        if len(result) > 0:
            return table.User(id=result[-1][-1])
        return False
