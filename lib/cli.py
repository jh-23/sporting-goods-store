# lib/cli.py

from helpers import (
    exit_program,
    create_equipment,
    delete_equipment,
    
)


def main():
    
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Adding sports equipment...")
        elif choice == "2":
            print("View sports equipment by title...")
        elif choice == "3":
            print("Displaying all sports equipment...")
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add sports equipment")
    print("2. View sports equipment by title")
    print("3. Show all sports equipment")
        


if __name__ == "__main__":
    main()
