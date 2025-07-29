from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class KPAForm(Base):
    __tablename__ = "kpa_forms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    qualification = Column(String)
    college = Column(String)
    address = Column(String)
    area_of_interest = Column(String)
    internship_domain = Column(String)
    project_topic = Column(String)
    project_description = Column(String)
    internship_expectation = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)
