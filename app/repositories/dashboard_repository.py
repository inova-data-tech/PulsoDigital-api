from typing import List
from sqlalchemy.orm import Session
from app.core.models.dashboard import Dashboard as DashboardModel
from app.core.models.topic import Topic as TopicModel
from app.core.schemas.dashboard import DashboardCreate, DashboardUpdate, Dashboard as DashboardSchema
from app.repositories.topic_repository import TopicRepository
from app.core.models.dashboard import DashboardEvaluation
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
            topic_id=dashboard_data.topic_id,
            status=dashboard_data.status,
            avg_rate=dashboard_data.avg_rate,
            category=dashboard_data.category,
            negative_rate=dashboard_data.negative_rate,
            neutral_rate=dashboard_data.neutral_rate,
            positive_rate=dashboard_data.positive_rate
        )
        self.db.add(db_dashboard)
        self.db.commit()
        self.db.refresh(db_dashboard)
        return db_dashboard
    
    def create_with_evaluations(self, dashboard_data: dict) -> DashboardModel:
        
        evaluations_data = dashboard_data.pop("evaluations", [])
        dashboard = DashboardModel(**dashboard_data)
        for eval_data in evaluations_data:
            evaluation = DashboardEvaluation(
                product_aspect=eval_data["product_aspect"],
                date=eval_data["rate_date"],
                rate=eval_data["rate"]
            )
            dashboard.evaluations.append(evaluation)
        self.db.add(dashboard)
        self.db.commit()
        self.db.refresh(dashboard)
        return dashboard
    
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

        db_dashboard.status = dashboard_data.status
        db_dashboard.avg_rate = dashboard_data.avg_rate
        db_dashboard.category = dashboard_data.category
        db_dashboard.negative_rate = dashboard_data.negative_rate
        db_dashboard.neutral_rate = dashboard_data.neutral_rate
        db_dashboard.positive_rate = dashboard_data.positive_rate

        db_dashboard.evaluations.clear()
        for eval_data in dashboard_data.evaluations:
            evaluation = DashboardEvaluation(
                product_aspect=eval_data.product_aspect,
                date=eval_data.rate_date,
                rate=eval_data.rate
            )
            db_dashboard.evaluations.append(evaluation)

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

    