from app import app
from api.user.card.sql import Database
@app.get("/api/user/card")
def get_card(user_token: str):
    return ''

@app.post("/api/user/card")
def new_card(user_token: str):
    return Database().new_card(user_token=user_token)






