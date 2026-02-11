from dataclasses import dataclass
from datetime import date
from database import insert_session, DELETE_session, UPDATE_session, SELECT_sessions

@dataclass
class Session:
    date: date
    duration: int
    focus: str = "No Focus"
    notes: str | None = None
    id: int | None = None

def create_session(date: date, duration: int, focus: str = "No Focus", notes: str | None = None, id: int | None = None) -> None:
    """Creates new session with user-inputted information."""
    insert_session(session: Session(date=date, duration=duration, focus=focus, notes=notes, id=id))

def read_sessions() -> str:
    """Reads out session data."""
    return SELECT_sessions('''SELECT date, duration, focus, notes
    FROM practice_sessions
    ''')

def update_session(session_aspect: str, edit: str | int, date: date) -> str:
    """Replaces a session's data with new user-inputted info."""
    return UPDATE_session('''UPDATE practice_sessions
    SET ? = ?
    WHERE date = ?
    ''', (session_aspect), (edit), (date))

def delete_session(date: date):
    """Deletes a session's data."""
    return DELETE_session('''DELETE FROM practice_sessions
    WHERE date = ?
    ''', (date))
