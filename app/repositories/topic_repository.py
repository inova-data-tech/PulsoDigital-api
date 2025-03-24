from app.core.models.topic import Topic
from sqlalchemy.orm import Session

class TopicRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, topic_create):
        db_topic = Topic(name=topic_create.name, theme_id=topic_create.theme_id)
        self.db.add(db_topic)
        self.db.commit()
        self.db.refresh(db_topic)
        return db_topic
