from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.core.bootstrap.db import Base

class Dashboard(Base):
    __tablename__ = 'dashboards'
    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)
    status = Column(String, nullable=False, default='active')
    avg_rate = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    negative_rate = Column(Integer, nullable=False)
    neutral_rate = Column(Integer, nullable=False)
    positive_rate = Column(Integer, nullable=False)
    
    evaluations = relationship('DashboardEvaluation', back_populates='dashboard', cascade='all, delete-orphan')
    topic = relationship('Topic', back_populates='dashboards')
    
class DashboardEvaluation(Base):
    __tablename__ = 'dashboard_evaluations'
    id = Column(Integer, primary_key=True, index=True)
    dashboard_id = Column(Integer, ForeignKey('dashboards.id'), nullable=False)
    product_aspect = Column(String, nullable=False)
    date = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    
    dashboard = relationship('Dashboard', back_populates='evaluations')