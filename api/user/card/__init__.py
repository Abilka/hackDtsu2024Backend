from app import app
from api.user.card import all, delete
from .sql import *


@app.post("/api/user/card")
def new_card(user_id: int):
    return Database().new_card(user_id=user_id)






