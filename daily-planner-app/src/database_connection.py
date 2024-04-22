"""
    Database handling file. Imports os, sqlalchemy's create_engine, scoped_session and 
    sessionmaker also the base entity.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from entities.base import Base

# I need to import the entities for the metadata to work correctly. So I disabled unused import.
from entities.user import User  # pylint: disable=unused-import
from entities.dailyplan import DailyPlan  # pylint: disable=unused-import


dirname = os.path.dirname(__file__)

is_test_env = os.getenv("TEST_ENV", "False") == "True"
DB_FILE = "test_database.sqlite" if is_test_env else "database.sqlite"

database_url = f"sqlite:///{os.path.join(dirname, '..', 'data', DB_FILE)}"

engine = create_engine(database_url, connect_args={
                       "check_same_thread": False}, echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def init_db():
    """Creates tables from metadata if necessary"""
    Base.metadata.create_all(bind=engine)


def get_database_session():
    """returns database session"""
    return Session()
