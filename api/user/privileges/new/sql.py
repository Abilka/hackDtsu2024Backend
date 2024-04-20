import db
import sqlalchemy

from api.user import table
class Database(db.Database):

    def get_privilege(self, card_hash: str):
        statement = sqlalchemy.dialects.postgresql.insert(table.PrivilegesHistory).values(data.__dict__)
        statement = statement.on_conflict_do_nothing()
        self.connect.execute(statement)
        self.connect.commit()

