import fastapi

from app import app

from api.user.login.obj import AnswerLogin

from api.user.register.sql import Database

import hashlib
@app.post("/api/user/register")
def new_user(username: str, password: str, name: str, family: str, two_name: str):
    if len(username) == 0 or len(password) == 0 or len(name) == 0 or len(family) == 0:
        return fastapi.Response(status_code=404)

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return Database().new(username=username, password=password, name=name, family=family, two_name=two_name)




