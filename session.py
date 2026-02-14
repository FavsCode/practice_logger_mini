from dataclasses import dataclass
from datetime import date
from database import insert_session, delete_session as db_delete_session, update_session as db_update_session, select_sessions

@dataclass
class Session:
    date: date
    duration: int
    focus: str = "No Focus"
    notes: str | None = None
    id: int | None = None

def create_session(date: date, duration: int, focus: str = "No Focus", notes: str | None = None, id: int | None = None) -> str:
    """Creates new session with user-inputted information."""
    new_session = Session(date=date, duration=duration, focus=focus, notes=notes, id=id)
    insert_session(new_session)
    return "Session successfully created."

def read_sessions() -> list[tuple]:
    """Reads out session data."""
    return select_sessions()

def update_session(session_aspect: str, edit: str | int, date: date) -> str:
    """Replaces a session's data with new user-inputted info."""
    db_update_session(session_aspect, edit, date)
    return "Session updated successfully."

def delete_session(date: date) -> str:
    """Deletes a session's data."""
    db_delete_session(date)
    return "Session deleted successfully."
