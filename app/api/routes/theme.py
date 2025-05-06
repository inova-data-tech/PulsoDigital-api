from fastapi import APIRouter, Depends
from typing import List
from app.core.schemas.theme import ThemeCreate, ThemeUpdate, Theme
from app.api.dependencies import get_theme_service
from app.services.theme_service import ThemeService

router = APIRouter(
    prefix="/api/themes",
    tags=["Themes"]
)

@router.post("/", response_model=Theme)
def create_theme(theme: ThemeCreate, service: ThemeService = Depends(get_theme_service)):
    return service.create(theme)

@router.get("/", response_model=List[Theme])
def get_themes(service: ThemeService = Depends(get_theme_service)):
    return service.get_all()

@router.get("/{theme_id}", response_model=Theme)
def get_theme(theme_id: int, service: ThemeService = Depends(get_theme_service)):
    return service.get_by_id(theme_id)

@router.put("/{theme_id}", response_model=Theme)
def update_theme(theme_id: int, theme: ThemeUpdate, service: ThemeService = Depends(get_theme_service)):
    return service.update(theme_id, theme)

@router.delete("/{theme_id}", status_code=204)
def delete_theme(theme_id: int, service: ThemeService = Depends(get_theme_service)):
    service.delete(theme_id)
    return None