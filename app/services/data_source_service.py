from app.core.models.data_source import DataSource
from app.repositories.topic_repository import TopicRepository
from app.repositories.data_source_repository import DataSourceRepository
from app.core.schemas.data_source import DataSourceCreate, DataSourceUpdate, DataSource as DataSourceSchema
from fastapi import HTTPException
from sqlalchemy.orm import Session

class DataSourceService:
    def __init__(self, repostitory: DataSourceRepository, topic_repository: TopicRepository):
        self.topic_repository = topic_repository
        self.repository = repostitory
    
    def create(self, data_source: DataSourceCreate) -> DataSourceSchema:
        db_data_source = self.repository.create(data_source)
        if db_data_source is None:
            raise HTTPException(status_code=400, detail="Failed to create data source")
        # Convertendo o modelo para schema
        db_data_source.topic = self.topic_repository.get_by_id(db_data_source.topic_id).name
        return DataSourceSchema.from_orm(db_data_source)
    
    def get_all(self) -> list[DataSourceSchema]:
        db_data_sources = self.repository.get_all()
        for data_source in db_data_sources:
            data_source.topic = self.topic_repository.get_by_id(data_source.topic_id).name
        return [DataSourceSchema.from_orm(data_source) for data_source in db_data_sources]
    
    def get_by_id(self, data_source_id: int) -> DataSourceSchema:
        data_source = self.repository.get_by_id(data_source_id)
        if data_source is None:
            raise HTTPException(status_code=404, detail="Data source not found")
        data_source.topic = self.topic_repository.get_by_id(data_source.topic_id).name
        return DataSourceSchema.from_orm(data_source)
    
    def update(self, data_source_id: int, data_source: DataSourceUpdate) -> DataSourceSchema:
        updated_data_source = self.repository.update(data_source_id, data_source)
        if updated_data_source is None:
            raise HTTPException(status_code=404, detail="Data source not found")
        return DataSourceSchema.from_orm(updated_data_source)
    
    def delete(self, data_source_id: int) -> None:
        success = self.repository.delete(data_source_id)
        if not success:
            raise HTTPException(status_code=404, detail="Data source not found")