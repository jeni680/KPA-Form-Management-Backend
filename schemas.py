from pydantic import BaseModel

# Shared base schema
class KPAFormBase(BaseModel):
    name: str
    email: str
    phone: str
    qualification: str
    college: str
    address: str
    area_of_interest: str
    internship_domain: str
    project_topic: str
    project_description: str
    internship_expectation: str
    description: str

# Input schema for POST request
class KPAFormCreate(KPAFormBase):
    pass

# Output schema for response
class KPAFormOut(KPAFormBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # Pydantic v2 compatible replacement for orm_mode
