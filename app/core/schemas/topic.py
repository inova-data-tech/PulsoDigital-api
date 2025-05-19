from pydantic import BaseModel

class TopicBase(BaseModel):
    name: str
    theme: str
    
class TopicCreate(TopicBase):
    pass

class TopicUpdate(TopicBase):
    pass    

class Topic(TopicBase):
    id: int
    
    class Topic(BaseModel):
        orm_mode = True # Isso é crucial para converter modelos ORM para schemas
        from_attributes = True
       

