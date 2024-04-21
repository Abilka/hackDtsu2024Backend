import typing

from app import app
from .sql import Database
from ..obj import GetAllCard
@app.get("/api/user/card/id", tags=['Карты'])
def select_by_user_id(user_id: int, auth_admin: str):
    return {"result": Database().select_by_user_id(user_id=user_id, auth_admin=auth_admin)}
