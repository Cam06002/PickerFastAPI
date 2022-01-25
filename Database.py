import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")

engine = create_engine('postgresql+psycopg2://postgres:6451Ducks!@localhost:5434/picker')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
