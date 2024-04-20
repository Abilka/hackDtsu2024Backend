from app import app
from api.user import register, login, card, privileges
from .sql import *
@app.get("/api/user")
def get_all_user():
    return Database().select_all_user()


