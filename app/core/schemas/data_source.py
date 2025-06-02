from pydantic import BaseModel, Field

class DataSourceBase(BaseModel):
    source_type: str = Field(..., description="Type of the data source")    
    sourceURL: str = Field(..., description="URL of the data source")    
    biased: bool = Field(False, description="Indicates if the data source is biased")
    topic_id: int   = Field(..., description="ID of the topic to which the data source belongs")
class DataSourceCreate(DataSourceBase):
    pass
class DataSourceUpdate(DataSourceBase):
    pass
class DataSource(DataSourceBase):
    id: int

    class Config:
        orm_mode = True  # Crucial for converting ORM models to schemas
        from_attributes = True  