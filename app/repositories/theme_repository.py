from app.core.models.theme import Theme
from sqlalchemy.orm import Session

class ThemeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, theme_create):
        db_theme = Theme(name=theme_create.name)
        self.db.add(db_theme)
        self.db.commit()
        self.db.refresh(db_theme)
        return db_theme
