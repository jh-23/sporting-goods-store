# lib/cli.py

from helpers import (
    exit_program,
    list_departments,
    create_department,
    delete_department,
    update_department,
    show_all_department_details,
    create_equipment,
    show_equipment_details,
    delete_equipment,
    select_department_equipment,
    update_equipment_details
)

def main_menu():
    print("\n")
    print("------Welcome to the Sporting Goods Store!------")
    print("\n")
    print("Please select an option:")
    print("\n")
    print("0. Exit the program")
    print("1. To display all Sporting Goods Department's")
    print("\n")

def department_menu_options():
    print("\n")
    print("Please select which option you would like to do next: ")
    print("\n")
    print("0. Exit the program")
    print("1. To display all Sporting Goods Department's again: ")
    print("2. To see all the details of each Sporting Goods Department")
    print("3. Select a Sporting Goods Department to view its equipment")
    print("4. To add a Department to the Sporting Goods Store")
    print("5. To delete a Department from the Sporting Goods Store")
    print("6. To update a Department's information")
    print("7. To return to the previous menu")
    print("\n")
    
def equipment_menu_options():
    print("\n")
    print("Select what you would like to do with the equipment of this Sporting Goods Department: ")
    print("\n")
    print("1. Add equipment to this department")
    print("2. Delete equipment from this department")
    print("3. Show specific equipment details")
    print("4. To update an equipment's information")
    print("5. To return to the previous menu")
    print("6. Exit the program")
    print("\n")
    
def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Sporting Goods Store Department's: ")
            list_departments()
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
            show_all_department_details()
        elif choice == "3":
            list_departments()
            department = select_department_equipment()
            equipments_menu(department)
        elif choice == "4":
            create_department()
        elif choice == "5":
            delete_department()
        elif choice == "6":
            update_department()
        elif choice == "7":
            main()
        else:
            print("Invalid Option")
            
def equipments_menu(department):
    while True:
        equipment_menu_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_equipment(department)
        elif choice == "2":
            delete_equipment(department)
        elif choice == "3":
            show_equipment_details(department)
        elif choice == "4":
            update_equipment_details(department)
        elif choice == "5":
            departments_menu()
        elif choice == "6":
            exit_program()
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
