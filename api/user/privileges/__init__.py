from app import app

from .all import *
from .new import *

@app.get("/api/user/privileges/card")
def get_card_privilege(data: obj.Privileges):
    sql.Database().new_privileges(data)


