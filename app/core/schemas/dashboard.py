
from pydantic import BaseModel
from datetime import date

class DashboardData(BaseModel):
    product_aspect: str
    rate: int
    coment_date: date
    overview: str

class DashboardBase(BaseModel):
    data: DashboardData
    topic_id: int

class DashboardCreate(DashboardBase):
    pass

class DashboardUpdate(DashboardBase):
    pass    

class Dashboard(DashboardBase):
    id: int

    class Config:
        orm_mode = True # Isso é crucial para converter modelos ORM para schemas
        from_attributes = True
