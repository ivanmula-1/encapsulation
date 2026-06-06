class Pet:
    def __init__(self):
        """Initialize private attributes with empty/default values."""
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
        
     def set_name(self, name):
        self.__name = name
         
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
