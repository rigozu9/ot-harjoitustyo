"""Sqlalchemy imports and base class import"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Activity(Base):
    """This an sqlalchmy model for Activity"""

    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="activities")
