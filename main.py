import fastapi
import uvicorn

import setting
from app import app
import api
import db

@app.get("/")
def redirect():
    return fastapi.responses.RedirectResponse('/docs')

if __name__ == "__main__":
    db.create_base()

    uvicorn.run(app, host=setting.IP, port=setting.PORT)