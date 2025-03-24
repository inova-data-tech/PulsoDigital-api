from app.core.models.data_source import DataSource
from sqlalchemy.orm import Session

class DataSourceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data_source_create):
        db_data_source = DataSource(
            source_type=data_source_create.source_type,
            sourceURL=data_source_create.sourceURL,
            partial=data_source_create.partial,
            topic_id=data_source_create.topic_id
        )
        self.db.add(db_data_source)
        self.db.commit()
        self.db.refresh(db_data_source)
        return db_data_source
