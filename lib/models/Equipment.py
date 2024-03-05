#lib/models/Equipment.py
from models.__init__ import CURSOR, CONN
from models.Department import Department

class Equipment:
    
    all = {}
    
    def __init__(self, name, price, description, id=None):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
            
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self.price = price
        else:
            raise ValueError(
                "price must be a non-empty string"
            )
            
    @property
    def description(self):
        return self.description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError(
                "description must be a non-empty string"
            )
            
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Employee instances """
        sql = """
            CREATE TABLE IF NOT EXISTS equipments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INT,
            description TEXT,
            FOREIGN KEY (department_id) REFERENCES departments(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Equipment instances """
        sql = """
            DROP TABLE IF EXISTS equipments;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
            """ Insert a new row with the name, price, and description values of the current Equipment object.
            Update object id attribute using the primary key value of new row.
            Save the object in local dictionary using table row's PK as dictionary key"""
            sql = """
                INSERT INTO equipments (name, price, description)
                VALUES (?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.price, self.description))
            CONN.commit()

            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
            
    def update(self):
        """Update the table row corresponding to the current Equipment instance."""
        sql = """
            UPDATE equipments
            SET name = ?, price = ?, description = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.description))
        CONN.commit()
    
    def delete(self):
        """Delete the table row corresponding to the current Equipment instance,
        delete the dictionary entry, and reassign id attribute"""
        
        sql = """
            DELETE FROM equipments
            WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        
        del type(self).all[self.id]
        
        self.id = None
        
    @classmethod
    def create(cls, name, price, description):
        """Initialize a new Equipment instance and save the object to the database"""
        equipment = cls(name, price, description)
        equipment.save()
        return equipment 
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an Equipment object having the attribute values from the table row."""
        
        equipment = cls.all.get(row[0])
        if equipment:
            equipment.name = row[1]
            equipment.price = row[2]
            equipment.description = row[3]
        else:
            equipment = cls(row[1], row[2], row[3])
            equipment.id = row[0]
            cls.all[equipment.id] = equipment
        return equipment
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Equipment object per table row"""
        sql = """
            SELECT *
            FROM equipments
        """
        
        rows = CURSOR.execute(sql).fetchall()
        
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Equipment object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM equipments
            WHERE id = ?
        """
        
        row = CURSOR.exectue(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return Equipment object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM equipments
            WHERE name is ? 
        """
        
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
            
        