import sqlalchemy.orm

import setting

Base = sqlalchemy.orm.declarative_base()

def create_base():
    engine = sqlalchemy.create_engine(setting.DATABASE_CONNECT)
    Base.metadata.create_all(engine)