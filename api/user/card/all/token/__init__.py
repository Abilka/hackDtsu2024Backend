import typing

from app import app
from .sql import Database
from ..obj import GetAllCard
@app.get("/api/user/card/token", tags=['Карты'])
def select_by_token(auth_hash: str) -> typing.List[GetAllCard]:
    return Database().select_by_token(auth_hash=auth_hash)