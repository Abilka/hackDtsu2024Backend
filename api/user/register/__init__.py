from app import app
from api.user.register.sql import Database
import hashlib
@app.post("/api/user/register")
def new_user(username: str, password: str):
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    Database().new(username=username, password=password)
    return {"result": True}




