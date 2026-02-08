import sqlite3

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

if __name__ == '__main__':
    create_db()