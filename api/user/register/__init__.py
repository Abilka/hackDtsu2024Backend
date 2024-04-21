import fastapi

from app import app

from api.user.login.obj import AnswerLogin
import api.user.login.sql

from api.user.register.sql import Database

import hashlib
@app.post("/api/user/register", tags=['Пользователь'])
def new_user(username: str, password: str, name: str, family: str, two_name: str):
    if len(username) == 0 or len(password) == 0 or len(name) == 0 or len(family) == 0:
        return fastapi.Response(status_code=404)

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    result = Database().new(username=username, password=password, name=name, family=family, two_name=two_name)
    if result:
        return AnswerLogin(api.user.login.sql.Database().new_token(username=username, password=password))
    return fastapi.Response(status_code=fastapi.status.HTTP_400_BAD_REQUEST)



