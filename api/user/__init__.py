from app import app
from api.user import register, login, card, privileges, admin, cash, me, username
from .sql import *
@app.get("/api/user", tags=['Пользователь'])
def get_all_user(auth_admin):
    return Database().select_all_user(auth_admin=auth_admin)


