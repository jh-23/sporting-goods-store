# lib/cli.py

from helpers import (
    exit_program,
    list_departments,
    create_department,
    delete_department,
    show_all_department_details,
    create_equipment,
    show_equipment_details,
    delete_equipment,
    equipments_less_than_50, 
    select_department_equipment
)

def main_menu():
    print("------Welcome to the Sporting Goods Store!--------")
    print("\n")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. To display all Sporting Goods Department's")
    print("\n")

def department_menu_options():
    print("Please select which option you would like to do next: ")
    print("\n")
    print("0. Exit the program")
    print("1. To display all Sporting Goods Department's again: ")
    print("2. To see all the details of each Sports Department")
    print("3. Select a Sports department to view its equipment")
    print("4. To add a department to the Sporting Goods Store")
    print("5. To delete a department from the Sporting Goods Store")
    print("6. Type B or b to go back to the previous menu")
    print("\n")
    
def equipment_menu_options():
    print("\n")
    print("Select what you would like to do with the equipment of the Sporting Goods Department: ")
    print("\n")
    print("1. Add equipment to this department")
    print("2. Delete equipment from this department")
    print("3. Show specific equipment details")
    print("4. To go back to the previous menu")
    print("5. Exit the program")
    print("\n")
    
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
            print("\n")
        elif choice == "2":
            show_all_department_details()
        elif choice == "3":
            list_departments()
            print("\n")
            department = select_department_equipment()
            print("\n")
            equipments_menu(department)
        elif choice == "4":
            create_department()
        elif choice == "5":
            delete_department()
        elif choice == "B" or "b":
            main()
        else:
            print("Invalid Choice")
            
def equipments_menu(department):
    while True:
        equipment_menu_options()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_equipment(department)
        elif choice == "2":
            delete_equipment()
        elif choice == "3":
            show_equipment_details(department)
        elif choice == "4":
            departments_menu()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
