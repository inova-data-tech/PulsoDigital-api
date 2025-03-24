from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.schemas.data_source import DataSource
from app.db.session import get_db
from app.services import data_source_service

router = APIRouter()

@router.post("/", response_model=DataSource, tags=["DataSources"])
def create_data_source(data_source: DataSource, db: Session = Depends(get_db)):
    return data_source_service.create_data_source(db, data_source)

@router.get("/", response_model=list[DataSource], tags=["DataSources"])
def get_data_sources(db: Session = Depends(get_db)):
    return data_source_service.get_data_sources(db)

@router.get("/{data_source_id}", response_model=DataSource, tags=["DataSources"])
def get_data_source(data_source_id: int, db: Session = Depends(get_db)):
    return data_source_service.get_data_source(db, data_source_id)

@router.put("/{data_source_id}", response_model=DataSource, tags=["DataSources"])
def update_data_source(data_source_id: int, data_source: DataSource, db: Session = Depends(get_db)):
    return data_source_service.update_data_source(db, data_source_id, data_source)

@router.delete("/{data_source_id}", tags=["DataSources"], status_code=204)
def delete_data_source(data_source_id: int, db: Session = Depends(get_db)):
    data_source_service.delete_data_source(db, data_source_id)
