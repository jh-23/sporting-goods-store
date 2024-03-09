# lib/cli.py

from helpers import (
    exit_program,
    list_departments
)

def menu():
    print("------Welcome to the Sporting Goods Store!--------")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Display all Sporting Goods Departments")
    
def menu2():
    print("Please select a Sporting Goods Department:")
    print("1. Print outdoors equipment")
    print("2. Print fitness equipment")
    print("3. Print sports equipment")
    print("4. Exit the program")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Sporting Goods Store Department's: ")
            list_departments()
            menu2()
            choice = input("> ")
            if choice == "1":
                print("Outdoors equipment")
            elif choice == "2":
                print("fitness equipment")
            elif choice == "3":
                print("sports equipment")
            elif choice == "4":
                exit_program()       
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
