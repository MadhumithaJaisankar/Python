# Base class 
class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")


class Processor:
    def process_data(self):
        print("Processing data")

class Storage:
    def store_data(self):
        print("Storing data")

class Display:
    def show_display(self):
        print("Displaying information")

class Computer(Processor, Storage, Display, ElectronicDevice):
    def __init__(self, brand, model):
        # Call constructors of multiple base classes
        Processor.__init__(self)
        Storage.__init__(self)
        Display.__init__(self)
        ElectronicDevice.__init__(self, brand, model)



computer = Computer("XYZ", "Desktop")

computer.display_info()       # Inherited from ElectronicDevice
computer.process_data()       # Inherited from Processor
computer.store_data()         # Inherited from Storage
computer.show_display()       # Inherited from Display
