#Changed to use sqlaclhemy instead of raw sql commands
#Repository for user database activities
from entities.user import User
import bcrypt

class UserRepository:
    def __init__(self, session):
        self._session = session

    # Check for username in the database
    def find_by_username(self, username):
        return self._session.query(User).filter_by(username=username).first()

    # Creates a user
    def create_user(self, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    # Logging in verification of username and password
    def verify_user(self, username, password):
        user_record = self.find_by_username(username)
        if user_record and bcrypt.checkpw(password.encode('utf-8'), user_record.password.encode('utf-8')):
            return user_record.id
        return False
    
    # Find an ID belonging to a user
    def find_id_by_username(self, username):
        user = self.find_by_username(username)
        return user.id if user else None

    # Retrieving user's username
    def get_username_by_user(self, user_id):
        user = self._session.get(User, user_id)
        return user.username if user else None