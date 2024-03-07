# lib/helpers.py
from models.Department import Department
from models.Equipment import Equipment

def exit_program():
    print("Goodbye!")
    exit()
    
def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)
        
def find_department_by_name():
    name = input("Enter the Sporting Good department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')

def find_department_by_id():
    name = input("Enter the Sporting Goods department's name: ")
    department = Department.find_by_id(name)
    print(department) if department else print(f'Department {name} not found')

def create_department():
    name = input("Enter the Sporting Goods Store Department name: ")
    location = input("Enter the location of the Department in the Sporting Good Store: ")
    try:
        Department = Department.create(name, location)
        print(f'Success: {Department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    id_ = input("Enter the Sporting Goods department id: ")
    if Department := Department.find_by_id(id_):
        try:
            name = input("Enter the Sporting Goods Department's new name: ")
            Department.name = name
            location = input("Enter the department's new location: ")
            Department.location = location
            
            Department.update()
            print(f'Success: {Department}')
        except Exception as exc:
            print("Error updating Sporting Goods department: ", exc)
    else:
        print(f'Department {id_} not found')
    
def delete_department():
    id_ = input("Enter the Sporting Goods Department id: ")
    if Department := Department.find_by_id(id_):
        Department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')
        
#Equipments
    
def list_equipments():
    equipments = Equipment.get_all()
    for equipment in equipments:
        print(equipment)
        
def find_equipment_by_name():
    name = input("Enter the equipment's name: ")
    equipment = Equipment.find_by_name(name)
    print(equipment) if equipment else print(f'Equipment {name} not found')
    
def find_equipment_by_id():
    id_ = input("Enter the equipment's id: ")
    equipment = Equipment.find_by_id(id_)
    print(equipment) if equipment else print(f'Equipment {id_} not found')
    
def create_equipment():
    name = input("Enter the equipment's name: ")
    price = input("Enter the equipment's price: ")
    description = input("Enter the equipment's description: ")
    department_id = input("Enter the equipment's department id: ")
    print(type(department_id))
    try:
        equipment = Equipment.create(name, int(price), description, int(department_id))
        print(f'Success: {equipment}')
    except Exception as exc:
        print("Error creating equipment: ", exc)
        
def update_equipment():
    id_ = input("Enter the equipment's id: ")
    if equipment := Equipment.find_by_id(id_):
        try:
            name = input("Enter the equipment's new name: ")
            equipment.name = name
            price = input("Enter the equipment's new price: ")
            equipment.price = price
            department_id = input("Enter the equipment's new department id: ")
            equipment.department_id = int(department_id)
            
            equipment.update()
            print(f'Success: {equipment}')
        except Exception as exc:
            print("Error updating equipment: ", exc)
    else:
        print(f'Equipment {id_} not found')
        
