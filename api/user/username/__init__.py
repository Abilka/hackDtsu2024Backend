from app import app
from .sql import Database
import api.user.sql

@app.get("/api/user/username", tags=['Пользователь'])
def get_user_info(auth_admin: str, username: str):
    if not api.user.sql.Database().get_admin_by_token(auth_admin):
        return {'resut': 'Не авторизован'}
    return {'result': sql.Database().get(username)}
