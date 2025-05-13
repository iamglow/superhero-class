 superheroclass Superhero:
    def __init__(self, name, superpower, level):
        self.name = name          # Name of the superhero
        self.__superpower = superpower  # Superpower (Encapsulated)
        self.level = level        # Power level

    def display_info(self):
        print(f"Superhero Name: {self.name}")
        print(f"Superpower: {self.__superpower}")
        print(f"Power Level: {self.level}")

    def use_superpower(self):
        print(f"{self.name} is using their {self.__superpower}!")
        
    def upgrade_level(self):
        self.level += 1
        print(f"{self.name}'s power level increased to {self.level}!")

    # A method to get the private superpower attribute (getter method)
    def get_superpower(self):
        return self.__superpower
-class
