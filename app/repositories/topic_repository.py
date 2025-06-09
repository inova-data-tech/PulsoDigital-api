from typing import List, Optional
from sqlalchemy.orm import Session
from app.core.models.topic import Topic as TopicModel
from app.core.models.theme import Theme as ThemeModel
from app.core.schemas.topic import TopicCreate, TopicUpdate, Topic as TopicSchema



class TopicRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, topic_data: TopicCreate) -> TopicModel:
        # Converter o schema para um dict e criar o modelo
        db_topic = TopicModel(name=topic_data.name, theme_id=topic_data.theme_id)
        self.db.add(db_topic)
        self.db.commit()
        self.db.refresh(db_topic)
        return db_topic
    
    def get_all(self) -> List[TopicModel]:
        return self.db.query(TopicModel).all()
    
    def get_by_id(self, topic_id: int) -> Optional[TopicModel]:
        return self.db.query(TopicModel).filter(TopicModel.id == topic_id).first()
    
    def update(self, topic_id: int, topic_data: TopicUpdate) -> Optional[TopicModel]:   
        db_topic = self.get_by_id(topic_id)
        if db_topic:
            db_topic.name = topic_data.name
            db_topic.theme_id = topic_data.theme_id
            self.db.commit()
            self.db.refresh(db_topic)
        return db_topic
    
    def get_by_name(self, topic_name: str) -> Optional[TopicModel]:
        return self.db.query(TopicModel).filter(TopicModel.name == topic_name).first()
    
    def delete(self, topic_id: int) -> bool:
        db_topic = self.get_by_id(topic_id)
        if db_topic:
            self.db.delete(db_topic)
            self.db.commit()
            return True
        return False