from typing import List, Optional
from sqlalchemy.orm import Session
from app.core.models.theme import Theme as ThemeModel
from app.core.schemas.theme import ThemeCreate, ThemeUpdate, Theme as ThemeSchema

class ThemeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, theme_data: ThemeCreate) -> ThemeModel:
        # Converter o schema para um dict e criar o modelo
        db_theme = ThemeModel(name=theme_data.name)
        self.db.add(db_theme)
        self.db.commit()
        self.db.refresh(db_theme)
        return db_theme
    
    def get_all(self) -> List[ThemeModel]:
        return self.db.query(ThemeModel).all()
    
    def get_by_id(self, theme_id: int) -> Optional[ThemeModel]:
        return self.db.query(ThemeModel).filter(ThemeModel.id == theme_id).first()

    def update(self, theme_id: int, theme_data: ThemeUpdate) -> Optional[ThemeModel]:
        db_theme = self.get_by_id(theme_id)
        if db_theme:
            db_theme.name = theme_data.name
            self.db.commit()
            self.db.refresh(db_theme)  # Corrigido: faltava o parâmetro
        return db_theme
    
    def delete(self, theme_id: int) -> bool:
        db_theme = self.get_by_id(theme_id)
        if db_theme:
            self.db.delete(db_theme)
            self.db.commit()
            return True
        return False