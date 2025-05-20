from sqlalchemy.orm import Session
from app.repositories.topic_repository import TopicRepository
from app.repositories.theme_repository import ThemeRepository
from app.core.schemas.topic import TopicCreate, TopicUpdate, Topic as TopicSchema
from fastapi import HTTPException
from typing import List, Optional


class TopicService:
    def __init__(self, repository: TopicRepository, theme_repository: ThemeRepository):
        self.theme_repository = theme_repository
        self.repository = repository

    def create(self, topic: TopicCreate) -> TopicSchema:
        db_topic = self.repository.create(topic)
        if db_topic is None:
            raise HTTPException(status_code=400, detail="Topic creation failed")
        db_topic.theme = self.theme_repository.get_by_id(db_topic.theme_id).name
        return TopicSchema.from_orm(db_topic)
    
    def get_all(self):
        db_topics = self.repository.get_all()
        for topic in db_topics:
            topic.theme = self.theme_repository.get_by_id(topic.theme_id).name
        return [TopicSchema.from_orm(topic) for topic in db_topics]
    
    def get_by_id(self, topic_id: int):
        topic = self.repository.get_by_id(topic_id)
        if topic is None:
            raise HTTPException(status_code=404, detail="Topic not found")
        topic.theme = self.theme_repository.get_by_id(topic.theme_id).name
        return TopicSchema.from_orm(topic)
    
    def update(self, topic_id: int, topic: TopicUpdate) -> TopicSchema:
        updated_topic = self.repository.update(topic_id, topic)
        if updated_topic is None:
            raise HTTPException(status_code=404, detail="Topic not found")
        return TopicSchema.from_orm(updated_topic)
    
    def delete(self, topic_id: int) -> None:
        success = self.repository.delete(topic_id)
        if not success:
            raise HTTPException(status_code=404, detail="Topic not found")