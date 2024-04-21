from app import app

from .sql import *

@app.post("/api/user/privileges/set", tags=['Привилегии'])
def get_card_privilege(user_id: str, privileges_prefix: str, auth_admin: str):
    result = sql.Database().insert_privilege(user_id=user_id, privileges_prefix=privileges_prefix, auth_admin=auth_admin)
    return {"result": result}


