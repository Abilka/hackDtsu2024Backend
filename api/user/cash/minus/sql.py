import json

import fastapi

import db
import sqlalchemy
from api.user import table
from ...privileges.card import sql
from .obj import CashOperation
import api.user.cash.sql

class Database(db.Database):

    def minus(self, data: CashOperation, **kwargs):
        user_id = sql.Database().get_user_id_by_card(data.card_hash)

        user_balance = api.user.cash.sql.Database().get_balance_user(user_id)

        if user_balance - data.price < 0:
            content = {"result": {"message": 'Нет денег на данную операцию', "balance": user_balance}}
            return fastapi.Response(status_code=fastapi.status.HTTP_402_PAYMENT_REQUIRED)

        values = {}
        values.update({'user_id': user_id})
        values.update({'price': data.price})
        values.update({'reason': data.reason})
        values.update({'inn': data.inn})

        statement = sqlalchemy.insert(table.CashLog).values(values)
        self.connect.execute(statement)
        statement = sqlalchemy.update(table.User).where(table.User.id == user_id).values(cash=user_balance - data.price)
        self.connect.execute(statement)
        self.connect.commit()
        return {'result': {'balance': {'card_hash': data.card_hash, 'balance': user_balance - data.price}}}