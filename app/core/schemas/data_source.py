from pydantic import BaseModel

class DataSource(BaseModel):
    id: int
    topic_id: int
    source_type: str
    sourceURL: str
    partial: bool

