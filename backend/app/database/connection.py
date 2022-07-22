from email.policy import default
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time

POSTGRES_USER = config("POSTGRES_USER", cast=str ,default="postgres")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str,default="postgres")
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="postgres")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str ,default="localhost")
DATABASE_URL = config(
  "DATABASE_URL",
  default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
)


def wait_for_db(db_uri):
    """checks if database connection is established"""

    _local_engine = create_engine(db_uri)

    _LocalSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=_local_engine
    )

    up = False
    while not up:
        try:
            # Try to create session to check if DB is awake
            db_session = _LocalSessionLocal()
            # try some basic query
            db_session.execute("SELECT 1")
            db_session.commit()
        except Exception as err:
            print(f"Connection error: {err}")
            up = False
        else:
            up = True
        
        time.sleep(2)

wait_for_db(DATABASE_URL)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
