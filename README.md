# Practice Session Logger Mini
A command-line session logger to create, update, read, and delete musical practice session data.

**Status: Currently in active development.**

## Features
- SQLite database storage
- Session data modeling
- CRUD session operations
- Automated tests (in progress)
- Command-line UI (planned)
- Clean structure and type hints (in progress)
- Development tracking and documentation 
- Clear separation of concerns

## Architecture
### Layer #1 - UI
main.py handles all visual aspects like the menu and collecting user-inputted data.

### Layer #2 - Session Model
Acts as an organizer for data to represent a practice session.

### Layer #3 - Service Bridge
session.py (the service bridge) acts as a middle ground between the UI and database layers, validating session data and coordinating CRUD operations before passing it on to the database executor or sending it back as invalid data.

### Layer #4 - Database Executor
When commanded by the service to do so, it takes the data and performs requested CRUD operations on the database to send back results.

### Layer #5 - Database
practice_sessions.sqlite stores structured session data in a local SQLite file for retrieval and external manipulation by the database executor.

## Data Flow

> User Input (CLI)\
    ↓\
> Session Model\
    ↓\
> Service Bridge\
    ↓\
> Database Executor\
    ↓\
> SQLite Database

## Roadmap/Milestones
> 1. Database connects and is created (Done)
> 2. Session model exists (Done)
> 3. Successful CRUD operations on practice_sessions (In progress)
> 4. Automated tests for CRUD operations
> 5. CLI menu interacts with functions 
> 6. Refactor + type hints cleanup 

## Tech Stack
- **Language:** Python
- **Database:** SQLite

## Future Goals
- Scale up to the full-sized practice logger
- Add comprehensive data summaries
- Show last session data upon startup
- Built-in timer to track session duration while the app is running
- Support multi-user accounts
- Improve accessibility through a desktop app, widget, or packaged download