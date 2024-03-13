# lib/cli.py

from helpers import (
    exit_program,
    list_departments,
    list_department_equipments,
    create_equipment, 
    delete_equipment
)

def menu():
    print("------Welcome to the Sporting Goods Store!--------")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Display all Sporting Goods Department's")

def menu2():
    print("Please select which Sporting Good's Department you wish to view: ")
    print("1. To view Outdoors department equipment")
    print("2. To view Fitness department equipment")
    print("3. To view Sports department equipment")
    
def menu3():
    print("Select what you would like to do with this department's equipment: ")
    print("1. To add an equipment to the department")
    print("2. To delete an equipment from the department")
    print("3. To go back to the department menu")
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
            # menu2()
            choice = input("> ")
            if choice == "1":
                list_department_equipments()
                menu3()
                choice = input("> ")
                if choice == "1":
                    print("Add equipment to department")
                    create_equipment()
                elif choice == "2":
                    print("Delete equipment from department")
                    delete_equipment()
                elif choice =="3":
                    print("Back to department menu")
                    list_departments()
                else:
                    print("Not a valid option, exiting program")
                    exit_program()
            elif choice == "2":
                list_department_equipments()
                menu3()
                choice = input("> ")
                if choice == "1":
                    print("Add equipment to department")
                    create_equipment()
                elif choice == "2":
                    print("Delete equipment from department")
                    delete_equipment()
                elif choice == "3":
                    print("Back to department menu")
                    list_departments()
                else:
                    print("Not a valid option, exiting program")
                    exit_program()
            elif choice == "3":
                list_department_equipments()
                menu3()
                choice = input("> ")
                if choice == "1":
                    print("Add equipment to department")
                    create_equipment()
                elif choice == "2":
                    print("Delete equipment from department")
                elif choice == "3":
                    print("Back to department menu")
                    list_departments()
                else:
                    print("Not a valid option, exiting program")
                    exit_program()
            elif choice == "4":
                exit_program()       
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
