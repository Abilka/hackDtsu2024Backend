from app import app

from ..obj import Privileges
from .sql import *

@app.get("/api/user/privileges/card", tags=['Привилегии'])
def get_card_privilege(card_hash: str):
    return {"result": sql.Database().get_privilege(card_hash=card_hash)}


