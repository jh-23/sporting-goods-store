#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.Department import Department
from models.Equipment import Equipment

def seed_database():
    Equipment.drop_table()
    Department.drop_table()
    Department.create_table()
    Equipment.create_table()
    
# Create seed data

outdoors = Department.create("Outdoors", "West Wing of Sporting Goods store")
fitness = Department.create("Fitness", "East Wing of Sporting Goods store")
sports = Department.create("Sports", "North Wing of Sporting Good store")
Equipment.create("")