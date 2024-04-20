from app import app
from api.user import register, login, card, privileges, admin
from .sql import *
@app.get("/api/user")
def get_all_user(auth_admin):
    return Database().select_all_user(auth_admin=auth_admin)


