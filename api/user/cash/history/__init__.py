
from app import app
from .sql import Database
@app.get("/api/user/cash/history")
def get_history(user_token: str):
    return Database().get(user_token)






