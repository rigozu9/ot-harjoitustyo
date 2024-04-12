"""SQLAlchemy imports and base"""
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class DailyPlan(Base):
    """SQLAlchemy model for DailyPlan"""

    __tablename__ = 'dailyplans'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    sleep = Column(Integer, nullable=True)  # Hours of sleep
    outside_time = Column(Integer, nullable=True)  # Time spent outside in minutes
    productive_time = Column(Integer, nullable=True)  # Productive time in minutes
    exercise = Column(Integer, nullable=True)  # Time spent on exercise in minutes
    screen_time = Column(Integer, nullable=True)  # Screen time in minutes
    other_activities = Column(String, nullable=True)  # Description of other activities

    user = relationship("User", back_populates="daily_plans")
