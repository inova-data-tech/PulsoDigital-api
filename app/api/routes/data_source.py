from fastapi import APIRouter, Depends
from app.core.schemas.data_source import DataSourceCreate, DataSourceUpdate,DataSource
from app.repositories.data_source_repository import DataSourceRepository
from app.api.dependencies import get_data_source_service, get_dashboard_repository
from app.services.data_source_service import DataSourceService

router = APIRouter(
    prefix="/api/data_sources",
    tags=["Data Sources"]
)

@router.post("/", response_model=DataSource)
def create_data_source(data_source: DataSourceCreate, service: DataSourceService = Depends(get_data_source_service)):
    return service.create(data_source)

@router.get("/", response_model=list[DataSource])
def get_data_sources(service: DataSourceService = Depends(get_data_source_service)):
    return service.get_all()

@router.get("/{data_source_id}", response_model=DataSource)
def get_data_source(data_source_id: int, service: DataSourceService = Depends(get_data_source_service)):
    return service.get_by_id(data_source_id)

@router.put("/{data_source_id}", response_model=DataSource)
def update_data_source(data_source_id: int, data_source: DataSourceUpdate, service: DataSourceService = Depends(get_data_source_service)):
    return service.update(data_source_id, data_source)

@router.delete("/{data_source_id}", status_code=204)
def delete_data_source(data_source_id: int, service: DataSourceService = Depends(get_data_source_service)):
    service.delete(data_source_id)
    return None