# lib/cli.py

from helpers import (
    exit_program,
    list_departments,
    list_department_equipments,
    create_equipment, 
    delete_equipment,
    equipment_less_than_50
)

def menu():
    print("------Welcome to the Sporting Goods Store!--------")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. To display all Sporting Goods Department's")

def menu2():
    print("Please select which Sporting Good's Department you wish to view: ")
    print("1. To view equipment from the Outdoors department")
    print("2. To view equipment from the Fitness department")
    print("3. To view equipment from the Sports department")
    
def menu3():
    print("Select what you would like to do with this department's equipment: ")
    print("1. Add equipment to a Sporting Goods department")
    print("2. Delete equipment from a Sporting Goods department")
    print("3. To return to the Sporting Goods Department menu")
    print("4. Exit the program")
    print("5. View all equipment under $50 at the Sporting Good's store")

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
                elif choice == "3":
                    print("Back to department menu")
                    list_departments()
                elif choice == "4":
                    exit_program()
                elif choice == "5":
                    equipment_less_than_50()
                else:
                    print("Not a valid option")
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
                elif choice == "4":
                    exit_program()
                else:
                    print("Not a valid option")
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
                elif choice == "4":
                    exit_program()
                else:
                    print("Not a valid option")
            elif choice == "4":
                exit_program()       
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
