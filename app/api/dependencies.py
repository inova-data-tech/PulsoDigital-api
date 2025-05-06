from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.bootstrap.db import get_db
from app.repositories.theme_repository import ThemeRepository
from app.services.theme_service import ThemeService
# Importe outros repositórios e serviços

def get_theme_repository(db: Session = Depends(get_db)) -> ThemeRepository:
    return ThemeRepository(db)

def get_theme_service(repo: ThemeRepository = Depends(get_theme_repository)) -> ThemeService:
    return ThemeService(repo)