import bcrypt

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()

    def create_user(self, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        self._connection.commit()

    def verify_user(self, username, password):
        user_record = self.find_by_username(username)
        if user_record and bcrypt.checkpw(password.encode('utf-8'), user_record["password"]):
            return True
        return False
