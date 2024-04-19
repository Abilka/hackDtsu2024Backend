from .obj import *

from app import app


@app.post("/api/user/privileges")
def new_privileges(data: obj.Privileges):
    pass



