from pydantic import BaseModel

class Theme(BaseModel):
    id: int
    name: str
