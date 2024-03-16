# lib/cli.py

from helpers import (
    exit_program,
    list_departments,
    create_department,
    delete_department,
    list_department_equipments,
    create_equipment, 
    delete_equipment,
    equipments_less_than_50,
    list_departments
)

def main_menu():
    print("------Welcome to the Sporting Goods Store!--------")
    print("\n")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. To display all Sporting Goods Department's")

def department_menu_options():
    print("0. Exit the program")
    print("1. To display all Sporting Goods Department's again: ")
    print("2. Select a given department to see details")
    print("3. To add a department to the Sporting Goods Store")
    print("4. To delete a department from the Sporting Goods Store")
    print("5. Go back to previous menu")
    
def equipment_menu_options():
    print("Select what you would like to do with a Sporting Goods Department: ")
    print("\n")
    print("1. Add equipment to a Sporting Goods department")
    print("2. Delete equipment from a Sporting Goods department")
    print("3. View all equipment under $50 at the Sporting Good's store")
    print("4. To return to the Sporting Goods Department menu")
    print("5. Exit the program")
    

def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Sporting Goods Store Department's: ")
            print("\n")
            list_departments()
            print("\n")
            departments_menu()
        else:
            print("Invalid choice")

def departments_menu():
     while True:
        department_menu_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_departments()
        elif choice == "2":
            list_departments()
        elif choice == "3":
            create_department()
        elif choice == "4":
            delete_department()
        elif choice == "5":
            main()
        else:
            print("Invalid Choice")
            
def equipments_menu():
    while True:
        equipment_menu_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        if choice == "1":
            

if __name__ == "__main__":
    main()





            # menu2()
            # choice = input("> ")
            # if choice == "1":
            #     print("\n")
            #     list_department_equipments()
            #     menu3()
            #     choice = input("> ")
            #     if choice == "1":
            #         print("Add equipment to department")
            #         create_equipment()
            #     elif choice == "2":
            #         print("Delete equipment from department")
            #         delete_equipment()
            #     elif choice == "3":
            #         print("View all equipment under $50 at the Sporting Goods Store:")
            #         equipments_less_than_50()
            #     elif choice == "4":
            #         print("Return to department menu")
            #         list_departments()
            #     elif choice == "5":
            #         exit_program()
            #     else:
            #         print("Not a valid option")
            # elif choice == "2":
            #     list_department_equipments()
            #     print("\n")
            #     menu3()
            #     choice = input("> ")
            #     if choice == "1":
            #         print("Add equipment to department")
            #         create_equipment()
            #     elif choice == "2":
            #         print("Delete equipment from department")
            #         delete_equipment()
            #     elif choice == "3":
            #         print("View all equipment under $50 at the Sporting Good Store: ")
            #         equipments_less_than_50()
            #     elif choice == "4":
            #         print("Return to department menu")
            #         list_departments()
            #     elif choice == "5":
            #         exit_program()
            #     else:
            #         print("Not a valid option")
            #         exit_program()
            # elif choice == "3":
            #     list_department_equipments()
            #     print("\n")
            #     menu3()
            #     choice = input("> ")
            #     if choice == "1":
            #         print("Add equipment to department")
            #         create_equipment()
            #     elif choice == "2":
            #         print("Delete equipment from department")
            #     elif choice == "3":
            #         print("View all equipment under $50 at the Sporting Good Store: ")
            #         list_departments()
            #     elif choice == "4":
            #         print("Return to department menu")
            #         list_departments()
            #     elif choice == "5":
            #         exit_program()
            #     else:
            #         print("Not a valid option")
            # elif choice == "4":
            #     exit_program()       