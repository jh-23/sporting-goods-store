# lib/cli.py

from helpers import (
    exit_program,
    create_equipment,
    delete_equipment,
    list_equipments,
    find_equipment_by_name
)


def main():
    
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Viewing all sports equipment...")
            list_equipments()
            
        elif choice == "2":
            print("View sports equipment by title...")
        elif choice == "3":
            print("Displaying all sports equipment...")
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View all sports equipment")
    print("2. View sports equipment by title")
    print("3. Show all sports equipment")
        


if __name__ == "__main__":
    main()
