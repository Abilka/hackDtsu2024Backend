import sqlalchemy.orm

import setting

Base = sqlalchemy.orm.declarative_base()
class Database:
    def __init__(self):
        self.engine = sqlalchemy.create_engine(setting.DATABASE_CONNECT)
        self.connect = self.engine.connect()

def create_base():
    engine = sqlalchemy.create_engine(setting.DATABASE_CONNECT)
    Base.metadata.create_all(engine)