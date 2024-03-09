# lib/cli.py

from helpers import (
    exit_program,
    list_departments

)

def main():
    
    while True:
        print("------Welcome to the Sporting Good Store!--------")
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("List Sporting Goods Store Department's: ")
            list_departments()


            if choice == "1":
                print("Outdoors")
            elif choice == "2":
                print("fitness")
            elif choice == "3":
                print("sports")
            elif choice == "4":
                exit_program()       
        else:
            print("Invalid choice")

            
            
            
            
            
            
        #     while True:
        #         menu()
        #         choice = input("> ")
        #         if choice == "1":
        #             print("Display equipment in specific Sporting Goods")

       
       
       
        # elif choice == "2":
        #     print("Adding sports equipment...")
        #     create_equipment()
        # elif choice == "3":
        #     print("Delete sports equipment")
        #     delete_equipment()
        # elif choice == "4":
        #     print("View equipments by department...")
        #     list_department_equipments()
        # elif choice == "5":
        #     print("Find equipment by name...")
        #     find_equipment_by_name()
        # else:
        #     print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Display all Sporting Goods Departments")
    
# def menu2():
#     print("Please select a Sporting Goods Department:")
#     print("1. Print outdoors equipment")
#     print("2. Print fitness equipment")
#     print("3. Print sports equipment")
#     print("4. Exit the program")

        


if __name__ == "__main__":
    main()
