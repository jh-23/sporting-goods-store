# lib/helpers.py
from models.department import Department
from models.equipment import Equipment

def exit_program():
    print("\n")
    print("Goodbye!  Please visit the Sporting Goods Store again!")
    print("\n")
    exit()

def list_departments():
    departments = Department.get_all()
    print("\n")
    for i, department in enumerate(departments, start=1):
        print(f'{i}. {department.name}')
        
def show_all_department_details():
    departments = Department.get_all()
    for i, department in enumerate(departments, start=1):
        print(f'{i}. Department: {department.name}, Department location in store: {department.location}')
        
def create_department():
    name = input("Enter the Sporting Goods Department's name: ")
    location = input("Enter the Sporting Goods Department location in the store: ")
    try: 
        department = Department.create(name, location)
        print(f'Success: {department.name}')
        print("\n")
        print("Sporting Goods Store Departments: ")
        print("\n")
        return list_departments()
    except Exception as exc:
        print("Error creating Sporting Goods department: ", exc)

def delete_department():
    print("\n")
    number = int(input("Enter the number associated with the Sporting Goods department you wish to delete: "))
    departments = Department.get_all()
    if number <= len(departments):
        department = departments[number - 1]
        department.delete()
        print(f'Department: {department.name} deleted')
        print("\n")
        print("Sporting Goods Store Departments: ")
        print("\n")
        return list_departments()
    else:
        print(f'Department: {department.name} not found')
        
def update_department():
    print("\n")
    number = int(input("Enter the number associated with the Sporting Goods Department you wish to update: "))
    departments = Department.get_all()
    if number <= len(departments):
        department = departments[number - 1]
        try:
            name = input("Enter the department's updated name (or press <Enter> to not update Department name): ").title()
            if name:
                department.name = name
            location = input("Enter the department's updated store location (or press <Enter> to not update the Department's location): ").title()
            if location:
                department.location = location
            department.update()
            print(f'Department details updated successfully: {department.name}, {department.location}')
            print("\n")
            return list_departments()
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department: Number is not a valid option')
                    
def select_department_equipment():
    print("\n")
    number = int(input("Enter the number of department you wish to view: "))
    print("\n")
    departments = Department.get_all()
    if number <= len(departments):
        department = departments[number - 1]
        equipment_list = department.equipments()
        print(f'Please see the {department.name} equipment list: ')
        print('\n')
        for i, equipment in enumerate(equipment_list, start=1):
            print(f'{i}. Equipment: {equipment.name}')
        return department
    else:
        print("Not a valid option")
        
def show_equipment_details(department):
    equipment_list = department.equipments()
    for i, equipment in enumerate(equipment_list, start=1):
        print(f'{i}. {equipment.name}')
    print("\n")
    number = int(input("Enter the equipment number to view its details: "))
    print("\n")
    if number <= len(equipment_list):
        equipment = equipment_list[number - 1]
        print(f'Please see the {department.name} equipment: ')
        print("\n")
        print(f'{i}. Equipment: {equipment.name}, Price($): {equipment.price}, Description: {equipment.description}')
        return equipment
    else:
        print("Not a valid option")
        return equipment

def create_equipment(department):
    name = input("Enter the equipment's name: ").title()
    price = input("Enter the equipment's price: ")
    description = input("Enter the equipment's description: ")
    try:
        equipment = Equipment.create(name, int(price), description, department.id)
        print(f'Success: {equipment.name} created')
        print("\n")
        equipment_list = department.equipments()
        print(f'{department.name} Department equipment list: ')
        print("\n")
        for i, equipment in enumerate(equipment_list, start=1):
            print(f'{i}. {equipment.name}')
    except Exception as exc:
        print("Error creating equipment: ", exc)
        
def update_equipment_details(department):
    equipment_list = department.equipments()
    for i, equipment in enumerate(equipment_list, start=1):
        print(f'{i}. {equipment.name}')
    print("\n")
    number = int(input("Enter the equipment number you wish to update its details: "))
    print("\n")
    if number <= len(equipment_list):
        equipment = equipment_list[number - 1]
        try:
            name = input("Enter the equipment's updated name (or press <Enter> to not update): ")
            if name:
                equipment.name = name
            price = int(input("Enter the equipment's updated price with an integer (or press <Enter> to not update): "))
            if price:
                equipment.price = price
            description = input("Enter the equipment's updated description (or press <Enter> to not update): ")
            if description:
                equipment.description = description
            equipment.update()
            print("\n")
            print(f'Equipment details updated successfully: Equipment: {equipment.name}, Price ($): {equipment.price}, Description: {equipment.description}')
        except Exception as exc:
            print("Error updating equipment: ", exc)
    else:
        print("equipment not a valid option")

def delete_equipment(department):
    number = int(input("Enter the number associated with the equipment you wish to delete: "))
    equipment_list = department.equipments()
    if number <= len(equipment_list):
        equipment = equipment_list[number - 1]
        equipment.delete()
        print("\n")
        print(f'Equipment: {equipment.name} deleted')
        equipment_list = department.equipments()
        print("\n")
        print(f'{department.name} Department equipment list: ')
        for i, equipment in enumerate(equipment_list, start=1):
            print(f'{i}. {equipment.name}')
    else:
        print(f'Equipment: {equipment.name} not found')
    








 
def equipments_less_than_50():
    equipments = Equipment.get_all()
    for equipment in equipments:
        if equipment.price <= 50:
            print(equipment.name)
        

            