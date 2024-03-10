# lib/cli.py

from helpers import (
    exit_program,
    list_departments,
    list_department_equipments
)

def menu():
    print("------Welcome to the Sporting Goods Store!--------")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Display all Sporting Goods Departments")
    
    
def menu3():
    print("Select if you would like to add or delete equipment to the Sporting Goods Department: ")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Sporting Goods Store Department's: ")
            list_departments()
            choice = input("> ")
            if choice == "1":
                list_department_equipments()
                menu3()
                choice = input("> ")
                # if choice == "1":
                #     print("Add equipment to department: ")
                # elif choice == "2":
                #     print("Delete equipment from department: ")
            elif choice == "2":
                list_department_equipments()
            elif choice == "3":
                list_department_equipments()
            elif choice == "4":
                exit_program()       
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
