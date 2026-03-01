import sqlite3
from datetime import date
from pathlib import Path

def create_db(path: Path | str = 'practice_sessions.sqlite') -> None:
    """Initializes the SQLite database and creates the practice_sessions table if it doesn't exist."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS practice_sessions (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            duration INTEGER NOT NULL,
            focus TEXT,
            notes TEXT
        )
        ''')
        sqlite_connection.commit()

def insert_session(session, path: Path | str = 'practice_sessions.sqlite') -> None:
    """Inserts session data to the database."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute('''
        INSERT INTO practice_sessions (date, duration, focus, notes) 
        VALUES (?, ?, ?, ?)
        ''', (session.date.isoformat(), session.duration, session.focus, session.notes))
        sqlite_connection.commit()

def delete_session(date: date, path: Path | str = 'practice_sessions.sqlite') -> None:
    """Deletes session data from the database."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute('''
        DELETE FROM practice_sessions
        WHERE date = ?
        ''', (date.isoformat(),))
        sqlite_connection.commit()

def update_session(session_aspect: str, edit: str | int, date: date, path: Path | str = 'practice_sessions.sqlite') -> None:
    """Updates session data from the database."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute(f'''
        UPDATE practice_sessions
        SET {session_aspect} = ?
        WHERE date = ?
        ''', (edit, date.isoformat()))
        sqlite_connection.commit()

def select_sessions(path: Path | str = 'practice_sessions.sqlite') -> list[tuple]:
    """Selects all session data from the database."""
    with sqlite3.connect(path) as sqlite_connection:
        cursor = sqlite_connection.cursor()
        cursor.execute('''
        SELECT * FROM practice_sessions 
        ''')
        return cursor.fetchall()

if __name__ == '__main__':
    create_db()