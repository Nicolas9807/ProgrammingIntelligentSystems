class Car():
    
    def __init__(self, brand, model, year, num_doors, owner):
        self.brand = brand
        self.model = model
        self.year = year
        self.num_doors = num_doors
        self.owner = owner
    
    def description_car(self):
        print ("\n")
        print("Brand name of this car is " + str(self.brand))
        print("Model name of this car is " + str(self.model))
        print("This car was built in " + str(self.year) + ".")
        print("This car have a " + str(self.num_doors) + " doors")
        print(self.owner + " is owner of this car")

def display_message1():
	return "All about Python!"
    
car1 = Car('Opel', 'Astra H', 2009, 4, 'Jack Morrison')
car1.description_car()

car2 = Car('BMW', 'X5', 2012, 6, 'Paul McCartney')
car2.description_car()

car3 = Car('Dodge', 'Carger', 1969, 4, 'Freddie Mercury')
car3.description_car()
