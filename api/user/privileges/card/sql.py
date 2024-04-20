import db
import sqlalchemy

from api.user import table
class Database(db.Database):

    def get_privilege(self, card_hash: str):
        user_id = self.get_user_id_by_card(card_hash)
        if not user_id:
            return "Нет такой карты"

        return self.get_privileges_by_user_id(user_id)

    def get_user_id_by_card(self, card_hash: str):
        statement = sqlalchemy.select(table.Card.user_id).where(table.Card.secret_key == card_hash)
        result = self.connect.execute(statement).fetchone()
        if result is None:
            return False
        return result[-1]

    def get_privileges_by_user_id(self, user_id: int):
        statement = sqlalchemy.select(table.Privileges.privileges_prefix).where(table.Privileges.user_id == user_id)
        result = self.connect.execute(statement).fetchall()
        return list(map(lambda x: x[-1], result))


