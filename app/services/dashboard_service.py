from app.core.models.dashboard import Dashboard
from app.repositories.dashboard_repository import DashboardRepository
from sqlalchemy.orm import Session

class DashboardService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = DashboardRepository(db)

    def create(self, dashboard_create):
        return self.repository.create(dashboard_create)
