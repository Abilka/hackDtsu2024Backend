from app import app
from api.user.card import all
from .sql import *

@app.get("/api/user/card")
def get_card(user_token: str):
    return ''

@app.post("/api/user/card")
def new_card(user_id: int):
    return Database().new_card(user_id=user_id)






