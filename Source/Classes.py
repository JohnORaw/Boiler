"""
Boiler Class
"""

# Create a class 
class Boiler():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, parameter1, debug_flag):
        
        # Create attributes and set initial values
        self.message = parameter1
        # If debug is required, send messages
        self.debug = debug_flag       
        if self.debug:
            print(f"Executing constructor for {parameter1}")

    def my_method(self):
        print(self.message)



class Heater():

# Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        
        # Create attributes and set initial values
        self.debug = True
        self.message = ""
        if self.debug:
            print("Executing constructor for base heater class")

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from base")
        # Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc
    
    def my_method(self):
        print(self.message)



"""
OilBurner Class
"""

# Create a class 
class OilBurner(Heater):
    
    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Heater.__init__(self)
        self.debug = True
        if self.debug:
            print(f"Executing constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1

    def configure(self):
        print("Configuring Oil Burner")



"""
WoodBurner Class
"""

# Create a class 
class WoodBurner(Heater):
    
    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Heater.__init__(self)
        self.debug = True
        if self.debug:
            print(f"Executing constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""

    def configure(self):
        print("Configuring Wood Burner")



"""
Immersion Class
"""

# Create a class 
class Immersion(Heater):
    
    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Heater.__init__(self)
        self.debug = True
        if self.debug:
            print(f"Executing constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""

    def configure(self):
        print("Configuring Immersion")
