from fastapi import APIRouter, Depends
from app.core.schemas.dashboard import DashboardCreate, DashboardUpdate, Dashboard
from app.api.dependencies import get_dashboard_service 
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/api/dashboards",
    tags=["Dashboards"]
)

@router.post("/", response_model=Dashboard)
def create_dashboard(dashboard: DashboardCreate, service: DashboardService = Depends(get_dashboard_service)):
    return service.create(dashboard)

@router.get("/", response_model=list[Dashboard])
def get_dashboards(service: DashboardService = Depends(get_dashboard_service)):
    return service.get_all()

@router.get("/{dashboard_id}", response_model=Dashboard)
def get_dashboard(dashboard_id: int, service: DashboardService = Depends(get_dashboard_service)):
    return service.get_by_id(dashboard_id)

@router.put("/{dashboard_id}", response_model=Dashboard)
def update_dashboard(dashboard_id: int, dashboard: DashboardUpdate, service: DashboardService = Depends(get_dashboard_service)):
    return service.update(dashboard_id, dashboard)

@router.delete("/{dashboard_id}", status_code=204)
def delete_dashboard(dashboard_id: int, service: DashboardService = Depends(get_dashboard_service)):
    service.delete(dashboard_id)
    return None