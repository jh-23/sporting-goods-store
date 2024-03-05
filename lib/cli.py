# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    
    sportsEquipment = []
    
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("Adding sports equipment...")
            nEquipment = input("Enter the title of the sports equipment: ")
            nPrice = input("Enter the price of the new sports equipment: ")
            nDescription = input("Enter the description of the new sports equipment: ")
            sportsEquipment.append([nEquipment, nPrice, nDescription])
        elif choice == "2":
            print("View sports equipment by title...")
            keyword = input("Enter title of equpiment: ")
            for equipment in sportsEquipment:
                if keyword in equipment:
                    print(equipment)
        elif choice == "3":
            print("Displaying all sports equipment...")
            print(sportsEquipment)
            for i in range(len(sportsEquipment)):
                print(sportsEquipment[i])
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add sports equipment")
    print("2. View sports equipment by title")
    print("3. Show all sports equipment")
        


if __name__ == "__main__":
    main()
