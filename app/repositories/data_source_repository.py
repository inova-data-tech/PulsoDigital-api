from app.core.models.data_source import DataSource
from sqlalchemy.orm import Session
from fastapi import HTTPException

class DataSourceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data_source_data: DataSource) -> DataSource:
        db_data_source = DataSource(
            source_type=data_source_data.source_type,
            sourceURL=data_source_data.sourceURL,
            biased=data_source_data.biased,
            topic_id=data_source_data.topic_id
        )
        self.db.add(db_data_source)
        self.db.commit()
        self.db.refresh(db_data_source)
        return db_data_source
    
    def get_all(self) -> list[DataSource]:
        return self.db.query(DataSource).all()
    
    def get_by_id(self, data_source_id: int) -> DataSource:
        db_data_source = self.db.query(DataSource).filter(DataSource.id == data_source_id).first()
        if not db_data_source:
            raise HTTPException(status_code=404, detail="Data source not found")
        return db_data_source
    
    def update(self, data_source_id: int, data_source_data: DataSource) -> DataSource:
        db_data_source = self.get_by_id(data_source_id)
        if not db_data_source:
            raise HTTPException(status_code=404, detail="Data source not found")
        
        db_data_source.source_type = data_source_data.source_type
        db_data_source.sourceURL = data_source_data.sourceURL
        db_data_source.biased = data_source_data.biased
        db_data_source.topic_id = data_source_data.topic_id
        
        self.db.commit()
        self.db.refresh(db_data_source)
        return db_data_source
    
    def delete(self, data_source_id: int) -> bool:
        db_data_source = self.get_by_id(data_source_id)
        if db_data_source:
            self.db.delete(db_data_source)
            self.db.commit()
            return True
        return False