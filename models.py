from database import Base
from sqlalchemy import Column , String , TIMESTAMP, Integer , Boolean, DateTime
from datetime import datetime

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100) , unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime,default= datetime.utcnow)