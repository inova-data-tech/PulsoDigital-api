from pydantic import BaseModel

class Topic(BaseModel):
    id: int
    name: str
    theme: str

