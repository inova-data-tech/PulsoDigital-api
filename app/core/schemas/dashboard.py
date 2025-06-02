
from pydantic import BaseModel, Field
from datetime import date

class DashboardBase(BaseModel):
    product_aspect: str = Field(..., min_length=1, max_length=100, description="Product aspect of the topic being evaluated")   
    rate: int = Field(..., description="Rate of the topic being evaluated")
    comment_date: date = Field(..., description="Date of the comment from post about the topic")
    overview: str = Field(..., description="Overview of the topic being evaluated")
    topic_id: int = Field(..., description="ID of the topic to which the dashboard belongs")    

class DashboardCreate(DashboardBase):
    pass

class DashboardUpdate(DashboardBase):
    pass    

class Dashboard(DashboardBase):
    id: int

    class Config:
        orm_mode = True # Isso é crucial para converter modelos ORM para schemas
        from_attributes = True
