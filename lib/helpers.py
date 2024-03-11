# lib/helpers.py
from models.department import Department
from models.equipment import Equipment

def exit_program():
    print("Goodbye!")
    exit()

def list_departments():
    departments = Department.get_all()
    for i, department in enumerate(departments, start=1):
        print(i, department.name)
        
def list_department_equipments():
    name = input("Enter the Sporting Good's department name: ")
    if department := Department.find_by_name(name):
        equipments = department.equipments()
        for i, equipment in enumerate(equipments, start=1):
            print(i, f'Equipment: {equipment.name}, Price ($): {equipment.price}, Description: {equipment.description}')
            
def create_equipment():
    name = input("Enter the equipment's name: ")
    price = input("Enter the equipment's price: ")
    description = input("Enter the equipment's description: ")
    department = input("Enter the department's name: ")
    if department == Department.name:
        try:
            equipment = Equipment.create(name, int(price), description, department.id)
            print(f'Success: {equipment}')
        except Exception as exc:
            print("Error creating equipment: ", exc)
        
def delete_equipment():
    name = input("Enter the equipment's name: ")
    if equipment := Equipment.find_by_name(name.title()):
        equipment.delete()
        print(f'Equipment {name} deleted')
    else:
        print(f'Equipment {name} not found')
    
        
        
        
        

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
        
