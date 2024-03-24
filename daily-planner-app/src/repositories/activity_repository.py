#Class for all the activity database methods
class ActivityRepository:
    def __init__(self, connection):
        self._connection = connection

    #Adding an activity to database
    def add_activity(self, description, user_id):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO activities (description, user_id) VALUES (?, ?)', (description, user_id))
        self._connection.commit()

    #Retrivien users activities
    def get_all_activities_by_user(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM activities WHERE user_id = ?', (user_id,))
        activities = cursor.fetchall()
        return activities

    #Retrivien users username
    def get_username_by_user(self, user_id):
        cursor = self._connection.cursor()
        cursor.execute('SELECT username FROM users WHERE id = ?', (user_id,))
        username = cursor.fetchone()
        return username
        
        