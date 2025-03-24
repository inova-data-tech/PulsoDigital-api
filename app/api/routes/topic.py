from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.schemas.topic import Topic
from app.db.session import get_db
from app.services import topic_service

router = APIRouter()

@router.post("/", response_model=Topic, tags=["Topics"])
def create_topic(topic: Topic, db: Session = Depends(get_db)):
    return topic_service.create_topic(db, topic)

@router.get("/", response_model=list[Topic], tags=["Topics"])
def get_topics(db: Session = Depends(get_db)):
    return topic_service.get_topics(db)

@router.get("/{topic_id}", response_model=Topic, tags=["Topics"])
def get_topic(topic_id: int, db: Session = Depends(get_db)):
    return topic_service.get_topic(db, topic_id)

@router.put("/{topic_id}", response_model=Topic, tags=["Topics"])
def update_topic(topic_id: int, topic: Topic, db: Session = Depends(get_db)):
    return topic_service.update_topic(db, topic_id, topic)

@router.delete("/{topic_id}", tags=["Topics"], status_code=204)
def delete_topic(topic_id: int, db: Session = Depends(get_db)):
    topic_service.delete_topic(db, topic_id)
