
from app import app
from .obj import CashOperation
from .sql import Database
@app.post("/api/user/cash/minus")
def cash_minus(data: CashOperation):
    return Database().minus(data)






