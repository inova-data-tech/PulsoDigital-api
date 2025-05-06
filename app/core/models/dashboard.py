from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from app.core.bootstrap.db import Base

class Dashboard(Base):
    __tablename__ = 'dashboards'
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)
    topic_id = Column(Integer, ForeignKey('topics.id'))
