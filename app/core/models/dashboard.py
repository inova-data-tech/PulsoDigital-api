from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.bootstrap.db import Base

class Dashboard(Base):
    __tablename__ = 'dashboards'
    id = Column(Integer, primary_key=True, index=True)
    product_aspect = Column(String, nullable=False)
    rate = Column(Integer, nullable=False)
    comment_date = Column(String, nullable=False)
    overview = Column(String, nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)
    
    topic = relationship('Topic', back_populates='dashboards')
    
