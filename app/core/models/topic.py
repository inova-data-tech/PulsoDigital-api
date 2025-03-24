from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    theme_id = Column(Integer, ForeignKey('themes.id'))

    theme = relationship('Theme', back_populates='topics')
