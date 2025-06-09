
from pydantic import BaseModel, Field
from datetime import date

class DashboardEvaluationModel(BaseModel):
    product_aspect: str = Field(..., min_length=1, max_length=100, description="Product aspect of the topic being evaluated")
    rate_date: date = Field(..., description="Date of the evaluation")
    rate: int = Field(..., description="Rate of the topic being evaluated")
    
class DashboardEvaluationCreate(DashboardEvaluationModel):
    pass

class DashboardEvaluationUpdate(DashboardEvaluationModel):
    pass

class DashboardEvaluation(DashboardEvaluationModel):
    id: int
    
    class Config:
        orm_mode = True  # Crucial for converting ORM models to schemas
        from_attributes = True    
        
class DashboardBase(BaseModel):
    topic_id: int = Field(..., description="ID of the topic to which the dashboard belongs") 
    status: str = Field(..., description="Status of the dashboard", default="deactive")
    avg_rate: float = Field(..., description="Average rate of the topic being evaluated")
    category: str = Field(..., description="Category of the topic being evaluated")
    negative_rate: int = Field(..., description="Negative rate of the topic being evaluated")
    neutral_rate: int = Field(..., description="Neutral rate of the topic being evaluated")
    positive_rate: int = Field(..., description="Positive rate of the topic being evaluated")   
   
class DashboardCreate(DashboardBase):
    evaluations: list[DashboardEvaluationCreate] = Field(..., description="List of evaluations for the dashboard")
    pass

class DashboardUpdate(DashboardBase):
    evaluations: list[DashboardEvaluationUpdate] = Field(..., description="List of evaluations for the dashboard")
    pass    

class Dashboard(DashboardBase):
    id: int
    evaluations: list[DashboardEvaluation] = Field(..., description="List of evaluations for the dashboard")

    class Config:
        orm_mode = True # Isso é crucial para converter modelos ORM para schemas
        from_attributes = True
