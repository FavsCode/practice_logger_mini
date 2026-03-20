"""Main module and entry point for Practice Logger Mini."""
from session import create_session, read_sessions, update_session, delete_session
from src.database import create_db

def divider():
    print("\n" + "-" * 40 + "\n")

def greet():
    print("Welcome to Practice Logger Mini!")
    print("An app that allows you to log and retrieve practice session data.\n")

def menu():
    """Displays the main menu.
    """
    print("Menu:")
    print("1. Add session")
    print("2. View sessions")
    print("3. Update session")
    print("4. Delete session")
    print("5. Exit")
    divider()

def handle_user_selection():
    """Handles the user's menu selection.
    """
    valid_selection = False

    while valid_selection != True:
        selection = int(input("Enter your selection (1-5): "))
        if selection == 1:
            example_input = "2023-09-15, 60, Scales, Focused on major scales"
            print(f"\nExample input: {example_input}")

            create_session_input = input("Enter session details (date in YYYY-MM-DD format, duration in minutes, focus, notes - optional) separated by commas: ")
            try:
                date, duration, focus, notes = [item.strip() for item in create_session_input.split(",")]
            except ValueError:
                date, duration, focus = [item.strip() for item in create_session_input.split(",")]
                notes = None

            duration = int(duration)

            result = create_session(date, duration, focus, notes)
            print(f"\n{result}")
            divider()
            menu()
        elif selection == 2:
            sessions = read_sessions(None) # Error with no input for some reason, so it's set to None
            
            if sessions:
                divider()
                print("Sessions:")
                for session in sessions:
                    print(f"Date: {session[1]}, Duration: {session[2]} minutes, Focus: {session[3]}, Notes: {session[4]}")
                divider()
                menu()
            else:
                print("\nNo sessions found.")
                divider()
                menu()
        elif selection == 3:
            # Display all sessions before updating
            sessions = read_sessions(None) # Error with no input for some reason, so it's set to None
            print("\nSessions:")
            for session in sessions:
                print(f"Date: {session[1]}, Duration: {session[2]} minutes, Focus: {session[3]}, Notes: {session[4]}")
            divider()

            date = input("Enter the date of the session you want to update (YYYY-MM-DD): ")
            session_aspect = input("Enter the aspect you want to update (date, duration, focus, notes): ")
            edit = input(f"Enter the new value for {session_aspect}: ")
            
            result = update_session(session_aspect, edit, date, None)
            print(f"\n{result}")
            divider()
            menu()
        elif selection == 4:
            # Display all sessions before deletion
            sessions = read_sessions(None) # Error with no input for some reason, so it's set to None
            print("\nSessions:")
            for session in sessions:
                print(f"Date: {session[1]}, Duration: {session[2]} minutes, Focus: {session[3]}, Notes: {session[4]}")
            divider()

            date = input("Enter the date of the session you want to delete (YYYY-MM-DD): ")
            
            result = delete_session(date, None)
            print(f"\n{result}")
            divider()
            menu()
        elif selection == 5:
            print("\nExiting the program. Goodbye!")
            divider()
            quit()
        else:
            print("\nInvalid selection.\n")

def main():
    create_db()
    greet()
    menu()
    handle_user_selection()

if __name__ == "__main__":
    main()