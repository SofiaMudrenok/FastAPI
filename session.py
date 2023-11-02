from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

import os
import dotenv

dotenv.load_dotenv(".env")
host = os.environ.get("MYSQL_HOST")
user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
port = os.environ.get("MYSQL_PORT")
database = os.environ.get("MYSQL_DATABASE")

url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(
    url
)

sync_session = sessionmaker(bind=engine, class_=Session, expire_on_commit=False, )


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


def get_session() -> Session:
    db = sync_session()
    try:
        yield db
    finally:
        db.close()
