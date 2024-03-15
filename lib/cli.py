# lib/cli.py

from helpers import (
    exit_program,
    list_departments,
    list_department_equipments,
    create_equipment, 
    delete_equipment,
    equipments_less_than_50
)

def menu():
    print("------Welcome to the Sporting Goods Store!--------")
    print("\n")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. To display all Sporting Goods Department's")

def menu2():
    print("Please select which Sporting Good's Department you wish to view: ")
    print("1. To view equipment from the Outdoors department")
    print("2. To view equipment from the Fitness department")
    print("3. To view equipment from the Sports department")
    
def menu3():
    print("Select what you would like to do with a Sporting Goods Department: ")
    print("\n")
    print("1. Add equipment to a Sporting Goods department")
    print("2. Delete equipment from a Sporting Goods department")
    print("3. View all equipment under $50 at the Sporting Good's store")
    print("4. To return to the Sporting Goods Department menu")
    print("5. Exit the program")
    

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Sporting Goods Store Department's: ")
            list_departments()
            print("\n")
            menu2()
            choice = input("> ")
            if choice == "1":
                print("\n")
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
                    print("View all equipment under $50 at the Sporting Goods Store:")
                    equipments_less_than_50()
                elif choice == "4":
                    print("Return to department menu")
                    list_departments()
                elif choice == "5":
                    exit_program()
                else:
                    print("Not a valid option")
            elif choice == "2":
                list_department_equipments()
                print("\n")
                menu3()
                choice = input("> ")
                if choice == "1":
                    print("Add equipment to department")
                    create_equipment()
                elif choice == "2":
                    print("Delete equipment from department")
                    delete_equipment()
                elif choice == "3":
                    print("View all equipment under $50 at the Sporting Good Store: ")
                    equipments_less_than_50()
                elif choice == "4":
                    print("Return to department menu")
                    list_departments()
                elif choice == "5":
                    exit_program()
                else:
                    print("Not a valid option")
                    exit_program()
            elif choice == "3":
                list_department_equipments()
                print("\n")
                menu3()
                choice = input("> ")
                if choice == "1":
                    print("Add equipment to department")
                    create_equipment()
                elif choice == "2":
                    print("Delete equipment from department")
                elif choice == "3":
                    print("View all equipment under $50 at the Sporting Good Store: ")
                    list_departments()
                elif choice == "4":
                    print("Return to department menu")
                    list_departments()
                elif choice == "5":
                    exit_program()
                else:
                    print("Not a valid option")
            elif choice == "4":
                exit_program()       
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
