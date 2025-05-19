from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.bootstrap.db import Base

class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    theme_id = Column(Integer, ForeignKey('themes.id'))
   