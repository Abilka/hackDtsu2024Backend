import fastapi

from app import app

from api.user.login.obj import AnswerLogin

from api.user.register.sql import Database

import hashlib
@app.post("/api/user/admin")
def new_user(username: str, password: str):
    if len(username) == 0 or len(password) == 0:
        return fastapi.Response(status_code=404)

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return Database().new(username=username, password=password)


@app.get("/api/user/admin")
def get_admin(username: str, password: str):
    if len(username) == 0 or len(password) == 0:
        return fastapi.Response(status_code=404)

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return Database().new(username=username, password=password)


