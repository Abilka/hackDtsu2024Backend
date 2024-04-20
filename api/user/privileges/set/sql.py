import db
import sqlalchemy

from api.user import table
class Database(db.Database):

    def insert_privilege(self, **kwargs):
        if not self.select_prefix(kwargs['privileges_prefix']):
            return 'Неправильный префикс'
        statement = sqlalchemy.dialects.postgresql.insert(table.Privileges).values(kwargs)
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

