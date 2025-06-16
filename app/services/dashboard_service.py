from app.repositories.topic_repository import TopicRepository
from app.repositories.dashboard_repository import DashboardRepository
from app.core.schemas.dashboard import DashboardCreate, DashboardUpdate, Dashboard as DashboardSchema
from fastapi import HTTPException
from typing import List, Optional


class DashboardService:
    def __init__(self, repository: DashboardRepository, topic_repository: TopicRepository):
        self.topic_repository = topic_repository
        self.repository = repository

    def create(self, dashboard: DashboardCreate) -> DashboardSchema:
        db_dashboard = self.repository.create(dashboard)
        if db_dashboard is None:
            raise HTTPException(status_code=400, detail="Dashboard creation failed")
        db_dashboard.topic = self.topic_repository.get_by_id(db_dashboard.topic_id).name
        return DashboardSchema.from_orm(db_dashboard)
    
    def create_with_evaluations(self, dashboard_data: dict) -> DashboardSchema:
        db_dashboard = self.repository.create_with_evaluations(dashboard_data)
        if db_dashboard is None:
            raise HTTPException(status_code=400, detail="Dashboard creation with evaluations failed")
        return DashboardSchema.from_orm(db_dashboard)

    
    def get_all(self) -> List[DashboardSchema]:
        db_dashboards = self.repository.get_all()
        for dashboard in db_dashboards:
            dashboard.topic = self.topic_repository.get_by_id(dashboard.topic_id).id
        return [DashboardSchema.from_orm(dashboard) for dashboard in db_dashboards]
    
    def get_by_id(self, dashboard_id: int) -> DashboardSchema:
        dashboard = self.repository.get_by_id(dashboard_id)
        if dashboard is None:
            raise HTTPException(status_code=404, detail="Dashboard not found")
        dashboard.topic = self.topic_repository.get_by_id(dashboard.topic_id).id
        return DashboardSchema.from_orm(dashboard)
    
    def update(self, dashboard_id: int, dashboard: DashboardUpdate) -> DashboardSchema:
        updated_dashboard = self.repository.update(dashboard_id, dashboard)
        if updated_dashboard is None:
            raise HTTPException(status_code=404, detail="Dashboard not found")
        return DashboardSchema.from_orm(updated_dashboard)
    
    def delete(self, dashboard_id: int) -> None:
        success = self.repository.delete(dashboard_id)
        if not success:
            raise HTTPException(status_code=404, detail="Dashboard not found")
   

    