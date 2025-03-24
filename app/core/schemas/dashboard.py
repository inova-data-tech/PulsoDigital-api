from pydantic import BaseModel, Json


class Dashboard(BaseModel):
    id: int
    topic_id: int
    data: Json

