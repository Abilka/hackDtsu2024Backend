from .obj import *
from .sql import Database
from app import app


@app.get("/api/user/category/all")
def get_category_all():
    return sql.Database().get()



