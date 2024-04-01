#Tiedosto tietokantaan yhdistämiselle. 
import os
from sqlalchemy import create_engine
from entities.base import Base
from sqlalchemy.orm import scoped_session, sessionmaker

dirname = os.path.dirname(__file__)
#Jos TEST_ENV on true niin käytetään testi tietokantaa
is_test_env = os.getenv("TEST_ENV", "False") == "True"
db_file = "test_database.sqlite" if is_test_env else "database.sqlite"

database_url = f"sqlite:///{os.path.join(dirname, '..', 'data', db_file)}"

engine = create_engine(database_url, connect_args={"check_same_thread": False}, echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def init_db():
    from entities.user import User
    from entities.activity import Activity
    Base.metadata.create_all(bind=engine)

def get_database_session():
    return Session()
