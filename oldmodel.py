from datetime import datetime

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)
    created_on = Column(DateTime, default=datetime.utcnow)