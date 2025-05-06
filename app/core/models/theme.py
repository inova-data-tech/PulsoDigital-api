from sqlalchemy import Column, Integer, String
from app.core.bootstrap.db import Base

class Theme(Base):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
