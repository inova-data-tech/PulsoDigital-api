from fastapi import APIRouter, Depends, Request, status
from app.api.dependencies import get_dashboard_service, get_topic_service
from app.services.dashboard_service import DashboardService
from app.services.topic_service import TopicService
from app.utils.webhook_parser import parse_webhook_payload

router = APIRouter(
    prefix="/api/webhook",
    tags=["Webhook"]
)

@router.post("/task-result", status_code=status.HTTP_200_OK)
async def webhook_task_result(
    payload: dict,
    dashboard_service: DashboardService = Depends(get_dashboard_service),
    topic_service: TopicService = Depends(get_topic_service)
):
    topic_name = payload.get("topic_name") or payload.get("nome_topico")
    topic = topic_service.get_by_name(topic_name)
    if not topic:
        return {"error": "Topic not found"}

    dashboard_data = parse_webhook_payload(payload, topic.id)
    dashboard = dashboard_service.create_with_evaluations(dashboard_data)
    return {"message": "Dashboard created", "dashboard_id": dashboard.id}