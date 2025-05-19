from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.bootstrap.db import get_db
from app.repositories.theme_repository import ThemeRepository
from app.services.theme_service import ThemeService
from app.repositories.topic_repository import TopicRepository
from app.services.topic_service import TopicService
# Importe outros repositórios e serviços

def get_theme_repository(db: Session = Depends(get_db)) -> ThemeRepository:
    return ThemeRepository(db)

def get_theme_service(repo: ThemeRepository = Depends(get_theme_repository)) -> ThemeService:
    return ThemeService(repo)

def get_topic_repository(db: Session = Depends(get_db)) -> TopicRepository:
    return TopicRepository(db)

def get_topic_service(repo: TopicRepository = Depends(get_topic_repository)) -> TopicService:
    return TopicService(repo)