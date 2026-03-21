"""Main module and entry point for Practice Logger Mini."""
from src.session import create_session, read_sessions, update_session, delete_session, see_last_session
from src.database import create_db

def divider():
    """Prints a divider line for better readability."""
    print("\n" + "-" * 40 + "\n")

def greet():
    """Prints a welcome message to the user."""
    print("Welcome to Practice Logger Mini!")
    print("An app that allows you to log and retrieve practice session data.\n")

    print("Your last session:")
    print(see_last_session(None) + "\n")

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

def selection_1():
    """Handles the logic for adding a new session."""
    example_input = "2023-09-15, 60, Scales, Nice major scales!"
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
    
def selection_2():
    """Handles the logic for viewing all sessions."""
    sessions = read_sessions(None) # Error with no input for some reason, so it's set to None
    if sessions:
        divider()
        print("Sessions:")
        for session in sessions:
            print(f"\nDate: {session[1]}, Duration: {session[2]} minutes, Focus: {session[3]}, Notes: {session[4]}")
        divider()
        menu()
    else:
        print("\nNo sessions found.")
        divider()
        menu()

def selection_3():
    """Handles the logic for updating a session."""
    print("\nUpdate Session:")
    print("To update a session, you will need to provide the date of the session you want to update and the aspect you want to change (date, duration, focus, notes).")
    print("Example input for aspect: date")
    print("Example input for new value: 2023-09-16")
    divider()
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

def selection_4():
    """Handles the logic for deleting a session."""
    print("\nDelete Session:")
    print("To delete a session, you will need to provide the date of the session you want to delete.")
    print("Example input: 2023-09-15")
    divider()
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

def handle_user_selection():
    """Handles the user's menu selection.
    """
    valid_selection = False

    while valid_selection != True:
        try:
            selection = int(input("Enter your selection (1-5): "))
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 5.\n")
            continue

        if selection == 1:
            selection_1()
        elif selection == 2:
            selection_2()
        elif selection == 3:
            selection_3() 
        elif selection == 4:
            selection_4()
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