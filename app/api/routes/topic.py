from fastapi import APIRouter, Depends
from app.core.schemas.topic import TopicCreate, TopicUpdate, Topic
from app.api.dependencies import get_topic_service
from app.services.topic_service import TopicService

router = APIRouter(
    prefix="/api/topics",
    tags=["Topics"]
)

@router.post("/", response_model=Topic)
def create_topic(topic: TopicCreate, service: TopicService = Depends(get_topic_service)):
    return service.create(topic)

@router.get("/", response_model=list[Topic])
def get_topics(service: TopicService = Depends(get_topic_service)):
    return service.get_all()

@router.get("/{topic_id}", response_model=Topic)
def get_topic(topic_id: int, service: TopicService = Depends(get_topic_service)):
    return service.get_by_id(topic_id)

@router.put("/{topic_id}", response_model=Topic)
def update_topic(topic_id: int, topic: TopicUpdate, service: TopicService = Depends(get_topic_service)):
    return service.update(topic_id, topic)

@router.delete("/{topic_id}", status_code=204)
def delete_topic(topic_id: int, service: TopicService = Depends(get_topic_service)):
    service.delete(topic_id)
    return None