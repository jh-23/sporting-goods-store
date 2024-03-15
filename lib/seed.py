#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.department import Department
from models.equipment import Equipment

def seed_database():
    Equipment.drop_table()
    Department.drop_table()
    Department.create_table()
    Equipment.create_table()
    
# Create seed data

    outdoors = Department.create("Outdoors", "West Wing of Sporting Goods store")
    fitness = Department.create("Fitness", "East Wing of Sporting Goods store")
    sports = Department.create("Sports", "North Wing of Sporting Good store")
    Equipment.create("Magellan Outdoors Tent", 40, "4 person tent with 4.7 ft. center height", outdoors.id)
    Equipment.create("YETI Tundra 45 Cooler", 300, "Capable of storing 28 cans using a 2:1 ice-to-can ratio", outdoors.id)
    Equipment.create("GPS Fishfinder", 1100, "Offers a clear, colorful view of the water in 1280 x 720 resolution", outdoors.id)
    Equipment.create("Bowflex adjustable dumbell set", 429, "Easy to use selection dials that enable you to adjust your resistance from 5 lbs to 52.5 lbs", fitness.id)
    Equipment.create("Fitness Trampoline", 60, "features elastic resistance bands for optimal bounce", fitness.id)
    Equipment.create("Whey Protein Powder", 80, "Enjoy a sweet flavor with fast acting results", fitness.id)
    Equipment.create("Wilson Men's Golf Club Set", 330, "High Launch technology promotes distance and accuracy with every shot", sports.id)
    Equipment.create("Franklin 2-Player Pickleball Set", 35, "The 7-ply wood construction affords durabililty, while the nonslip grip handle offers comfort", sports.id)
    Equipment.create("Tennis Balls", 4, "1 can (3 pack) for hard court play", sports.id)

seed_database()
print("Seeded database")

