import sqlite3
from datetime import date
from session import Session

def create_db(path: str = 'practice_sessions.sqlite') -> None:
    """Initializes the SQLite database and creates the practice_sessions table if it doesn't exist."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS practice_sessions (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            duration INTEGER NOT NULL,
            focus_area TEXT,
            notes TEXT
        )
        ''')

def insert_session(path: str = 'practice_sessions.sqlite') -> None:
    """Inserts session data to the database."""

def DELETE_session(path: str = 'practice_sessions.sqlite') -> None:
    """Deletes session data from the database."""

def UPDATE_session(path: str = 'practice_sessions.sqlite') -> None:
    """Updates session data from the database."""

def SELECT_sessions(path: str = 'practice_sessions.sqlite') -> None:
    """Selects all session data from the database."""

if __name__ == '__main__':
    create_db()