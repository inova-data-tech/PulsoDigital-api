from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.schemas.dashboard import Dashboard
from app.db.session import get_db
from app.services import dashboard_service

router = APIRouter()

@router.post("/", response_model=Dashboard, tags=["Dashboards"])
def create_dashboard(dashboard: Dashboard, db: Session = Depends(get_db)):
    return dashboard_service.create_dashboard(db, dashboard)

@router.get("/", response_model=list[Dashboard], tags=["Dashboards"])
def get_dashboards(db: Session = Depends(get_db)):
    return dashboard_service.get_dashboards(db)

@router.get("/{dashboard_id}", response_model=Dashboard, tags=["Dashboards"])
def get_dashboard(dashboard_id: int, db: Session = Depends(get_db)):
    return dashboard_service.get_dashboard(db, dashboard_id)

@router.put("/{dashboard_id}", response_model=Dashboard, tags=["Dashboards"])
def update_dashboard(dashboard_id: int, dashboard: Dashboard, db: Session = Depends(get_db)):
    return dashboard_service.update_dashboard(db, dashboard_id, dashboard)

@router.delete("/{dashboard_id}", tags=["Dashboards"], status_code=204)
def delete_dashboard(dashboard_id: int, db: Session = Depends(get_db)):
    dashboard_service.delete_dashboard(db, dashboard_id)
