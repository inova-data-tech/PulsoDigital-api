from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.bootstrap.db import Base

class DataSource(Base):
    __tablename__ = 'data_sources'
    id = Column(Integer, primary_key=True, index=True)
    source_type = Column(String)
    sourceURL = Column(String)
    partial = Column(Boolean, default=False)
    topic_id = Column(Integer, ForeignKey('topics.id'))

    topic = relationship('Topic', back_populates='data_sources')
