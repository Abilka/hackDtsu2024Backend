import typing

from app import app
from .sql import Database
from ..obj import GetAllCard
@app.get("/api/user/card/id")
def select_by_user_id(user_id: int) -> typing.List[GetAllCard]:
    return Database().select_by_user_id(user_id=user_id)