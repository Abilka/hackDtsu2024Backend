from .obj import *
from .sql import Database
from app import app


@app.get("/api/user/privileges/all", tags=['Привилегии'])
def get_all_privileges():
    return sql.Database().get_all()



