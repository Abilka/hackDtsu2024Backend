
from app import app
from .obj import CashOperation
from .sql import Database
import api.user.sql
@app.post("/api/user/cash/plus")
def cash_minus(data: CashOperation, auth_admin: str):
    if not api.user.sql.Database().get_admin_by_token(auth_admin):
        return {"result": 'Не авторизован'}
    return Database().plus(data)






