from app import app

@app.get("/api/user/card")
def get_card(user_token: str):
    return ''




