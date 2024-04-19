from app import app

from api.user.login.obj import AnswerLogin

from api.user.register.sql import Database

import hashlib
@app.post("/api/user/register")
def new_user(username: str, password: str, name: str, family: str, two_name: str) -> AnswerLogin:
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return Database().new(username=username, password=password)




