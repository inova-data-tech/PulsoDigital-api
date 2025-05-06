from typing import List, Optional
from fastapi import HTTPException
from app.core.schemas.theme import ThemeCreate, ThemeUpdate, Theme as ThemeSchema
from app.repositories.theme_repository import ThemeRepository
from sqlalchemy.orm import Session

class ThemeService:
    def __init__(self, repository: ThemeRepository):
        self.repository = repository
    
    def create(self, theme: ThemeCreate) -> ThemeSchema:
        db_theme = self.repository.create(theme)
        # Convertendo o modelo para schema
        return ThemeSchema.from_orm(db_theme)
    
    def get_all(self) -> List[ThemeSchema]:
        db_themes = self.repository.get_all()
        # Convertendo lista de modelos para schemas
        return [ThemeSchema.from_orm(theme) for theme in db_themes]
    
    def get_by_id(self, theme_id: int) -> ThemeSchema:
        theme = self.repository.get_by_id(theme_id)
        if theme is None:
            raise HTTPException(status_code=404, detail="Theme not found")
        return ThemeSchema.from_orm(theme)
    
    def update(self, theme_id: int, theme: ThemeUpdate) -> ThemeSchema:
        updated_theme = self.repository.update(theme_id, theme)
        if updated_theme is None:
            raise HTTPException(status_code=404, detail="Theme not found")
        return ThemeSchema.from_orm(updated_theme)
    
    def delete(self, theme_id: int) -> None:
        success = self.repository.delete(theme_id)
        if not success:
            raise HTTPException(status_code=404, detail="Theme not found")