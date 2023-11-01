from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'postgresql://postgres:surya@localhost'

engine = create_engine(DB_URL)
session = Session(engine)
Base = declarative_base()