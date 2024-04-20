from .obj import *
from .sql import Database
from app import app


@app.post("/api/user/privileges/new")
def new_privileges(data: obj.GetCategory, admin_auth):
    return sql.Database().new(auth_admin, data)



