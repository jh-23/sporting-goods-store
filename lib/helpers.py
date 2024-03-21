# lib/helpers.py
from models.department import Department
from models.equipment import Equipment

def exit_program():
    print("Goodbye!  Please visit the Sporting Goods Store again!")
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
    except Exception as exc:
        print("Error creating Sporting Goods department: ", exc)
    print("\n")
    print("Sporting Goods Store Departments: ")
    print("\n")
    return list_departments()

def delete_department():
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
        print(f'Department: {department} not found')
               
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
        print(i, equipment.name)
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
        

















# def create_equipment(department):
#     name = input("Enter the equipment's name: ")
#     price = input("Enter the equipment's price: ")
#     description = input("Enter the equipment's description: ")
#     try: 
#         equipment = Equipment.create(name, int(price), description, department.id)
#         print(f'Success: {equipment}')
#     except Exception as exc:
#         print("Error creating equipment: ", exc)

    
    


# def create_equipment(department):
#     name = input("Enter the equipment's name: ")
#     price = input("Enter the equipment's price: ")
#     description = input("Enter the equipment's description: ")
#     # department_id = input("Enter the equipment's department id: ")
#     # print(type(department_id))
#     try:
#         equipment = Equipment.create(name, int(price), description, department.id)
#         print(f'Success: {equipment}')
#     except Exception as exc:
#         print("Error creating equipment: ", exc)

# def list_department_equipments():
#     id_ = input("Enter the department's id: ")
#     if department := Department.find_by_id(id_):
#         equipments = department.equipments()
#         for equipment in equipments:
#             print(equipment)
#     else:
#         print(f'Department {id_} not found')



# #         for i, value in enumerate(values, start=1):
# # ...     print(i, value)



#Department
    
# def list_departments():
#     departments = Department.get_all()
#     for department in departments:
#         print(department)
        


# def update_department():
#     id_ = input("Enter the Sporting Goods department id: ")
#     if department := Department.find_by_id(id_):
#         try:
#             name = input("Enter the Sporting Goods Department's new name: ")
#             department.name = name
#             location = input("Enter the department's new location: ")
#             department.location = location
            
#             department.update()
#             print(f'Success: {department}')
#         except Exception as exc:
#             print("Error updating Sporting Goods department: ", exc)
#     else:
#         print(f'Department {id_} not found')
    
        
# #Equipments
    
# def list_equipments():
#     equipments = Equipment.get_all()
#     # for equipment in equipments:
#     #     print(f'We have {equipment.name}')
#     for i, equipment in enumerate(equipments, start=1):
#         print(i, equipment.name)
        
# #         for i, value in enumerate(values, start=1):
# # ...     print(i, value)
        
# def find_equipment_by_name():
#     name = input("Enter the equipment's name: ")
#     equipment = Equipment.find_by_name(name)
#     print(equipment) if equipment else print(f'Equipment {name} not found')
    
    

        
# def update_equipment():
#     id_ = input("Enter the equipment's id: ")
#     if equipment := Equipment.find_by_id(id_):
#         try:
#             name = input("Enter the equipment's new name: ")
#             equipment.name = name
#             price = input("Enter the equipment's new price: ")
#             equipment.price = price
#             department_id = input("Enter the equipment's new department id: ")
#             equipment.department_id = int(department_id)
            
#             equipment.update()
#             print(f'Success: {equipment}')
#         except Exception as exc:
#             print("Error updating equipment: ", exc)
#     else:
#         print(f'Equipment {id_} not found')

# def delete_equipment():
#     id_ = input("Enter the equpiment's id: ")
#     if equipment := Equipment.find_by_id(id_):
#         equipment.delete()
#         print(f'Equipment {id_} deleted')
#     else:
#         print(f'Equipment {id_} not found')
        


    # call list_departments()
    # ask user to pick one 
    # department = Department.get_all()
    # list_department_equipments(department)
    
    
    # def pick_department():
#     name = input("Enter the name of the Sporting Good's department you wish to view: ").title()
#     if department := Department.find_by_name(name):
#         equipments = department.equipments()
#         for i, equipment in enumerate(equipments, start=1):
#             print(i, f'Department: {department.name}, Equipment: {equipment.name}, Price ($): {equipment.price}, Description: {equipment.description}')


# def list_department_equipments():
#     name = input("Enter the name of the Sporting Good's department you wish to view: ").title()
#     if department := Department.find_by_name(name):
#         equipments = department.equipments()
#         for i, equipment in enumerate(equipments, start=1):
#             print(i, f'Department: {department.name}, Equipment: {equipment.name}, Price ($): {equipment.price}, Description: {equipment.description}')
            