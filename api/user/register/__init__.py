from app import app
import db
import api.user.register.table
import typing

@app.get("/api/user/register")
def new_user(name: str, password: str):
    return ''




