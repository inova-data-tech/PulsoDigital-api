from app.core.models.data_source import DataSource
from app.repositories.data_source_repository import DataSourceRepository
from sqlalchemy.orm import Session

class DataSourceService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = DataSourceRepository(db)

    def create(self, data_source_create):
        return self.repository.create(data_source_create)
