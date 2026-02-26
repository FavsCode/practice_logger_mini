import pytest
from pathlib import Path
from session import Session
from session import create_session, read_sessions
from database import create_db

@pytest.fixture
def database_path(tmp_path: Path) -> Path:
    db_file = tmp_path / "test.sqlite"
    return db_file

def test_create_session_creates_session(database_path: Path) -> None:
    with database_path as db_file:
        create_db(path=db_file)

    test_data = {"date": "2026-02-20",
                "duration": 60,
                "focus": "Repetition",
                } # Notes and id not inputted to test defaults
    
    creation = create_session(date=test_data["date"],
                duration=test_data["duration"],
                focus=test_data["focus"],
                path=database_path)
        
    sessions = read_sessions(path=db_file)

    assert creation == "Session successfully created."
    assert len(sessions) == 1

    stored = sessions[0]

    assert stored[1] == "2026-02-20"
    assert stored[2] == 60
    assert stored[3] == "Repetition"
    assert stored[4] == None

def test_read_sessions_returns_list_of_sessions(database_path: Path) -> None:
    with database_path as db_file:
        create_db(path=db_file)

    test_data = [{"date": "2026-02-20",
                    "duration": 60,
                    "focus": "Repetition"},
                 {"date": "2026-03-21",
                    "duration": 30,
                    "focus": "Scales"},
                 {"date": "2026-04-22",
                    "duration": 45,
                    "focus": ""}
                    ]
    for i in range(len(test_data)):
        create_session(test_data[i]["date"],
                       test_data[i]["duration"],
                       test_data[i]["focus"],
                       path=database_path)
    
    sessions = read_sessions(path=db_file)

    assert len(sessions) == 3
    # Don't forget the ID indexing!
    # Indexing will start at zero, but ID will start at 1
    # Don't forget the Notes row as None!
    assert sessions[0] == (1, "2026-02-20", 60, "Repetition", None)
    assert sessions[1] == (2, "2026-03-21", 30, "Scales", None)
    assert sessions[2] == (3, "2026-04-22", 45, "No Focus", None)

def test_update_sessions_changes_session_data(database_path: Path) -> None:
    pass
