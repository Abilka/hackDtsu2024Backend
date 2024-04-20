from app import app

from .sql import *

@app.post("/api/user/privileges/set")
def get_card_privilege(user_id: str, privileges_prefix: str):
    result = sql.Database().insert_privilege(user_id=user_id, privileges_prefix=privileges_prefix)
    return {"result": result}


