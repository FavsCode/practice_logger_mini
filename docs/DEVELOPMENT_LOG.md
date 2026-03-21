Feb 7 2026:
- Added file structure
- Transferred developement plan to VScode
- Installed SQLite and created table
- <b>Milestone #1 reached, "Database connects and is created"</b>
- PS. Update development plan

Feb 8 2026:
- Updated development plan
- Added tests to file structure and wrote some tests
- <b>Milestone #2 reached, "Session model exists"</b>
- PS. When saving date, use:
```bash 
session.date.isoformat
```
Feb 10 2026:
- Added newfound archetectural risk to development plan
- Attempted to implement CRUD
- Added placeholders for CRUD implementation
- Added files for failed CRUD attempts
- Gained an understanding of system responsibility

Feb 13 2026:
- Fixed circular import bug between database.py and session.py
- Switched database.py function names into pythonic format
- Added experiments folder to project structure
- CRUD operations successfully implemented; not clean and ready yet

Feb 15 2026:
- Added README

Feb 18 2026:
- Added data checks and validation in session.py 
- Updated roadmap milestones in README
- <b>Milestone #3 reached, "Successful CRUD operations on practice_sessions"</b>

Feb 20 2026:
- Added create_session() testing

Feb 25 2026:
- Added read_sessions() testing

Feb 28 2026:
- Added update_session() testing

Mar 3 2026:
- Added delete_session() testing
- <b>Milestone #4 reached, "Automated tests for CRUD operations"</b>

Mar 6 2026:
- Created main.py framework for functionality

Mar 8 2026:
- Moved database.py and session.py to src folder
- Added .pytest.ini to fix src module error (.gitignored)
- Updated test_database.py and test_session.py for new changes
- Updated README with new additions
- Updated DEVELOPMENT PLAN with new file structure
- Finshed main.py and tested it
- <b> Milestone #5 reached, "CLI menu interacts with functions" <b>

Mar 20 2026:
- Fixed src importing issues
- Confirmed code was pythonic and easy to read
- Updated README
- Fixed delete() testing error
- Moved main.py into the project root
- Deleted .pytest.ini
- Updated DEVELOPMENT_PLAN.md
- Updated code and made general refactors/repairs
- Finished project
- <b> Milestone #6 reached, "Refactor + type hints cleanup" <b>

Mar 21 2026:
- Improved UI a bit
- Fixed menu crash bug from no input
- Made the last session's data show up upon startup
- Split up main.py commands into more functions
- Fixed bug where database was created outside of the program folder