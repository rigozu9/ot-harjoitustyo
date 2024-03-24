# entities/activity.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
