from database_connection import get_database_connection


def drop_tables(connection):
    """
    Removes databases

    Args:
        connection (sqlite connect): database connection
    """
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()


def create_tables(connection):
    """
    Creates a table in the database

    Args:
        connection (sqlite connect): database connection
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table scores (
            name TEXT PRIMARY KEY,
            score INTEGER
        );
    ''')

    connection.commit()


def initialize_database():
    """
    Initialises the database
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
