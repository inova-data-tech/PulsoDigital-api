from app.core.models.topic import Topic
from app.repositories.topic_repository import TopicRepository
from sqlalchemy.orm import Session

class TopicService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = TopicRepository(db)

    def create(self, topic_create):
        return self.repository.create(topic_create)
