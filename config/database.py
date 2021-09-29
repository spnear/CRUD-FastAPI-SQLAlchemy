from config.config import DATABASE, PASSWORD, USER
from sqlalchemy import create_engine, MetaData
from .config import USER, PASSWORD, PORT, DATABASE

database_route = f'mysql+pymysql://{USER}:{PASSWORD}@localhost:{PORT}/{DATABASE}'

engine = create_engine(database_route)

meta = MetaData()

conn = engine.connect()