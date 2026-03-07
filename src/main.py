
def divider():
    print("\n" + "-" * 40 + "\n")

def greet():
    print("Welcome to Practice Logger Mini!")
    print("An app that allows you to log and retrieve practice session data.\n")

def menu():
    print("Menu:")
    print("1. Add session")
    print("2. View sessions")
    print("3. Update session")
    print("4. Delete session")
    print("5. Exit")
    divider()

    valid_selection = False

    while valid_selection != True:
        selection = int(input("Enter your selection (1-5): "))
        if selection == 1:
            valid_selection = True
            divider()
        elif selection == 2:
            valid_selection = True
            divider()
        elif selection == 3:
            valid_selection = True
            divider()
        elif selection == 4:
            valid_selection = True
            divider()
        elif selection == 5:
            valid_selection = True
            print("\nExiting the program. Goodbye!\n")
            divider()
            quit()
        else:
            print("\nInvalid selection.\n")

def main():
    greet()
    menu()

if __name__ == "__main__":
    main()