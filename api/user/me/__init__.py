import fastapi

from app import app

from .sql import *
from .obj import *

from fastapi import Response, status

@app.get("/api/user/me")
def get_user_info(auth_token: str):
    return sql.Database().get(auth_token)




