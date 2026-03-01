import pytest
from pathlib import Path
from session import create_session, read_sessions, update_session
from database import create_db

@pytest.fixture
def database_path(tmp_path: Path) -> Path:
    db_file = tmp_path / "test.sqlite"
    return db_file

@pytest.fixture
def test_data() -> list[dict]:
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
    return test_data

def test_create_session_creates_session(database_path: Path, test_data: list[dict]) -> None:
    with database_path as db_file:
        create_db(path=db_file)

    retrived_test_data = test_data[0]
    
    creation = create_session(date=retrived_test_data["date"],
                duration=retrived_test_data["duration"],
                focus=retrived_test_data["focus"],
                path=database_path)
        
    sessions = read_sessions(path=db_file)

    assert creation == "Session successfully created."
    assert len(sessions) == 1

    stored = sessions[0]

    assert stored[1] == "2026-02-20"
    assert stored[2] == 60
    assert stored[3] == "Repetition"
    assert stored[4] == None

def test_read_sessions_returns_list_of_sessions(database_path: Path, test_data: list[dict]) -> None:
    with database_path as db_file:
        create_db(path=db_file)

    retrived_test_data = test_data

    for i in range(len(retrived_test_data)):
        create_session(retrived_test_data[i]["date"],
                       retrived_test_data[i]["duration"],
                       retrived_test_data[i]["focus"],
                       path=database_path)
    
    sessions = read_sessions(path=db_file)

    assert len(sessions) == 3
    # Don't forget the ID indexing!
    # Indexing will start at zero, but ID will start at 1
    # Don't forget the Notes row as None!
    assert sessions[0] == (1, "2026-02-20", 60, "Repetition", None)
    assert sessions[1] == (2, "2026-03-21", 30, "Scales", None)
    assert sessions[2] == (3, "2026-04-22", 45, "No Focus", None)

def test_update_sessions_changes_session_data(database_path: Path, test_data: list[dict]) -> None:
    with database_path as db_file:
        create_db(path=db_file)

    retrived_test_data = test_data

    for i in range(len(retrived_test_data)):
        create_session(retrived_test_data[i]["date"],
                       retrived_test_data[i]["duration"],
                       retrived_test_data[i]["focus"],
                       path=database_path)

    update_session("duration", 90, "2026-02-20", database_path)
    update_session("notes", "Good practice.", "2026-03-21", database_path)
    update_session("date", "2026-04-23", "2026-04-22", database_path)
    update_session("focus", "Recreation", "2026-02-20", database_path)

    sessions = read_sessions(path=db_file)

    assert sessions[0] == (1, "2026-02-20", 90, "Recreation", None)
    assert sessions[1] == (2, "2026-03-21", 30, "Scales", "Good practice.")
    assert sessions[2] == (3, "2026-04-23", 45, "No Focus", None)