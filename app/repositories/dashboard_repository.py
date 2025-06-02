from typing import List
from sqlalchemy.orm import Session
from app.core.models.dashboard import Dashboard as DashboardModel
from app.core.models.topic import Topic as TopicModel
from app.core.schemas.dashboard import DashboardCreate, DashboardUpdate, Dashboard as DashboardSchema
from app.repositories.topic_repository import TopicRepository
from app.repositories.dashboard_repository import DashboardRepository
from fastapi import HTTPException

class DashboardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dashboard_data: DashboardCreate) -> DashboardModel:
        # Verifica se o tópico existe
        topic_repo = TopicRepository(self.db)
        topic = topic_repo.get_by_id(dashboard_data.topic_id)
        if not topic:
            raise HTTPException(status_code=404, detail="Topic not found")

        # Cria o modelo de dashboard
        db_dashboard = DashboardModel(
            product_aspect=dashboard_data.product_aspect,
            rate=dashboard_data.rate,
            comment_date=dashboard_data.comment_date,
            overview=dashboard_data.overview,
            topic_id=dashboard_data.topic_id
        )
        self.db.add(db_dashboard)
        self.db.commit()
        self.db.refresh(db_dashboard)
        return db_dashboard
    
    def get_all(self) -> List[DashboardModel]:  
        return self.db.query(DashboardModel).all()
    
    def get_by_id(self, dashboard_id: int) -> DashboardModel:
        db_dashboard = self.db.query(DashboardModel).filter(DashboardModel.id == dashboard_id).first()
        if not db_dashboard:
            raise HTTPException(status_code=404, detail="Dashboard not found")
        return db_dashboard
    
    def update(self, dashboard_id: int, dashboard_data: DashboardUpdate) -> DashboardModel:
        db_dashboard = self.get_by_id(dashboard_id)
        if not db_dashboard:
            raise HTTPException(status_code=404, detail="Dashboard not found")
        
        db_dashboard.product_aspect = dashboard_data.product_aspect
        db_dashboard.rate = dashboard_data.rate
        db_dashboard.comment_date = dashboard_data.comment_date
        db_dashboard.overview = dashboard_data.overview
        db_dashboard.topic_id = dashboard_data.topic_id
        
        # Verifica se o tópico existe
        topic_repo = TopicRepository(self.db)
        topic = topic_repo.get_by_id(dashboard_data.topic_id)
        if not topic:
            raise HTTPException(status_code=404, detail="Topic not found")
        self.db.add(db_dashboard)   
        self.db.commit()
        self.db.refresh(db_dashboard)
        return db_dashboard
    
    def delete(self, dashboard_id: int) -> bool:
        db_dashboard = self.get_by_id(dashboard_id)
        if not db_dashboard:
            raise HTTPException(status_code=404, detail="Dashboard not found")
        
        self.db.delete(db_dashboard)
        self.db.commit()
        return True

    