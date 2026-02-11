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

def insert_session(session: object, path: str = 'practice_sessions.sqlite') -> None:
    """Inserts session data to the database."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute('''
        INSERT INTO practice_sessions (date, duration, focus_area, notes)
        VALUES (?, ?, ?, ?)
        ''', (session.date, session.duration, session.focus, session.notes))
        sqlite_connection.commit()

def DELETE_session(command: str, date: date, path: str = 'practice_sessions.sqlite') -> None:
    """Deletes session data from the database."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute(command, date)
        sqlite_connection.commit()

def UPDATE_session(command: str, session_aspect: str, edit: str | int, date: date, path: str = 'practice_sessions.sqlite') -> None:
    """Updates session data from the database."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute(command, session_aspect, edit, date)
        sqlite_connection.commit()


def SELECT_sessions(command: str, path: str = 'practice_sessions.sqlite') -> None:
    """Selects all session data from the database."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        result = cursor.execute(command)
        sqlite_connection.commit()
        return result

if __name__ == '__main__':
    create_db()