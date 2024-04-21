from .obj import *
from .sql import Database
from app import app


@app.post("/api/user/privileges/new", tags=['Привилегии'])
def new_privileges(data: obj.Privileges, auth_admin):
    return sql.Database().new_privileges(data, auth_admin=auth_admin)



