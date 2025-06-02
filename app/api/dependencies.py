from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.bootstrap.db import get_db
from app.repositories.theme_repository import ThemeRepository
from app.services.theme_service import ThemeService
from app.repositories.topic_repository import TopicRepository
from app.services.topic_service import TopicService
from app.repositories.dashboard_repository import DashboardRepository
from app.services.dashboard_service import DashboardService
from app.repositories.data_source_repository import DataSourceRepository
from app.services.data_source_service import DataSourceService

# Importe outros repositórios e serviços

def get_theme_repository(db: Session = Depends(get_db)) -> ThemeRepository:
    return ThemeRepository(db)

def get_theme_service(repo: ThemeRepository = Depends(get_theme_repository)) -> ThemeService:
    return ThemeService(repo)

def get_topic_repository(db: Session = Depends(get_db)) -> TopicRepository:
    return TopicRepository(db)

def get_topic_service(repo: TopicRepository = Depends(get_topic_repository), theme_repo: ThemeRepository = Depends(get_theme_repository)) -> TopicService:
    return TopicService(repo, theme_repo)

def get_data_source_repository(db: Session = Depends(get_db)) -> DataSourceRepository:
    return DataSourceRepository(db)

def get_data_source_service(repo: DataSourceRepository = Depends(lambda: DataSourceRepository(get_db())), topic_repo: TopicRepository = Depends(get_topic_repository)) -> DataSourceService:
    return DataSourceService(repo, topic_repo)

def get_dashboard_repository(db: Session = Depends(get_db)) -> DashboardRepository:
    return DashboardRepository(db)

def get_dashboard_service(repo: DashboardRepository = Depends(lambda: DashboardRepository(get_db())), topic_repo: TopicRepository = Depends(get_topic_repository)) -> DashboardService:
    return DashboardService(repo, topic_repo) 