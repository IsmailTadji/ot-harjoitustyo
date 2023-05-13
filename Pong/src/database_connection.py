import os
import sqlite3

DIRNAME = "src/data/scores.db"

connection = sqlite3.connect(os.path.join(DIRNAME))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
