from app import app
import db
import api.user.register.table
import typing

@app.get("/api/user/login")
def new_user(email: str, password):
    return ''




