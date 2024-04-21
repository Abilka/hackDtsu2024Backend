import fastapi

from app import app

from .sql import *
from .obj import *
import hashlib
from fastapi import Response, status

@app.get("/api/user/login", tags=['Пользователь'])
def auth_user(username: str, password: str):
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    result = Database().new_token(username=username, password=password)
    return Response(status_code=status.HTTP_401_UNAUTHORIZED) if not result else obj.AnswerLogin(result)




