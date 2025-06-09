from fastapi import APIRouter, Depends, HTTPException, Request
from app.core.schemas.topic import TopicCreate, TopicUpdate, Topic
from app.api.dependencies import get_topic_service
from app.services.topic_service import TopicService
import httpx


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

@router.post("/{topiuc_name}/trigger-task")
async def trigger_task_for_topic(
    topic_name: str,
    request: Request,
    service: TopicService = Depends(get_topic_service)
    ):
    
    topic = service.get_by_name(topic_name)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")


    base_url = str(request.base_url).rstrip("/")

    webhook_url = f"{base_url}/api/webhook/task-result"

    payload = {
        "topic": topic_name,
        "webhook": webhook_url
    }
    async with httpx.AsyncClient() as client:
        response = await client.post("URL_DA_API_TERCEIRA", json=payload)
        response.raise_for_status()
        return {
            "message": "Task triggered",
            "webhook": webhook_url,
            "third_party_response": response.json()
        }