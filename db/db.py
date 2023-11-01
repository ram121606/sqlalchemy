from sqlalchemy import Column, Integer, String
from .db_con import Base

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer , primary_key = True , nullable = False)
    name = Column(String , nullable = False)
    password = Column(String , nullable = False)