from app.core.models.dashboard import Dashboard
from sqlalchemy.orm import Session

class DashboardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dashboard_create):
        db_dashboard = Dashboard(data=dashboard_create.data, topic_id=dashboard_create.topic_id)
        self.db.add(db_dashboard)
        self.db.commit()
        self.db.refresh(db_dashboard)
        return db_dashboard
