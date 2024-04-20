from app import app
from api.user.card import all
from .sql import *


@app.delete("/api/user/card/delete")
def new_card(card_id: int):
    return Database().delete(card_id=card_id)






