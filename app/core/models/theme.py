from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Theme(Base):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
