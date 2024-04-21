import fastapi

from app import app

from .login import *

from .sql import *

import hashlib
@app.post("/api/user/admin", tags=['Администратор'])
def new_user(username: str, password: str):
    if len(username) == 0 or len(password) == 0:
        return fastapi.Response(status_code=404)

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return Database().new(username=username, password=password)

