class ActivityRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_activity(self, description):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO activities (description) VALUES (?)', (description,))
        self._connection.commit()

    def get_all_activities(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM activities')
        activities = cursor.fetchall()
        return activities
    