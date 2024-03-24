import os
import sqlite3

dirname = os.path.dirname(__file__)

# Determine if we are running in a test environment
is_test_env = os.getenv("TEST_ENV", "False") == "True"

# Choose database file based on the environment
db_file = "test_database.sqlite" if is_test_env else "database.sqlite"

connection = sqlite3.connect(os.path.join(dirname, "..", "data", db_file))
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
