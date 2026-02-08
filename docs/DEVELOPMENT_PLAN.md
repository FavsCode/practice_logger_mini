# Concept 

A command-line session logger to create, update, read, and delete sessions. 

# Scope 

## DOES: 

- Create session records 

- Read session records 

- Update session records 

- Delete session records 

## DOES NOT: 

- Have fancy CLI 

- Possess folders 

- Have an account feature 

- Possess a login 

- Data analytics or progress tracking 

# Data Model 
```bash
Session: 

    ID: (PRIMARY KEY)	 

    Date: (Stored as TEXT in ISO format: YYYY-MM-DD) 

    Duration: (INTEGER as minutes) 

    Focus: (STRING, default = “No Focus”) 

    Notes: (TEXT, optional) 
```
# Program Flow 
```bash
Start program 

Show menu: 

    1. Add session 

    2. View sessions 

    3. Update session 

    4. Delete session 

    5. Exit 
```
# File Structure 
```bash
practice_logger_mini/ 

    main.py --> Entry point of the program 

    practice_sessions.db --> Stores all practice session data 

    database.py --> Takes info from main and operates on practice_sessions using the session model 

    session.py --> Contains a session model 
```
# Milestones 

1. Database connects and is created 

2. Session model exists 

3. Successful CRUD operations on practice_sessions 

4. CLI menu interacts with functions 

5. Refactor + type hints cleanup 

# Risk Notes 

- Deletion and updating permissions given to the user could be exploited and over-delete or fully change existing data 

- Database could break program 

- Service might have to handle too much and mix up UI and server-side 

- Session model could transfer incorrectly to practice_sessions 

- Date logging could run into excess formatting issues 

- Forgetting to commit database transactions 