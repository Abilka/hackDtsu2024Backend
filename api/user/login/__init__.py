from app import app
from api.user.login.sql import Database
from api.user.login import obj
import hashlib
from fastapi import HTTPException, status

@app.get("/api/user/login")
def new_user(username: str, password: str) -> obj.AnswerLogin:
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    result = Database().new_token(username=username, password=password)
    return obj.AnswerLogin(result)




