import db
import sqlalchemy

from api.user import table
import api.user.sql

class Database(db.Database):

    def insert_privilege(self, **kwargs):
        if not self.select_prefix(kwargs['privileges_prefix']):
            return 'Неправильный префикс'

        if not self.user_is_instance(kwargs['user_id']):
            return 'Такого пользователя не существует'

        if not api.user.sql.Database().get_admin_by_token(kwargs['auth_admin']):
            return 'Не авторизован'

        statement = sqlalchemy.dialects.postgresql.insert(table.Privileges).values(user_id=kwargs['user_id'],
                                                                                   privileges_prefix=kwargs['privileges_prefix'])
        statement = statement.on_conflict_do_nothing()
        self.connect.execute(statement)
        self.connect.commit()
        return True

    def select_prefix(self, prefix):
        statement = sqlalchemy.select(table.PrivilegesHistory.privileges_prefix).where(table.PrivilegesHistory.privileges_prefix == prefix)
        result = self.connect.execute(statement).fetchone()
        if result is None:
            return False
        return True

    def user_is_instance(self, user_id: int):
        statement = sqlalchemy.select(table.User.id).where(table.User.id == user_id)
        result = self.connect.execute(statement).fetchone()
        return False if result is None else True

