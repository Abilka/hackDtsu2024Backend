from .obj import *
from .sql import Database
from app import app


@app.post("/api/user/category/new", tags=['Деньги', "Категории"])
def create_new_category(data: obj.GetCategory, admin_auth):
    return sql.Database().new(admin_auth, data)



