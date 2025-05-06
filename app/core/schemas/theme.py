from pydantic import BaseModel, Field

class ThemeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Theme of the topic being evaluated")

class ThemeCreate(ThemeBase):
    pass

class ThemeUpdate(ThemeBase):
    pass

class Theme(ThemeBase):
    id: int

    class Config:
        orm_mode = True # Isso é crucial para converter modelos ORM para schemas
        from_attributes = True # Para versões mais recentes do Pydantic