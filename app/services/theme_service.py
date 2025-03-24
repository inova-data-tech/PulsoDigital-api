from app.core.models.theme import Theme
from app.repositories.theme_repository import ThemeRepository
from sqlalchemy.orm import Session

class ThemeService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ThemeRepository(db)

    def create(self, theme_create):
        return self.repository.create(theme_create)
