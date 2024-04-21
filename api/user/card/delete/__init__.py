from app import app
from api.user.card import all
from .sql import *


@app.delete("/api/user/card/delete", tags=['Карты'])
def new_card(secret_key: str):
    return Database().delete(secret_key=secret_key)






