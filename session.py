from dataclasses import dataclass
from pathlib import Path
from datetime import date, datetime
from database import insert_session, delete_session as db_delete_session, update_session as db_update_session, select_sessions

@dataclass
class Session:
    date: date
    duration: int
    focus: str = "No Focus"
    notes: str | None = None
    id: int | None = None

def check_date_format(date_str: str) -> date | bool:
    """Checks if the date string is in the correct format."""
    try:
        user_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return user_date
    except ValueError:
        return False

def create_session(date: str,
                   duration: int,
                   focus: str = "No Focus", 
                   notes: str | None = None, 
                   id: int | None = None,
                   path: Path | None = None) -> str:
    """Creates new session with user-inputted information."""
    if not check_date_format(date):
        return "Error: Invalid date format."
    
    user_date = check_date_format(date)
    
    try: 
        duration = int(duration)
    except ValueError:
        return "Error: Invalid duration format."
    
    try:
        focus = str(focus)
        if not focus:
            focus = "No Focus"
    except ValueError:
        return "Error: Invalid focus format."
    
    try:
        notes = str(notes) if notes is not None else None
    except ValueError:        
        return "Error: Invalid notes format."

    # User date is already validated, so this will not return an error.
    new_session = Session(date=user_date, # type: ignore
                          duration=duration, 
                          focus=focus, 
                          notes=notes, 
                          id=id) 
    
    if path:
        insert_session(new_session, path=path)
    else:
        insert_session(new_session)
    return "Session successfully created."

def read_sessions() -> list[tuple]:
    """Reads out session data."""
    return select_sessions()

def update_session(session_aspect: str, edit: str | int, date: str) -> str:
    """Replaces a session's data with new user-inputted info."""
    try:
        if session_aspect == "duration":
            edit = int(edit)
        elif session_aspect in {"focus", "notes"}:
            edit = str(edit)
            if session_aspect == "focus" and not edit:
                edit = "No Focus"
    except ValueError:
        return "Error: Invalid edit format."
    
    try:
        user_date = datetime.strptime(str(date), "%Y-%m-%d").date()
    except ValueError:
        return "Error: Invalid date format."
    
    db_update_session(session_aspect, edit, user_date)
    return "Session updated successfully."

def delete_session(date: str) -> str:
    """Deletes a session's data."""
    if not check_date_format(date):
        return "Error: Invalid date format."
    
    user_date = check_date_format(date) # User date is already validated, so this will not return False.

    db_delete_session(user_date) # type: ignore
    return "Session deleted successfully."
