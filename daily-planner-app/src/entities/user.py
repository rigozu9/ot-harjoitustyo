"""Sqlalchemy imports and base class import"""
from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    """This is an SQLAlchemy model for User"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    sex = Column(Enum('Male', 'Female', 'Other', name='sex_types'), nullable=True)
    
    sleep_goal = Column(Integer, nullable=True)
    exercise_goal = Column(Integer, nullable=True)
    outside_goal = Column(Integer, nullable=True)
    productive_goal = Column(Integer, nullable=True)
    screen_goal = Column(Integer, nullable=True)

    first_login_completed = Column(Boolean, default=False, nullable=False)

    daily_plans = relationship("DailyPlan", back_populates="user", cascade="all, delete")
