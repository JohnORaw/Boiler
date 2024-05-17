"""
Boiler Class
"""

# Create a class 
class Boiler():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for Boiler")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)



my_class1 = Boiler("Morning JOR!")
my_class1.my_method()
print(type(my_class1))


"""
OilBurner Class
"""

# Create a class 
class OilBurner():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for Oil Burner")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)



my_class1 = OilBurner("Morning JOR!")
my_class1.my_method()
print(type(my_class1))

"""
WoodBurner Class
"""

# Create a class 
class WoodBurner():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for Wood Burner")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)



my_class1 = WoodBurner("Morning JOR!")
my_class1.my_method()
print(type(my_class1))

"""
Immersion Class
"""

# Create a class 
class Immersion():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for Immersion")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)



my_class1 = Immersion("Morning JOR!")
my_class1.my_method()
print(type(my_class1))
