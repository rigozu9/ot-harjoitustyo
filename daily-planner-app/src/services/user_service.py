import bcrypt
from database_connection import get_database_connection

""""Käyttäjien hallintaan service"""

""""Rekisteröinti"""
def register_user(username, password):
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        return False

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    connection.commit()

    return True

""""Sisäänkirjatuminen."""
def login_user(username, password):
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_record = cursor.fetchone()

    if user_record and bcrypt.checkpw(password.encode('utf-8'), user_record['password']):
        return True

    return False
