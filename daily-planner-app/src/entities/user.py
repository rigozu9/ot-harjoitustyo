from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

#SQLAlchemy class for User. Used for alembic

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    activities = relationship("Activity", back_populates="user")
