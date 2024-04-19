from app import app
import db
import api.user.register.table
import typing

@app.get("/api/user/card")
def new_user(user_token: str):
    return ''




