import hashlib

import sqlalchemy

import db
from api.user import table
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm.session
import sqlalchemy
from .obj import AnswerLogin

class Database(db.Database):
    def new_token(self, **kwargs):
        user_data: table.AdminAccount = self.authorization(username=kwargs['username'], password=kwargs['password'])
        if not user_data:
            return False
        user_data.username = kwargs['username']
        user_data.password = kwargs['password']
        statement = sqlalchemy.insert(table.AdminAuth).values(user_id=user_data.id).returning(table.AdminAuth.id)
        token_id = self.connect.execute(statement).fetchone()[-1]
        access_token = hashlib.sha256(str(token_id).encode('utf-8') + user_data.password.encode('utf-8')).hexdigest()
        statement = sqlalchemy.update(table.AdminAuth).values(access_token=access_token).where(table.AdminAuth.id == token_id)
        self.connect.execute(statement)
        self.connect.commit()
        self.connect.close()
        return AnswerLogin(access_token)

    def authorization(self, **kwargs) -> str or bool:
        statement = sqlalchemy.select(table.AdminAccount.id).where(sqlalchemy.and_(table.AdminAccount.username == kwargs['username'],
                                                           table.AdminAccount.password == kwargs['password']))
        result = self.connect.execute(statement).fetchall()
        if len(result) > 0:
            return table.AdminAuth(id=result[-1][-1])
        return False
