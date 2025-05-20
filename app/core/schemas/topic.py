from pydantic import BaseModel, Field

class TopicBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Topic of the theme being evaluated")
    theme_id: int = Field(..., description="ID of the theme to which the topic belongs")
    
class TopicCreate(TopicBase):
    pass

class TopicUpdate(TopicBase):
    pass    

class Topic(TopicBase):
    id: int
    theme: str = Field(..., description="Theme of the topic being evaluated")
    
    class Config:
        orm_mode = True # Isso é crucial para converter modelos ORM para schemas
        from_attributes = True
       