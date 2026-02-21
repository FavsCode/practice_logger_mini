import pytest
from pathlib import Path
from session import Session
from session import create_session
from database import create_db, select_sessions

@pytest.fixture
def database_path(tmp_path: Path) -> Path:
    db_file = tmp_path / "test.sqlite"
    return db_file

def test_create_session_creates_session(database_path: Path) -> None:
    create_db(path=database_path)
    test_data = {"date": "2026-02-20",
                 "duration": 60,
                 "focus": "Repetition",
                 } # Notes and id not inputted to test defaults
    
    creation = create_session(date=test_data["date"],
                   duration=test_data["duration"],
                   focus=test_data["focus"],
                   path=database_path)
    
    sessions = select_sessions(database_path)

    assert creation == "Session successfully created."
    assert len(sessions) == 1

    stored = sessions[0]

    assert stored[1] == "2026-02-20"
    assert stored[2] == 60
    assert stored[3] == "Repetition"
    assert stored[4] == None
