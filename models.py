from datetime import datetime

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    fruit_type = Column(String)
    planter = Column(String)
    color = Column(String)
    size = Column(Integer)
    grownm = Column(Boolean, default=False)
    created_on = Column(DateTime, default=datetime.utcnow)