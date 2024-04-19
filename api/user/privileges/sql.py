from app import app
import hashlib
from fastapi import HTTPException, status

@app.post("/api/privilegs")
def new_privileges(username: str, password: str):
    pass
    # return obj.AnswerLogin(result)




