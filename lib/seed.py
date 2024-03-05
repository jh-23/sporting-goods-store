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
Equipment.create("Magellan Outdoors Tent", 39.99, "4 person tent with 4.7 ft. center height", outdoors.id)
Equipment.create("YETI Tundra 45 Cooler", 300, "Capable of storing 28 cans using a 2:1 ice-to-can ratio", outdoors.id)
Equipment.create("Bowflex adjustable dumbell set", 429, "Easy to use selection dials that enable you to adjust your resistance from 5 lbs to 52.5 lbs", fitness.id)
Equipment.create("Fitness Trampoline", 59.99, "features elastic resistance bands for optimal bounce", fitness.id)
Equipment.create("Wilson Men's Golf Club Set", 329.99, "High Launch technology promotes distance and accuracy with every shot", sports.id)
Equipment.create("Franklin 2-Player Pickleball Set", 34.99, )